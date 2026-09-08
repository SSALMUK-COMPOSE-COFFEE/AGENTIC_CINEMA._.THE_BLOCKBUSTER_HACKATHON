from dataclasses import dataclass

from scenedetect import ContentDetector, detect

MIN_SHOT_SECONDS = 1.0


@dataclass(frozen=True)
class ShotSpan:
    index: int
    t_in: float
    t_out: float

    @property
    def duration(self) -> float:
        return self.t_out - self.t_in


def detect_shots(video_path: str, threshold: float = 27.0) -> list[ShotSpan]:
    raw = detect(video_path, ContentDetector(threshold=threshold))
    spans = [(a.get_seconds(), b.get_seconds()) for a, b in raw]
    merged: list[list[float]] = []
    for t_in, t_out in spans:
        if merged and (t_out - t_in) < MIN_SHOT_SECONDS:
            merged[-1][1] = t_out
        else:
            merged.append([t_in, t_out])
    return [ShotSpan(i, a, b) for i, (a, b) in enumerate(merged)]
