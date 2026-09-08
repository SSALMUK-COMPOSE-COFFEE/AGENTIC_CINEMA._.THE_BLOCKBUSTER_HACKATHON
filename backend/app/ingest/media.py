import json
import subprocess
from dataclasses import dataclass
from pathlib import Path

PROXY_SECONDS = 10.0
PROXY_HEIGHT = 320
THUMB_POSITIONS = (0.25, 0.5, 0.75)


@dataclass(frozen=True)
class VideoInfo:
    fps: float
    duration: float
    width: int
    height: int


def probe(path: Path) -> VideoInfo:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
         "stream=r_frame_rate,width,height:format=duration", "-of", "json", str(path)],
        check=True, capture_output=True, text=True,
    ).stdout
    data = json.loads(out)
    stream = data["streams"][0]
    num, den = stream["r_frame_rate"].split("/")
    return VideoInfo(
        fps=float(num) / float(den),
        duration=float(data["format"]["duration"]),
        width=int(stream["width"]),
        height=int(stream["height"]),
    )


def _run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, capture_output=True)


def make_proxy(src: Path, t_in: float, t_out: float, dst: Path) -> Path:
    dst.parent.mkdir(parents=True, exist_ok=True)
    length = min(t_out - t_in, PROXY_SECONDS)
    _run([
        "ffmpeg", "-y", "-v", "error", "-ss", f"{t_in:.3f}", "-i", str(src), "-t", f"{length:.3f}",
        "-vf", f"scale=-2:{PROXY_HEIGHT}", "-r", "12", "-c:v", "libx264", "-preset", "veryfast", "-crf", "30",
        "-c:a", "aac", "-b:a", "48k", "-movflags", "+faststart", str(dst),
    ])
    return dst


def make_thumbnails(src: Path, t_in: float, t_out: float, dst_stem: Path) -> list[Path]:
    dst_stem.parent.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for i, frac in enumerate(THUMB_POSITIONS):
        t = t_in + (t_out - t_in) * frac
        dst = dst_stem.with_name(f"{dst_stem.name}_{i}.jpg")
        _run(["ffmpeg", "-y", "-v", "error", "-ss", f"{t:.3f}", "-i", str(src), "-frames:v", "1",
              "-vf", f"scale=-2:{PROXY_HEIGHT}", "-q:v", "4", str(dst)])
        paths.append(dst)
    return paths
