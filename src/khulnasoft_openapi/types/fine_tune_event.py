# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["FineTuneEvent"]


class FineTuneEvent(BaseModel):
    created_at: Optional[int] = None

    level: Optional[str] = None

    message: Optional[str] = None

    object: Optional[str] = None
