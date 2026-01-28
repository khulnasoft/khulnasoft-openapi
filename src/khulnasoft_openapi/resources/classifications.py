# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import classification_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.classification_create_response import ClassificationCreateResponse

__all__ = ["ClassificationsResource", "AsyncClassificationsResource"]


class ClassificationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClassificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/khulnasoft-openapi-python#accessing-raw-response-data-eg-headers
        """
        return ClassificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/khulnasoft-openapi-python#with_streaming_response
        """
        return ClassificationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        examples: Optional[Iterable[SequenceNotStr[str]]] | Omit = omit,
        expand: Optional[Iterable[object]] | Omit = omit,
        file: Optional[str] | Omit = omit,
        labels: Optional[SequenceNotStr[str]] | Omit = omit,
        logit_bias: Optional[object] | Omit = omit,
        logprobs: Optional[int] | Omit = omit,
        max_examples: Optional[int] | Omit = omit,
        model: str | Omit = omit,
        query: str | Omit = omit,
        return_metadata: Optional[bool] | Omit = omit,
        return_prompt: Optional[bool] | Omit = omit,
        search_model: Optional[str] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassificationCreateResponse:
        """
        Classifies the specified `query` using provided examples.

        The endpoint first [searches](/docs/api-reference/searches) over the labeled
        examples to select the ones most relevant for the particular query. Then, the
        relevant examples are combined with the query to construct a prompt to produce
        the final label via the [completions](/docs/api-reference/completions) endpoint.

        Labeled examples can be provided via an uploaded `file`, or explicitly listed in
        the request using the `examples` parameter for quick tests and small scale use
        cases.

        Args:
          examples:
              A list of examples with labels, in the following format:

              `[["The movie is so interesting.", "Positive"], ["It is quite boring.", "Negative"], ...]`

              All the label strings will be normalized to be capitalized.

              You should specify either `examples` or `file`, but not both.

          expand: If an object name is in the list, we provide the full information of the object;
              otherwise, we only provide the object ID. Currently we support `completion` and
              `file` objects for expansion.

          file: The ID of the uploaded file that contains training examples. See
              [upload file](/docs/api-reference/files/upload) for how to upload a file of the
              desired format and purpose.

              You should specify either `examples` or `file`, but not both.

          labels: The set of categories being classified. If not specified, candidate labels will
              be automatically collected from the examples you provide. All the label strings
              will be normalized to be capitalized.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a json object that maps tokens (specified by their token ID in the GPT
              tokenizer) to an associated bias value from -100 to 100. You can use this
              [tokenizer tool](/tokenizer?view=bpe) (which works for both GPT-2 and GPT-3) to
              convert text to token IDs. Mathematically, the bias is added to the logits
              generated by the model prior to sampling. The exact effect will vary per model,
              but values between -1 and 1 should decrease or increase likelihood of selection;
              values like -100 or 100 should result in a ban or exclusive selection of the
              relevant token.

              As an example, you can pass `{"50256": -100}` to prevent the <|endoftext|> token
              from being generated.

          logprobs: Include the log probabilities on the `logprobs` most likely tokens, as well the
              chosen tokens. For example, if `logprobs` is 5, the API will return a list of
              the 5 most likely tokens. The API will always return the `logprob` of the
              sampled token, so there may be up to `logprobs+1` elements in the response.

              The maximum value for `logprobs` is 5. If you need more than this, please
              contact support@khulnasoft.com and describe your use case.

              When `logprobs` is set, `completion` will be automatically added into `expand`
              to get the logprobs.

          max_examples: The maximum number of examples to be ranked by
              [Search](/docs/api-reference/searches/create) when using `file`. Setting it to a
              higher value leads to improved accuracy but with increased latency and cost.

          model: ID of the engine to use for completion.

          query: Query to be classified.

          return_metadata: A special boolean flag for showing metadata. If set to `true`, each document
              entry in the returned JSON will contain a "metadata" field.

              This flag only takes effect when `file` is set.

          return_prompt: If set to `true`, the returned JSON will include a "prompt" field containing the
              final prompt that was used to request a completion. This is mainly useful for
              debugging purposes.

          search_model: ID of the engine to use for [Search](/docs/api-reference/searches/create).

          temperature: What sampling `temperature` to use. Higher values mean the model will take more
              risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones
              with a well-defined answer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/classifications",
            body=maybe_transform(
                {
                    "examples": examples,
                    "expand": expand,
                    "file": file,
                    "labels": labels,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_examples": max_examples,
                    "model": model,
                    "query": query,
                    "return_metadata": return_metadata,
                    "return_prompt": return_prompt,
                    "search_model": search_model,
                    "temperature": temperature,
                },
                classification_create_params.ClassificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassificationCreateResponse,
        )


class AsyncClassificationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClassificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/khulnasoft-openapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClassificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/khulnasoft-openapi-python#with_streaming_response
        """
        return AsyncClassificationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        examples: Optional[Iterable[SequenceNotStr[str]]] | Omit = omit,
        expand: Optional[Iterable[object]] | Omit = omit,
        file: Optional[str] | Omit = omit,
        labels: Optional[SequenceNotStr[str]] | Omit = omit,
        logit_bias: Optional[object] | Omit = omit,
        logprobs: Optional[int] | Omit = omit,
        max_examples: Optional[int] | Omit = omit,
        model: str | Omit = omit,
        query: str | Omit = omit,
        return_metadata: Optional[bool] | Omit = omit,
        return_prompt: Optional[bool] | Omit = omit,
        search_model: Optional[str] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassificationCreateResponse:
        """
        Classifies the specified `query` using provided examples.

        The endpoint first [searches](/docs/api-reference/searches) over the labeled
        examples to select the ones most relevant for the particular query. Then, the
        relevant examples are combined with the query to construct a prompt to produce
        the final label via the [completions](/docs/api-reference/completions) endpoint.

        Labeled examples can be provided via an uploaded `file`, or explicitly listed in
        the request using the `examples` parameter for quick tests and small scale use
        cases.

        Args:
          examples:
              A list of examples with labels, in the following format:

              `[["The movie is so interesting.", "Positive"], ["It is quite boring.", "Negative"], ...]`

              All the label strings will be normalized to be capitalized.

              You should specify either `examples` or `file`, but not both.

          expand: If an object name is in the list, we provide the full information of the object;
              otherwise, we only provide the object ID. Currently we support `completion` and
              `file` objects for expansion.

          file: The ID of the uploaded file that contains training examples. See
              [upload file](/docs/api-reference/files/upload) for how to upload a file of the
              desired format and purpose.

              You should specify either `examples` or `file`, but not both.

          labels: The set of categories being classified. If not specified, candidate labels will
              be automatically collected from the examples you provide. All the label strings
              will be normalized to be capitalized.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a json object that maps tokens (specified by their token ID in the GPT
              tokenizer) to an associated bias value from -100 to 100. You can use this
              [tokenizer tool](/tokenizer?view=bpe) (which works for both GPT-2 and GPT-3) to
              convert text to token IDs. Mathematically, the bias is added to the logits
              generated by the model prior to sampling. The exact effect will vary per model,
              but values between -1 and 1 should decrease or increase likelihood of selection;
              values like -100 or 100 should result in a ban or exclusive selection of the
              relevant token.

              As an example, you can pass `{"50256": -100}` to prevent the <|endoftext|> token
              from being generated.

          logprobs: Include the log probabilities on the `logprobs` most likely tokens, as well the
              chosen tokens. For example, if `logprobs` is 5, the API will return a list of
              the 5 most likely tokens. The API will always return the `logprob` of the
              sampled token, so there may be up to `logprobs+1` elements in the response.

              The maximum value for `logprobs` is 5. If you need more than this, please
              contact support@khulnasoft.com and describe your use case.

              When `logprobs` is set, `completion` will be automatically added into `expand`
              to get the logprobs.

          max_examples: The maximum number of examples to be ranked by
              [Search](/docs/api-reference/searches/create) when using `file`. Setting it to a
              higher value leads to improved accuracy but with increased latency and cost.

          model: ID of the engine to use for completion.

          query: Query to be classified.

          return_metadata: A special boolean flag for showing metadata. If set to `true`, each document
              entry in the returned JSON will contain a "metadata" field.

              This flag only takes effect when `file` is set.

          return_prompt: If set to `true`, the returned JSON will include a "prompt" field containing the
              final prompt that was used to request a completion. This is mainly useful for
              debugging purposes.

          search_model: ID of the engine to use for [Search](/docs/api-reference/searches/create).

          temperature: What sampling `temperature` to use. Higher values mean the model will take more
              risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones
              with a well-defined answer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/classifications",
            body=await async_maybe_transform(
                {
                    "examples": examples,
                    "expand": expand,
                    "file": file,
                    "labels": labels,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_examples": max_examples,
                    "model": model,
                    "query": query,
                    "return_metadata": return_metadata,
                    "return_prompt": return_prompt,
                    "search_model": search_model,
                    "temperature": temperature,
                },
                classification_create_params.ClassificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassificationCreateResponse,
        )


class ClassificationsResourceWithRawResponse:
    def __init__(self, classifications: ClassificationsResource) -> None:
        self._classifications = classifications

        self.create = to_raw_response_wrapper(
            classifications.create,
        )


class AsyncClassificationsResourceWithRawResponse:
    def __init__(self, classifications: AsyncClassificationsResource) -> None:
        self._classifications = classifications

        self.create = async_to_raw_response_wrapper(
            classifications.create,
        )


class ClassificationsResourceWithStreamingResponse:
    def __init__(self, classifications: ClassificationsResource) -> None:
        self._classifications = classifications

        self.create = to_streamed_response_wrapper(
            classifications.create,
        )


class AsyncClassificationsResourceWithStreamingResponse:
    def __init__(self, classifications: AsyncClassificationsResource) -> None:
        self._classifications = classifications

        self.create = async_to_streamed_response_wrapper(
            classifications.create,
        )
