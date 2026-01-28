# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EngineSearchResponse", "Data"]


class Data(BaseModel):
    document: Optional[int] = None

    object: Optional[str] = None

    score: Optional[float] = None


class EngineSearchResponse(BaseModel):
    data: Optional[List[Data]] = None

    model: Optional[str] = None

    object: Optional[str] = None
