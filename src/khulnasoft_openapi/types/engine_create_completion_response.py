# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EngineCreateCompletionResponse", "Choice", "ChoiceLogprobs"]


class ChoiceLogprobs(BaseModel):
    text_offset: Optional[List[int]] = None

    token_logprobs: Optional[List[float]] = None

    tokens: Optional[List[str]] = None

    top_logprobs: Optional[List[object]] = None


class Choice(BaseModel):
    finish_reason: Optional[str] = None

    index: Optional[int] = None

    logprobs: Optional[ChoiceLogprobs] = None

    text: Optional[str] = None


class EngineCreateCompletionResponse(BaseModel):
    id: Optional[str] = None

    choices: Optional[List[Choice]] = None

    created: Optional[int] = None

    model: Optional[str] = None

    object: Optional[str] = None
