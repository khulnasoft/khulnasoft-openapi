# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Optional

from .._models import BaseModel

__all__ = ["KhulnaSoftFile"]


class KhulnaSoftFile(BaseModel):
    id: Optional[str] = None

    bytes: Optional[int] = None

    created_at: Optional[int] = None

    filename: Optional[str] = None

    object: Optional[str] = None

    purpose: Optional[str] = None

    status: Optional[str] = None

    status_details: Optional[builtins.object] = None
