# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .khulna_soft_file import KhulnaSoftFile

__all__ = ["FileListResponse"]


class FileListResponse(BaseModel):
    data: Optional[List[KhulnaSoftFile]] = None

    object: Optional[str] = None
