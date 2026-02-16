# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EngineCreateEmbeddingResponse", "Data"]


class Data(BaseModel):
    embedding: Optional[List[float]] = None

    index: Optional[int] = None

    object: Optional[str] = None


class EngineCreateEmbeddingResponse(BaseModel):
    data: Optional[List[Data]] = None

    model: Optional[str] = None

    object: Optional[str] = None
