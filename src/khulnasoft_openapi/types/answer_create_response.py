# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AnswerCreateResponse", "SelectedDocument"]


class SelectedDocument(BaseModel):
    document: Optional[int] = None

    text: Optional[str] = None


class AnswerCreateResponse(BaseModel):
    answers: Optional[List[str]] = None

    completion: Optional[str] = None

    model: Optional[str] = None

    object: Optional[str] = None

    search_model: Optional[str] = None

    selected_documents: Optional[List[SelectedDocument]] = None
