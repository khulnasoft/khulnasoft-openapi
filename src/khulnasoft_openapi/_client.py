# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import files, answers, engines, fine_tunes, classifications
    from .resources.files import FilesResource, AsyncFilesResource
    from .resources.answers import AnswersResource, AsyncAnswersResource
    from .resources.engines import EnginesResource, AsyncEnginesResource
    from .resources.fine_tunes import FineTunesResource, AsyncFineTunesResource
    from .resources.classifications import ClassificationsResource, AsyncClassificationsResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "KhulnasoftOpenAPI",
    "AsyncKhulnasoftOpenAPI",
    "Client",
    "AsyncClient",
]


class KhulnasoftOpenAPI(SyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous KhulnasoftOpenAPI client instance.

        This automatically infers the `api_key` argument from the `KHULNASOFT_OPENAPI_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("KHULNASOFT_OPENAPI_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("KHULNASOFT_OPENAPI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.khulnasoft.com/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def engines(self) -> EnginesResource:
        from .resources.engines import EnginesResource

        return EnginesResource(self)

    @cached_property
    def files(self) -> FilesResource:
        from .resources.files import FilesResource

        return FilesResource(self)

    @cached_property
    def answers(self) -> AnswersResource:
        from .resources.answers import AnswersResource

        return AnswersResource(self)

    @cached_property
    def classifications(self) -> ClassificationsResource:
        from .resources.classifications import ClassificationsResource

        return ClassificationsResource(self)

    @cached_property
    def fine_tunes(self) -> FineTunesResource:
        from .resources.fine_tunes import FineTunesResource

        return FineTunesResource(self)

    @cached_property
    def with_raw_response(self) -> KhulnasoftOpenAPIWithRawResponse:
        return KhulnasoftOpenAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KhulnasoftOpenAPIWithStreamedResponse:
        return KhulnasoftOpenAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncKhulnasoftOpenAPI(AsyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncKhulnasoftOpenAPI client instance.

        This automatically infers the `api_key` argument from the `KHULNASOFT_OPENAPI_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("KHULNASOFT_OPENAPI_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("KHULNASOFT_OPENAPI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.khulnasoft.com/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def engines(self) -> AsyncEnginesResource:
        from .resources.engines import AsyncEnginesResource

        return AsyncEnginesResource(self)

    @cached_property
    def files(self) -> AsyncFilesResource:
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

    @cached_property
    def answers(self) -> AsyncAnswersResource:
        from .resources.answers import AsyncAnswersResource

        return AsyncAnswersResource(self)

    @cached_property
    def classifications(self) -> AsyncClassificationsResource:
        from .resources.classifications import AsyncClassificationsResource

        return AsyncClassificationsResource(self)

    @cached_property
    def fine_tunes(self) -> AsyncFineTunesResource:
        from .resources.fine_tunes import AsyncFineTunesResource

        return AsyncFineTunesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncKhulnasoftOpenAPIWithRawResponse:
        return AsyncKhulnasoftOpenAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKhulnasoftOpenAPIWithStreamedResponse:
        return AsyncKhulnasoftOpenAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class KhulnasoftOpenAPIWithRawResponse:
    _client: KhulnasoftOpenAPI

    def __init__(self, client: KhulnasoftOpenAPI) -> None:
        self._client = client

    @cached_property
    def engines(self) -> engines.EnginesResourceWithRawResponse:
        from .resources.engines import EnginesResourceWithRawResponse

        return EnginesResourceWithRawResponse(self._client.engines)

    @cached_property
    def files(self) -> files.FilesResourceWithRawResponse:
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)

    @cached_property
    def answers(self) -> answers.AnswersResourceWithRawResponse:
        from .resources.answers import AnswersResourceWithRawResponse

        return AnswersResourceWithRawResponse(self._client.answers)

    @cached_property
    def classifications(self) -> classifications.ClassificationsResourceWithRawResponse:
        from .resources.classifications import ClassificationsResourceWithRawResponse

        return ClassificationsResourceWithRawResponse(self._client.classifications)

    @cached_property
    def fine_tunes(self) -> fine_tunes.FineTunesResourceWithRawResponse:
        from .resources.fine_tunes import FineTunesResourceWithRawResponse

        return FineTunesResourceWithRawResponse(self._client.fine_tunes)


class AsyncKhulnasoftOpenAPIWithRawResponse:
    _client: AsyncKhulnasoftOpenAPI

    def __init__(self, client: AsyncKhulnasoftOpenAPI) -> None:
        self._client = client

    @cached_property
    def engines(self) -> engines.AsyncEnginesResourceWithRawResponse:
        from .resources.engines import AsyncEnginesResourceWithRawResponse

        return AsyncEnginesResourceWithRawResponse(self._client.engines)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithRawResponse:
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)

    @cached_property
    def answers(self) -> answers.AsyncAnswersResourceWithRawResponse:
        from .resources.answers import AsyncAnswersResourceWithRawResponse

        return AsyncAnswersResourceWithRawResponse(self._client.answers)

    @cached_property
    def classifications(self) -> classifications.AsyncClassificationsResourceWithRawResponse:
        from .resources.classifications import AsyncClassificationsResourceWithRawResponse

        return AsyncClassificationsResourceWithRawResponse(self._client.classifications)

    @cached_property
    def fine_tunes(self) -> fine_tunes.AsyncFineTunesResourceWithRawResponse:
        from .resources.fine_tunes import AsyncFineTunesResourceWithRawResponse

        return AsyncFineTunesResourceWithRawResponse(self._client.fine_tunes)


