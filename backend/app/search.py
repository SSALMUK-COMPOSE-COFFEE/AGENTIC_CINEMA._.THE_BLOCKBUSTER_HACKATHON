from app.db import get_client

SHOT_COLUMNS = (
    "shot_id, film_id, film_title, shot_index, t_in, t_out, caption, people_count, "
    "toString(time_of_day) AS time_of_day, toString(interior) AS interior, weather, "
    "toString(shot_size) AS shot_size, toString(camera_move) AS camera_move, emotion, tension, "
    "dialogue_present, dominant_colors, objects, characters, thumbnail_uri, proxy_uri"
)


def list_films() -> list[dict]:
    q = """
    SELECT film_id, argMax(title, updated_at) AS title, argMax(year, updated_at) AS year,
           argMax(shot_count, updated_at) AS shot_count, toString(argMax(status, updated_at)) AS status,
           max(updated_at) AS last_update
    FROM films GROUP BY film_id ORDER BY title
    """
    return list(get_client().query(q).named_results())


def list_shots(film_id: str, offset: int = 0, limit: int = 60) -> list[dict]:
    q = f"SELECT {SHOT_COLUMNS} FROM shots WHERE film_id = %(f)s ORDER BY shot_index LIMIT %(l)s OFFSET %(o)s"
    return list(get_client().query(q, parameters={"f": film_id, "l": limit, "o": offset}).named_results())


def get_shots(shot_ids: list[str]) -> list[dict]:
    q = f"SELECT {SHOT_COLUMNS} FROM shots WHERE shot_id IN %(ids)s"
    rows = {r["shot_id"]: r for r in get_client().query(q, parameters={"ids": shot_ids}).named_results()}
    return [rows[s] for s in shot_ids if s in rows]


def similar_shots(shot_id: str, limit: int = 24) -> list[dict]:
    c = get_client()
    ref = c.query("SELECT embedding FROM shots WHERE shot_id = %(s)s LIMIT 1", parameters={"s": shot_id}).result_rows
    if not ref:
        return []
    q = f"""
    SELECT {SHOT_COLUMNS}, cosineDistance(embedding, %(q)s) AS dist
    FROM shots WHERE shot_id != %(s)s ORDER BY dist ASC LIMIT %(l)s
    """
    return list(c.query(q, parameters={"q": ref[0][0], "s": shot_id, "l": limit}).named_results())


def stats() -> dict:
    c = get_client()
    return {
        "films": c.command("SELECT uniqExact(film_id) FROM shots"),
        "shots": c.command("SELECT count() FROM shots"),
        "hours": round(float(c.command("SELECT sum(t_out - t_in) FROM shots") or 0) / 3600, 2),
    }
