# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .fine_tune_event import FineTuneEvent
from .khulna_soft_file import KhulnaSoftFile

__all__ = ["FineTune"]


class FineTune(BaseModel):
    id: Optional[str] = None

    created_at: Optional[int] = None

    events: Optional[List[FineTuneEvent]] = None

    fine_tuned_model: Optional[str] = None

    hyperparams: Optional[object] = None

    model: Optional[str] = None

    object: Optional[str] = None

    organization_id: Optional[str] = None

    result_files: Optional[List[KhulnaSoftFile]] = None

    status: Optional[str] = None

    training_files: Optional[List[KhulnaSoftFile]] = None

    updated_at: Optional[int] = None

    validation_files: Optional[List[KhulnaSoftFile]] = None
