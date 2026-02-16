# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["FileUploadParams"]


class FileUploadParams(TypedDict, total=False):
    file: Required[FileTypes]
    """
    Name of the [JSON Lines](https://jsonlines.readthedocs.io/en/latest/) file to be
    uploaded.

    If the `purpose` is set to "search" or "answers", each line is a JSON record
    with a "text" field and an optional "metadata" field. Only "text" field will be
    used for search. Specially, when the `purpose` is "answers", "\n" is used as a
    delimiter to chunk contents in the "text" field into multiple documents for
    finer-grained matching.

    If the `purpose` is set to "classifications", each line is a JSON record
    representing a single training example with "text" and "label" fields along with
    an optional "metadata" field.

    If the `purpose` is set to "fine-tune", each line is a JSON record with "prompt"
    and "completion" fields representing your
    [training examples](/docs/guides/fine-tuning/prepare-training-data).
    """

    purpose: Required[str]
    """The intended purpose of the uploaded documents.

    Use "search" for [Search](/docs/api-reference/searches), "answers" for
    [Answers](/docs/api-reference/answers), "classifications" for
    [Classifications](/docs/api-reference/classifications) and "fine-tune" for
    [Fine-tuning](/docs/api-reference/fine-tunes). This allows us to validate the
    format of the uploaded file.
    """
