import os
from typing import Dict, List
from qdrant_client import QdrantClient

def get_qdrant_client() -> QdrantClient:
    """Get Qdrant client instance using environment variables"""
    try:
        qdrant_api_url = os.environ['QDRANT_API_URL']
        qdrant_api_key = os.environ['QDRANT_API_KEY']
    except KeyError as e:
        raise EnvironmentError(f"Required environment variable {e} is not set") from e
    
    qdrant_client = QdrantClient(
        url=qdrant_api_url, 
        api_key=qdrant_api_key,
        timeout=30.0 
    )

    return qdrant_client

def init_collection(
    qdrant_client: QdrantClient,
    collection_name: str,
    vector_size: int,
    # schema: str = ''
) -> QdrantClient:
    """"""
    from qdrant_client.http.api_client import UnexpectedResponse
    from qdrant_client.http.models import Distance, VectorParams

    try: 
        qdrant_client.get_collection(collection_name=collection_name)

    except (UnexpectedResponse, ValueError):
        qdrant_client.recreate_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            ),
    )

    return qdrant_client