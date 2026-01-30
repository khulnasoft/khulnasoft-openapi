# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .fine_tune_event import FineTuneEvent

__all__ = ["FineTuneGetEventsResponse"]


class FineTuneGetEventsResponse(BaseModel):
    data: Optional[List[FineTuneEvent]] = None

    object: Optional[str] = None