class KhulnasoftOpenAPIWithStreamedResponse:
    _client: KhulnasoftOpenAPI

    def __init__(self, client: KhulnasoftOpenAPI) -> None:
        self._client = client

    @cached_property
    def engines(self) -> engines.EnginesResourceWithStreamingResponse:
        from .resources.engines import EnginesResourceWithStreamingResponse

        return EnginesResourceWithStreamingResponse(self._client.engines)

    @cached_property
    def files(self) -> files.FilesResourceWithStreamingResponse:
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def answers(self) -> answers.AnswersResourceWithStreamingResponse:
        from .resources.answers import AnswersResourceWithStreamingResponse

        return AnswersResourceWithStreamingResponse(self._client.answers)

    @cached_property
    def classifications(self) -> classifications.ClassificationsResourceWithStreamingResponse:
        from .resources.classifications import ClassificationsResourceWithStreamingResponse

        return ClassificationsResourceWithStreamingResponse(self._client.classifications)

    @cached_property
    def fine_tunes(self) -> fine_tunes.FineTunesResourceWithStreamingResponse:
        from .resources.fine_tunes import FineTunesResourceWithStreamingResponse

        return FineTunesResourceWithStreamingResponse(self._client.fine_tunes)


class AsyncKhulnasoftOpenAPIWithStreamedResponse:
    _client: AsyncKhulnasoftOpenAPI

    def __init__(self, client: AsyncKhulnasoftOpenAPI) -> None:
        self._client = client

    @cached_property
    def engines(self) -> engines.AsyncEnginesResourceWithStreamingResponse:
        from .resources.engines import AsyncEnginesResourceWithStreamingResponse

        return AsyncEnginesResourceWithStreamingResponse(self._client.engines)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithStreamingResponse:
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def answers(self) -> answers.AsyncAnswersResourceWithStreamingResponse:
        from .resources.answers import AsyncAnswersResourceWithStreamingResponse

        return AsyncAnswersResourceWithStreamingResponse(self._client.answers)

    @cached_property
    def classifications(self) -> classifications.AsyncClassificationsResourceWithStreamingResponse:
        from .resources.classifications import AsyncClassificationsResourceWithStreamingResponse

        return AsyncClassificationsResourceWithStreamingResponse(self._client.classifications)

    @cached_property
    def fine_tunes(self) -> fine_tunes.AsyncFineTunesResourceWithStreamingResponse:
        from .resources.fine_tunes import AsyncFineTunesResourceWithStreamingResponse

        return AsyncFineTunesResourceWithStreamingResponse(self._client.fine_tunes)


Client = KhulnasoftOpenAPI

AsyncClient = AsyncKhulnasoftOpenAPI
