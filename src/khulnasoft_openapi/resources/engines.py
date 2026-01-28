# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional

import httpx

from ..types import engine_search_params, engine_create_embedding_params, engine_create_completion_params
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
from ..types.engine import Engine
from ..types.engine_list_response import EngineListResponse
from ..types.engine_search_response import EngineSearchResponse
from ..types.engine_create_embedding_response import EngineCreateEmbeddingResponse
from ..types.engine_create_completion_response import EngineCreateCompletionResponse

__all__ = ["EnginesResource", "AsyncEnginesResource"]


class EnginesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnginesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/khulnasoft/khulnasoft-openapi#accessing-raw-response-data-eg-headers
        """
        return EnginesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnginesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/khulnasoft/khulnasoft-openapi#with_streaming_response
        """
        return EnginesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        engine_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Engine:
        """
        Retrieves an engine instance, providing basic information about the engine such
        as the owner and availability.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not engine_id:
            raise ValueError(f"Expected a non-empty value for `engine_id` but received {engine_id!r}")
        return self._get(
            f"/engines/{engine_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Engine,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngineListResponse:
        """
        Lists the currently available engines, and provides basic information about each
        one such as the owner and availability.
        """
        return self._get(
            "/engines",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngineListResponse,
        )

    def create_completion(
        self,
        engine_id: str,
        *,
        best_of: Optional[int] | Omit = omit,
        echo: Optional[bool] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        logit_bias: Optional[object] | Omit = omit,
        logprobs: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        prompt: Union[str, SequenceNotStr[str], Iterable[int], Iterable[Iterable[int]], None] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stream: Optional[bool] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngineCreateCompletionResponse:
        """
        Creates a new completion for the provided prompt and parameters

        Args:
          best_of: Generates `best_of` completions server-side and returns the "best" (the one with
              the lowest log probability per token). Results cannot be streamed.

              When used with `n`, `best_of` controls the number of candidate completions and
              `n` specifies how many to return – `best_of` must be greater than `n`.

              **Note:** Because this parameter generates many completions, it can quickly
              consume your token quota. Use carefully and ensure that you have reasonable
              settings for `max_tokens` and `stop`.

          echo: Echo back the prompt in addition to the completion

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

              [See more information about frequency and presence penalties.](/docs/api-reference/parameter-details)

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

          max_tokens: The maximum number of [tokens](/tokenizer) to generate in the completion.

              The token count of your prompt plus `max_tokens` cannot exceed the model's
              context length. Most models have a context length of 2048 tokens (except
              `davinci-codex`, which supports 4096).

          n: How many completions to generate for each prompt.

              **Note:** Because this parameter generates many completions, it can quickly
              consume your token quota. Use carefully and ensure that you have reasonable
              settings for `max_tokens` and `stop`.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

              [See more information about frequency and presence penalties.](/docs/api-reference/parameter-details)

          prompt: The prompt(s) to generate completions for, encoded as a string, array of
              strings, array of tokens, or array of token arrays.

              Note that <|endoftext|> is the document separator that the model sees during
              training, so if a prompt is not specified the model will generate as if from the
              beginning of a new document.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          stream: Whether to stream back partial progress. If set, tokens will be sent as
              data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          temperature: What
              [sampling temperature](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277)
              to use. Higher values means the model will take more risks. Try 0.9 for more
              creative applications, and 0 (argmax sampling) for ones with a well-defined
              answer.

              We generally recommend altering this or `top_p` but not both.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not engine_id:
            raise ValueError(f"Expected a non-empty value for `engine_id` but received {engine_id!r}")
        return self._post(
            f"/engines/{engine_id}/completions",
            body=maybe_transform(
                {
                    "best_of": best_of,
                    "echo": echo,
                    "frequency_penalty": frequency_penalty,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "n": n,
                    "presence_penalty": presence_penalty,
                    "prompt": prompt,
                    "stop": stop,
                    "stream": stream,
                    "temperature": temperature,
                    "top_p": top_p,
                },
                engine_create_completion_params.EngineCreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngineCreateCompletionResponse,
        )

    def create_embedding(
        self,
        engine_id: str,
        *,
        input: Union[str, SequenceNotStr[str], Iterable[int], Iterable[Iterable[int]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngineCreateEmbeddingResponse:
        """
        Creates an embedding vector representing the input text.

        Args:
          input: Input text to get embeddings for, encoded as a string or array of tokens. To get
              embeddings for multiple inputs in a single request, pass an array of strings or
              array of token arrays. Each input must not exceed 2048 tokens in length.

              We suggest replacing newlines (`\n`) in your input with a single space, as we
              have observed inferior results when newlines are present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not engine_id:
            raise ValueError(f"Expected a non-empty value for `engine_id` but received {engine_id!r}")
        return self._post(
            f"/engines/{engine_id}/embeddings",
            body=maybe_transform({"input": input}, engine_create_embedding_params.EngineCreateEmbeddingParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngineCreateEmbeddingResponse,
        )

    def search(
        self,
        engine_id: str,
        *,
        documents: Optional[SequenceNotStr[str]] | Omit = omit,
        file: Optional[str] | Omit = omit,
        max_rerank: Optional[int] | Omit = omit,
        query: str | Omit = omit,
        return_metadata: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngineSearchResponse:
        """
        The search endpoint computes similarity scores between provided query and
        documents. Documents can be passed directly to the API if there are no more than
        200 of them.

        To go beyond the 200 document limit, documents can be processed offline and then
        used for efficient retrieval at query time. When `file` is set, the search
        endpoint searches over all the documents in the given file and returns up to the
        `max_rerank` number of documents. These documents will be returned along with
        their search scores.

        The similarity score is a positive score that usually ranges from 0 to 300 (but
        can sometimes go higher), where a score above 200 usually means the document is
        semantically similar to the query.

        Args:
          documents: Up to 200 documents to search over, provided as a list of strings.

              The maximum document length (in tokens) is 2034 minus the number of tokens in
              the query.

              You should specify either `documents` or a `file`, but not both.

          file: The ID of an uploaded file that contains documents to search over.

              You should specify either `documents` or a `file`, but not both.

          max_rerank: The maximum number of documents to be re-ranked and returned by search.

              This flag only takes effect when `file` is set.

          query: Query to search against the documents.

          return_metadata: A special boolean flag for showing metadata. If set to `true`, each document
              entry in the returned JSON will contain a "metadata" field.

              This flag only takes effect when `file` is set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not engine_id:
            raise ValueError(f"Expected a non-empty value for `engine_id` but received {engine_id!r}")
        return self._post(
            f"/engines/{engine_id}/search",
            body=maybe_transform(
                {
                    "documents": documents,
                    "file": file,
                    "max_rerank": max_rerank,
                    "query": query,
                    "return_metadata": return_metadata,
                },
                engine_search_params.EngineSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngineSearchResponse,
        )


class AsyncEnginesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnginesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/khulnasoft/khulnasoft-openapi#accessing-raw-response-data-eg-headers
        """
        return AsyncEnginesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnginesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/khulnasoft/khulnasoft-openapi#with_streaming_response
        """
        return AsyncEnginesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        engine_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Engine:
        """
        Retrieves an engine instance, providing basic information about the engine such
        as the owner and availability.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not engine_id:
            raise ValueError(f"Expected a non-empty value for `engine_id` but received {engine_id!r}")
        return await self._get(
            f"/engines/{engine_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Engine,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngineListResponse:
        """
        Lists the currently available engines, and provides basic information about each
        one such as the owner and availability.
        """
        return await self._get(
            "/engines",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngineListResponse,
        )

    async def create_completion(
        self,
        engine_id: str,
        *,
        best_of: Optional[int] | Omit = omit,
        echo: Optional[bool] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        logit_bias: Optional[object] | Omit = omit,
        logprobs: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        prompt: Union[str, SequenceNotStr[str], Iterable[int], Iterable[Iterable[int]], None] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stream: Optional[bool] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngineCreateCompletionResponse:
        """
        Creates a new completion for the provided prompt and parameters

        Args:
          best_of: Generates `best_of` completions server-side and returns the "best" (the one with
              the lowest log probability per token). Results cannot be streamed.

              When used with `n`, `best_of` controls the number of candidate completions and
              `n` specifies how many to return – `best_of` must be greater than `n`.

              **Note:** Because this parameter generates many completions, it can quickly
              consume your token quota. Use carefully and ensure that you have reasonable
              settings for `max_tokens` and `stop`.

          echo: Echo back the prompt in addition to the completion

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

              [See more information about frequency and presence penalties.](/docs/api-reference/parameter-details)

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

          max_tokens: The maximum number of [tokens](/tokenizer) to generate in the completion.

              The token count of your prompt plus `max_tokens` cannot exceed the model's
              context length. Most models have a context length of 2048 tokens (except
              `davinci-codex`, which supports 4096).

          n: How many completions to generate for each prompt.

              **Note:** Because this parameter generates many completions, it can quickly
              consume your token quota. Use carefully and ensure that you have reasonable
              settings for `max_tokens` and `stop`.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

              [See more information about frequency and presence penalties.](/docs/api-reference/parameter-details)

          prompt: The prompt(s) to generate completions for, encoded as a string, array of
              strings, array of tokens, or array of token arrays.

              Note that <|endoftext|> is the document separator that the model sees during
              training, so if a prompt is not specified the model will generate as if from the
              beginning of a new document.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          stream: Whether to stream back partial progress. If set, tokens will be sent as
              data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          temperature: What
              [sampling temperature](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277)
              to use. Higher values means the model will take more risks. Try 0.9 for more
              creative applications, and 0 (argmax sampling) for ones with a well-defined
              answer.

              We generally recommend altering this or `top_p` but not both.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not engine_id:
            raise ValueError(f"Expected a non-empty value for `engine_id` but received {engine_id!r}")
        return await self._post(
            f"/engines/{engine_id}/completions",
            body=await async_maybe_transform(
                {
                    "best_of": best_of,
                    "echo": echo,
                    "frequency_penalty": frequency_penalty,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "n": n,
                    "presence_penalty": presence_penalty,
                    "prompt": prompt,
                    "stop": stop,
                    "stream": stream,
                    "temperature": temperature,
                    "top_p": top_p,
                },
                engine_create_completion_params.EngineCreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngineCreateCompletionResponse,
        )

    async def create_embedding(
        self,
        engine_id: str,
        *,
        input: Union[str, SequenceNotStr[str], Iterable[int], Iterable[Iterable[int]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngineCreateEmbeddingResponse:
        """
        Creates an embedding vector representing the input text.

        Args:
          input: Input text to get embeddings for, encoded as a string or array of tokens. To get
              embeddings for multiple inputs in a single request, pass an array of strings or
              array of token arrays. Each input must not exceed 2048 tokens in length.

              We suggest replacing newlines (`\n`) in your input with a single space, as we
              have observed inferior results when newlines are present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not engine_id:
            raise ValueError(f"Expected a non-empty value for `engine_id` but received {engine_id!r}")
        return await self._post(
            f"/engines/{engine_id}/embeddings",
            body=await async_maybe_transform(
                {"input": input}, engine_create_embedding_params.EngineCreateEmbeddingParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngineCreateEmbeddingResponse,
        )

    async def search(
        self,
        engine_id: str,
        *,
        documents: Optional[SequenceNotStr[str]] | Omit = omit,
        file: Optional[str] | Omit = omit,
        max_rerank: Optional[int] | Omit = omit,
        query: str | Omit = omit,
        return_metadata: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngineSearchResponse:
        """
        The search endpoint computes similarity scores between provided query and
        documents. Documents can be passed directly to the API if there are no more than
        200 of them.

        To go beyond the 200 document limit, documents can be processed offline and then
        used for efficient retrieval at query time. When `file` is set, the search
        endpoint searches over all the documents in the given file and returns up to the
        `max_rerank` number of documents. These documents will be returned along with
        their search scores.

        The similarity score is a positive score that usually ranges from 0 to 300 (but
        can sometimes go higher), where a score above 200 usually means the document is
        semantically similar to the query.

        Args:
          documents: Up to 200 documents to search over, provided as a list of strings.

              The maximum document length (in tokens) is 2034 minus the number of tokens in
              the query.

              You should specify either `documents` or a `file`, but not both.

          file: The ID of an uploaded file that contains documents to search over.

              You should specify either `documents` or a `file`, but not both.

          max_rerank: The maximum number of documents to be re-ranked and returned by search.

              This flag only takes effect when `file` is set.

          query: Query to search against the documents.

          return_metadata: A special boolean flag for showing metadata. If set to `true`, each document
              entry in the returned JSON will contain a "metadata" field.

              This flag only takes effect when `file` is set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not engine_id:
            raise ValueError(f"Expected a non-empty value for `engine_id` but received {engine_id!r}")
        return await self._post(
            f"/engines/{engine_id}/search",
            body=await async_maybe_transform(
                {
                    "documents": documents,
                    "file": file,
                    "max_rerank": max_rerank,
                    "query": query,
                    "return_metadata": return_metadata,
                },
                engine_search_params.EngineSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngineSearchResponse,
        )


class EnginesResourceWithRawResponse:
    def __init__(self, engines: EnginesResource) -> None:
        self._engines = engines

        self.retrieve = to_raw_response_wrapper(
            engines.retrieve,
        )
        self.list = to_raw_response_wrapper(
            engines.list,
        )
        self.create_completion = to_raw_response_wrapper(
            engines.create_completion,
        )
        self.create_embedding = to_raw_response_wrapper(
            engines.create_embedding,
        )
        self.search = to_raw_response_wrapper(
            engines.search,
        )


class AsyncEnginesResourceWithRawResponse:
    def __init__(self, engines: AsyncEnginesResource) -> None:
        self._engines = engines

        self.retrieve = async_to_raw_response_wrapper(
            engines.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            engines.list,
        )
        self.create_completion = async_to_raw_response_wrapper(
            engines.create_completion,
        )
        self.create_embedding = async_to_raw_response_wrapper(
            engines.create_embedding,
        )
        self.search = async_to_raw_response_wrapper(
            engines.search,
        )


class EnginesResourceWithStreamingResponse:
    def __init__(self, engines: EnginesResource) -> None:
        self._engines = engines

        self.retrieve = to_streamed_response_wrapper(
            engines.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            engines.list,
        )
        self.create_completion = to_streamed_response_wrapper(
            engines.create_completion,
        )
        self.create_embedding = to_streamed_response_wrapper(
            engines.create_embedding,
        )
        self.search = to_streamed_response_wrapper(
            engines.search,
        )


class AsyncEnginesResourceWithStreamingResponse:
    def __init__(self, engines: AsyncEnginesResource) -> None:
        self._engines = engines

        self.retrieve = async_to_streamed_response_wrapper(
            engines.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            engines.list,
        )
        self.create_completion = async_to_streamed_response_wrapper(
            engines.create_completion,
        )
        self.create_embedding = async_to_streamed_response_wrapper(
            engines.create_embedding,
        )
        self.search = async_to_streamed_response_wrapper(
            engines.search,
        )
