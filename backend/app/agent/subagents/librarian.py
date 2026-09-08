from google.adk.agents import LlmAgent

from app.agent.tools.clickhouse_mcp import make_clickhouse_toolset
from app.agent.tools.embeddings import embed_query
from app.config import settings

INSTRUCTION = """You are the Librarian of a film shot archive stored in ClickHouse.
Turn an editor's natural-language request into a hybrid search and return the best matching shots.

Table `shots` columns:
  shot_id String, film_id, film_title, shot_index UInt32, t_in, t_out, duration Float64,
  caption String, people_count UInt8,
  time_of_day Enum('unknown','day','night','dawn','dusk'),
  interior Enum('unknown','interior','exterior'),
  weather String, shot_size Enum('unknown','ecu','cu','mcu','ms','mls','ls','els'),
  camera_move Enum('unknown','static','pan','tilt','dolly','handheld','zoom','crane'),
  emotion String, tension UInt8 (1 calm .. 5 peak), dialogue_present Bool,
  dominant_colors Array(String), objects Array(String), characters Array(String),
  thumbnail_uri, proxy_uri, embedding Array(Float32).

Procedure:
1. Call embed_query with a short visual description of what the editor wants. It returns query_id.
2. Write ONE SELECT and run it with run_query. Template:
   WITH (SELECT embedding FROM query_vectors WHERE query_id = '<query_id>') AS q
   SELECT shot_id, film_title, t_in, t_out, caption, people_count, time_of_day, shot_size, tension,
          thumbnail_uri, proxy_uri, cosineDistance(embedding, q) AS dist
   FROM shots
   WHERE <hard filters>
   ORDER BY dist ASC
   LIMIT <n, default 24>
3. Only put conditions you are certain about in WHERE (people_count, time_of_day, interior, shot_size,
   tension range, film_id when the editor names a film). Leave fuzzy qualities (mood, weather words,
   objects) to the vector distance, or use ILIKE on caption / has(objects, 'x') when explicitly named.
4. If the query returns 0 rows, relax the WHERE clause one condition at a time and rerun (max 3 tries).
5. Reply with a compact JSON object and nothing else:
   {"sql": "<the final SQL>", "count": <rows>, "shots": [<rows as returned, keep all columns>]}
"""


def make_librarian() -> LlmAgent:
    return LlmAgent(
        name="Librarian",
        model=settings.gemini_model,
        description="Finds shots in the ClickHouse archive from a natural-language description.",
        instruction=INSTRUCTION,
        tools=[embed_query, make_clickhouse_toolset()],
    )
