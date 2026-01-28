# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional

import httpx

from ..types import answer_create_params
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
from ..types.answer_create_response import AnswerCreateResponse

__all__ = ["AnswersResource", "AsyncAnswersResource"]


class AnswersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnswersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/khulnasoft-openapi-python#accessing-raw-response-data-eg-headers
        """
        return AnswersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnswersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/khulnasoft-openapi-python#with_streaming_response
        """
        return AnswersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        documents: Optional[SequenceNotStr[str]] | Omit = omit,
        examples: Iterable[SequenceNotStr[str]] | Omit = omit,
        examples_context: str | Omit = omit,
        expand: Optional[Iterable[object]] | Omit = omit,
        file: Optional[str] | Omit = omit,
        logit_bias: Optional[object] | Omit = omit,
        logprobs: Optional[int] | Omit = omit,
        max_rerank: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        model: str | Omit = omit,
        n: Optional[int] | Omit = omit,
        question: str | Omit = omit,
        return_metadata: Optional[bool] | Omit = omit,
        return_prompt: Optional[bool] | Omit = omit,
        search_model: Optional[str] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnswerCreateResponse:
        """
        Answers the specified question using the provided documents and examples.

        The endpoint first [searches](/docs/api-reference/searches) over provided
        documents or files to find relevant context. The relevant context is combined
        with the provided examples and question to create the prompt for
        [completion](/docs/api-reference/completions).

        Args:
          documents: List of documents from which the answer for the input `question` should be
              derived. If this is an empty list, the question will be answered based on the
              question-answer examples.

              You should specify either `documents` or a `file`, but not both.

          examples: List of (question, answer) pairs that will help steer the model towards the tone
              and answer format you'd like. We recommend adding 2 to 3 examples.

          examples_context: A text snippet containing the contextual information used to generate the
              answers for the `examples` you provide.

          expand: If an object name is in the list, we provide the full information of the object;
              otherwise, we only provide the object ID. Currently we support `completion` and
              `file` objects for expansion.

          file: The ID of an uploaded file that contains documents to search over. See
              [upload file](/docs/api-reference/files/upload) for how to upload a file of the
              desired format and purpose.

              You should specify either `documents` or a `file`, but not both.

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

          max_rerank: The maximum number of documents to be ranked by
              [Search](/docs/api-reference/searches/create) when using `file`. Setting it to a
              higher value leads to improved accuracy but with increased latency and cost.

          max_tokens: The maximum number of tokens allowed for the generated answer

          model: ID of the engine to use for completion.

          n: How many answers to generate for each question.

          question: Question to get answered.

          return_metadata: A special boolean flag for showing metadata. If set to `true`, each document
              entry in the returned JSON will contain a "metadata" field.

              This flag only takes effect when `file` is set.

          return_prompt: If set to `true`, the returned JSON will include a "prompt" field containing the
              final prompt that was used to request a completion. This is mainly useful for
              debugging purposes.

          search_model: ID of the engine to use for [Search](/docs/api-reference/searches/create).

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          temperature: What
              [sampling temperature](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277)
              to use. Higher values mean the model will take more risks and value 0 (argmax
              sampling) works better for scenarios with a well-defined answer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/answers",
            body=maybe_transform(
                {
                    "documents": documents,
                    "examples": examples,
                    "examples_context": examples_context,
                    "expand": expand,
                    "file": file,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_rerank": max_rerank,
                    "max_tokens": max_tokens,
                    "model": model,
                    "n": n,
                    "question": question,
                    "return_metadata": return_metadata,
                    "return_prompt": return_prompt,
                    "search_model": search_model,
                    "stop": stop,
                    "temperature": temperature,
                },
                answer_create_params.AnswerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnswerCreateResponse,
        )


class AsyncAnswersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnswersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/khulnasoft-openapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnswersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnswersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/khulnasoft-openapi-python#with_streaming_response
        """
        return AsyncAnswersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        documents: Optional[SequenceNotStr[str]] | Omit = omit,
        examples: Iterable[SequenceNotStr[str]] | Omit = omit,
        examples_context: str | Omit = omit,
        expand: Optional[Iterable[object]] | Omit = omit,
        file: Optional[str] | Omit = omit,
        logit_bias: Optional[object] | Omit = omit,
        logprobs: Optional[int] | Omit = omit,
        max_rerank: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        model: str | Omit = omit,
        n: Optional[int] | Omit = omit,
        question: str | Omit = omit,
        return_metadata: Optional[bool] | Omit = omit,
        return_prompt: Optional[bool] | Omit = omit,
        search_model: Optional[str] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnswerCreateResponse:
        """
        Answers the specified question using the provided documents and examples.

        The endpoint first [searches](/docs/api-reference/searches) over provided
        documents or files to find relevant context. The relevant context is combined
        with the provided examples and question to create the prompt for
        [completion](/docs/api-reference/completions).

        Args:
          documents: List of documents from which the answer for the input `question` should be
              derived. If this is an empty list, the question will be answered based on the
              question-answer examples.

              You should specify either `documents` or a `file`, but not both.

          examples: List of (question, answer) pairs that will help steer the model towards the tone
              and answer format you'd like. We recommend adding 2 to 3 examples.

          examples_context: A text snippet containing the contextual information used to generate the
              answers for the `examples` you provide.

          expand: If an object name is in the list, we provide the full information of the object;
              otherwise, we only provide the object ID. Currently we support `completion` and
              `file` objects for expansion.

          file: The ID of an uploaded file that contains documents to search over. See
              [upload file](/docs/api-reference/files/upload) for how to upload a file of the
              desired format and purpose.

              You should specify either `documents` or a `file`, but not both.

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

          max_rerank: The maximum number of documents to be ranked by
              [Search](/docs/api-reference/searches/create) when using `file`. Setting it to a
              higher value leads to improved accuracy but with increased latency and cost.

          max_tokens: The maximum number of tokens allowed for the generated answer

          model: ID of the engine to use for completion.

          n: How many answers to generate for each question.

          question: Question to get answered.

          return_metadata: A special boolean flag for showing metadata. If set to `true`, each document
              entry in the returned JSON will contain a "metadata" field.

              This flag only takes effect when `file` is set.

          return_prompt: If set to `true`, the returned JSON will include a "prompt" field containing the
              final prompt that was used to request a completion. This is mainly useful for
              debugging purposes.

          search_model: ID of the engine to use for [Search](/docs/api-reference/searches/create).

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          temperature: What
              [sampling temperature](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277)
              to use. Higher values mean the model will take more risks and value 0 (argmax
              sampling) works better for scenarios with a well-defined answer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/answers",
            body=await async_maybe_transform(
                {
                    "documents": documents,
                    "examples": examples,
                    "examples_context": examples_context,
                    "expand": expand,
                    "file": file,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_rerank": max_rerank,
                    "max_tokens": max_tokens,
                    "model": model,
                    "n": n,
                    "question": question,
                    "return_metadata": return_metadata,
                    "return_prompt": return_prompt,
                    "search_model": search_model,
                    "stop": stop,
                    "temperature": temperature,
                },
                answer_create_params.AnswerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnswerCreateResponse,
        )


class AnswersResourceWithRawResponse:
    def __init__(self, answers: AnswersResource) -> None:
        self._answers = answers

        self.create = to_raw_response_wrapper(
            answers.create,
        )


class AsyncAnswersResourceWithRawResponse:
    def __init__(self, answers: AsyncAnswersResource) -> None:
        self._answers = answers

        self.create = async_to_raw_response_wrapper(
            answers.create,
        )


class AnswersResourceWithStreamingResponse:
    def __init__(self, answers: AnswersResource) -> None:
        self._answers = answers

        self.create = to_streamed_response_wrapper(
            answers.create,
        )


class AsyncAnswersResourceWithStreamingResponse:
    def __init__(self, answers: AsyncAnswersResource) -> None:
        self._answers = answers

        self.create = async_to_streamed_response_wrapper(
            answers.create,
        )
