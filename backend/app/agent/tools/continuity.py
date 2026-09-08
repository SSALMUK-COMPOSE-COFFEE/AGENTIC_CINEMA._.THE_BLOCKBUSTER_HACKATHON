from itertools import pairwise

from app.db import get_client

COLUMNS = "shot_id, toString(time_of_day) AS time_of_day, toString(interior) AS interior, weather, characters, dominant_colors, toString(shot_size) AS shot_size"


def check_metadata(shot_ids: list[str]) -> dict:
    """Apply the deterministic continuity rules to an ordered shot list using their ClickHouse metadata.

    Rules per adjacent pair (a, b):
      time_of_day differs and neither is 'unknown' -> mid
      interior differs and neither is 'unknown'    -> mid
      same character descriptor in both but no shared dominant color -> low

    Args:
        shot_ids: ordered shot ids in cut order.
    """
    rows = get_client().query(
        f"SELECT {COLUMNS} FROM shots WHERE shot_id IN %(ids)s", parameters={"ids": shot_ids}
    ).named_results()
    meta = {r["shot_id"]: r for r in rows}
    warnings = []
    ordered = [s for s in shot_ids if s in meta]
    for a, b in pairwise(ordered):
        ma, mb = meta[a], meta[b]
        if ma["time_of_day"] != mb["time_of_day"] and "unknown" not in (ma["time_of_day"], mb["time_of_day"]):
            warnings.append(_warn(a, b, "time_of_day", "mid",
                                  f"{a} is {ma['time_of_day']}, {b} is {mb['time_of_day']}"))
        if ma["interior"] != mb["interior"] and "unknown" not in (ma["interior"], mb["interior"]):
            warnings.append(_warn(a, b, "interior_exterior", "mid",
                                  f"{a} is {ma['interior']}, {b} is {mb['interior']}"))
        shared_people = set(ma["characters"]) & set(mb["characters"])
        if shared_people and not set(ma["dominant_colors"]) & set(mb["dominant_colors"]):
            warnings.append(_warn(a, b, "wardrobe_palette", "low",
                                  f"{', '.join(sorted(shared_people))} appears in both but the palettes share nothing"))
    return {"warnings": warnings, "checked_pairs": max(len(ordered) - 1, 0), "missing": [s for s in shot_ids if s not in meta]}


def _warn(a: str, b: str, rule: str, severity: str, explanation: str) -> dict:
    return {"pair": [a, b], "rule": rule, "severity": severity, "explanation": explanation, "suggested_replacement": None}
