# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ClassificationCreateResponse", "SelectedExample"]


class SelectedExample(BaseModel):
    document: Optional[int] = None

    label: Optional[str] = None

    text: Optional[str] = None


class ClassificationCreateResponse(BaseModel):
    completion: Optional[str] = None

    label: Optional[str] = None

    model: Optional[str] = None

    object: Optional[str] = None

    search_model: Optional[str] = None

    selected_examples: Optional[List[SelectedExample]] = None
