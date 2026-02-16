from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `khulnasoft_openapi.resources` module.

    This is used so that we can lazily import `khulnasoft_openapi.resources` only when
    needed *and* so that users can just import `khulnasoft_openapi` and reference `khulnasoft_openapi.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("khulnasoft_openapi.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
