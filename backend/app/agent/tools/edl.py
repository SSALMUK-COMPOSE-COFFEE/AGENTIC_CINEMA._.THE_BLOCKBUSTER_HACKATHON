import uuid

from google.adk.tools.tool_context import ToolContext

from app.db import get_client


def _tc(seconds: float, fps: float) -> str:
    fps_i = round(fps)
    frames = round(seconds * fps)
    f = frames % fps_i
    s = frames // fps_i
    return f"{s // 3600:02d}:{(s % 3600) // 60:02d}:{s % 60:02d}:{f:02d}"


def build_edl(shot_ids: list[str], title: str = "SHOT MEMORY SEQUENCE", fps: float = 24.0) -> dict:
    """Build a CMX3600 EDL for an ordered list of shot_ids and return the text plus the timeline.

    Args:
        shot_ids: ordered shot ids, e.g. ["charade:00012", "charade:00340"].
        title: sequence title written into the EDL header.
        fps: timeline frame rate.
    """
    client = get_client()
    rows = client.query(
        "SELECT shot_id, film_title, t_in, t_out, thumbnail_uri, proxy_uri, caption FROM shots WHERE shot_id IN %(ids)s",
        parameters={"ids": shot_ids},
    ).named_results()
    by_id = {r["shot_id"]: r for r in rows}
    lines = [f"TITLE: {title}", "FCM: NON-DROP FRAME", ""]
    timeline = []
    rec = 0.0
    for n, sid in enumerate(shot_ids, start=1):
        r = by_id.get(sid)
        if not r:
            continue
        dur = r["t_out"] - r["t_in"]
        lines.append(
            f"{n:03d}  AX       V     C        {_tc(r['t_in'], fps)} {_tc(r['t_out'], fps)} {_tc(rec, fps)} {_tc(rec + dur, fps)}"
        )
        lines.append(f"* FROM CLIP NAME: {r['film_title']}")
        lines.append(f"* COMMENT: {r['caption'][:80]}")
        timeline.append({
            "shot_id": sid, "film_title": r["film_title"], "t_in": r["t_in"], "t_out": r["t_out"],
            "rec_in": rec, "rec_out": rec + dur, "thumbnail_uri": r["thumbnail_uri"], "proxy_uri": r["proxy_uri"],
            "caption": r["caption"],
        })
        rec += dur
    return {"edl": "\n".join(lines), "timeline": timeline, "total_seconds": rec}


def save_sequence(intent: str, shot_ids: list[str], tool_context: ToolContext) -> dict:
    """Persist an assembled sequence so it can be reloaded or exported later.

    Args:
        intent: the editor's request that produced the sequence.
        shot_ids: ordered shot ids.
    """
    session_id = str(tool_context.state.get("session_id") or tool_context.session.id)
    sequence_id = uuid.uuid4().hex
    get_client().insert(
        "sequences", [[sequence_id, session_id, intent, shot_ids]],
        column_names=["sequence_id", "session_id", "intent", "shot_ids"],
    )
    return {"sequence_id": sequence_id, "shot_count": len(shot_ids)}
