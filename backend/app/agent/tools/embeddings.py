import uuid

from app.db import get_client
from app.ingest.embed import embed_text


def embed_query(text: str) -> dict:
    """Embed a natural-language search query and stage it in ClickHouse.

    Returns a query_id. Use it in SQL as:
      WITH (SELECT embedding FROM query_vectors WHERE query_id = '<query_id>') AS q
      ... ORDER BY cosineDistance(embedding, q)

    Args:
        text: the search phrase describing the shots to find.
    """
    query_id = uuid.uuid4().hex
    vector = embed_text(text)
    get_client().insert("query_vectors", [[query_id, vector]], column_names=["query_id", "embedding"])
    return {"query_id": query_id, "dimensions": len(vector)}
