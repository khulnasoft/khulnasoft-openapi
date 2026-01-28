# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .engine import Engine
from .._models import BaseModel

__all__ = ["EngineListResponse"]


class EngineListResponse(BaseModel):
    data: Optional[List[Engine]] = None

    object: Optional[str] = None
