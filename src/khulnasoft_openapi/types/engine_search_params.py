# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["EngineSearchParams"]


class EngineSearchParams(TypedDict, total=False):
    documents: Optional[SequenceNotStr[str]]
    """Up to 200 documents to search over, provided as a list of strings.

    The maximum document length (in tokens) is 2034 minus the number of tokens in
    the query.

    You should specify either `documents` or a `file`, but not both.
    """

    file: Optional[str]
    """The ID of an uploaded file that contains documents to search over.

    You should specify either `documents` or a `file`, but not both.
    """

    max_rerank: Optional[int]
    """The maximum number of documents to be re-ranked and returned by search.

    This flag only takes effect when `file` is set.
    """

    query: str
    """Query to search against the documents."""

    return_metadata: Optional[bool]
    """A special boolean flag for showing metadata.

    If set to `true`, each document entry in the returned JSON will contain a
    "metadata" field.

    This flag only takes effect when `file` is set.
    """
