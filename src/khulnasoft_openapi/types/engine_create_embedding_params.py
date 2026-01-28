# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["EngineCreateEmbeddingParams"]


class EngineCreateEmbeddingParams(TypedDict, total=False):
    input: Union[str, SequenceNotStr[str], Iterable[int], Iterable[Iterable[int]]]
    """Input text to get embeddings for, encoded as a string or array of tokens.

    To get embeddings for multiple inputs in a single request, pass an array of
    strings or array of token arrays. Each input must not exceed 2048 tokens in
    length.

    We suggest replacing newlines (`\n`) in your input with a single space, as we
    have observed inferior results when newlines are present.
    """
