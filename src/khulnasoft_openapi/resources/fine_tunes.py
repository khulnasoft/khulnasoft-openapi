# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import fine_tune_create_params, fine_tune_get_events_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.fine_tune import FineTune
from ..types.fine_tune_list_response import FineTuneListResponse
from ..types.fine_tune_get_events_response import FineTuneGetEventsResponse

__all__ = ["FineTunesResource", "AsyncFineTunesResource"]


class FineTunesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FineTunesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/khulnasoft-openapi-python#accessing-raw-response-data-eg-headers
        """
        return FineTunesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FineTunesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/khulnasoft-openapi-python#with_streaming_response
        """
        return FineTunesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        batch_size: Optional[int] | Omit = omit,
        classification_betas: Optional[Iterable[float]] | Omit = omit,
        classification_n_classes: Optional[int] | Omit = omit,
        classification_positive_class: Optional[str] | Omit = omit,
        compute_classification_metrics: Optional[bool] | Omit = omit,
        learning_rate_multiplier: Optional[float] | Omit = omit,
        model: Optional[str] | Omit = omit,
        n_epochs: Optional[int] | Omit = omit,
        prompt_loss_weight: Optional[float] | Omit = omit,
        training_file: str | Omit = omit,
        validation_file: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FineTune:
        """
        Creates a job that fine-tunes a specified model from a given dataset.

        Response includes details of the enqueued job including job status and the name
        of the fine-tuned models once complete.

        [Learn more about Fine-tuning](/docs/guides/fine-tuning)

        Args:
          batch_size: The batch size to use for training. The batch size is the number of training
              examples used to train a single forward and backward pass.

              By default, the batch size will be dynamically configured to be ~0.2% of the
              number of examples in the training set, capped at 256 - in general, we've found
              that larger batch sizes tend to work better for larger datasets.

          classification_betas: If this is provided, we calculate F-beta scores at the specified beta values.
              The F-beta score is a generalization of F-1 score. This is only used for binary
              classification.

              With a beta of 1 (i.e. the F-1 score), precision and recall are given the same
              weight. A larger beta score puts more weight on recall and less on precision. A
              smaller beta score puts more weight on precision and less on recall.

          classification_n_classes: The number of classes in a classification task.

              This parameter is required for multiclass classification.

          classification_positive_class: The positive class in binary classification.

              This parameter is needed to generate precision, recall, and F1 metrics when
              doing binary classification.

          compute_classification_metrics: If set, we calculate classification-specific metrics such as accuracy and F-1
              score using the validation set at the end of every epoch. These metrics can be
              viewed in the
              [results file](/docs/guides/fine-tuning/analyzing-your-fine-tuned-model).

              In order to compute classification metrics, you must provide a
              `validation_file`. Additionally, you must specify `classification_n_classes` for
              multiclass classification or `classification_positive_class` for binary
              classification.

          learning_rate_multiplier: The learning rate multiplier to use for training. The fine-tuning learning rate
              is the original learning rate used for pretraining multiplied by this value.

              By default, the learning rate multiplier is the 0.05, 0.1, or 0.2 depending on
              final `batch_size` (larger learning rates tend to perform better with larger
              batch sizes). We recommend experimenting with values in the range 0.02 to 0.2 to
              see what produces the best results.

          model: The name of the base model to fine-tune. You can select one of "ada", "babbage",
              "curie", or "davinci". To learn more about these models, see the
              [Engines](https://beta.khulnasoft.com/docs/engines) documentation.

          n_epochs: The number of epochs to train the model for. An epoch refers to one full cycle
              through the training dataset.

          prompt_loss_weight: The weight to use for loss on the prompt tokens. This controls how much the
              model tries to learn to generate the prompt (as compared to the completion which
              always has a weight of 1.0), and can add a stabilizing effect to training when
              completions are short.

              If prompts are extremely long (relative to completions), it may make sense to
              reduce this weight so as to avoid over-prioritizing learning the prompt.

          training_file: The ID of an uploaded file that contains training data.

              See [upload file](/docs/api-reference/files/upload) for how to upload a file.

              Your dataset must be formatted as a JSONL file, where each training example is a
              JSON object with the keys "prompt" and "completion". Additionally, you must
              upload your file with the purpose `fine-tune`.

              See the [fine-tuning guide](/docs/guides/fine-tuning/creating-training-data) for
              more details.

          validation_file: The ID of an uploaded file that contains validation data.

              If you provide this file, the data is used to generate validation metrics
              periodically during fine-tuning. These metrics can be viewed in the
              [fine-tuning results file](/docs/guides/fine-tuning/analyzing-your-fine-tuned-model).
              Your train and validation data should be mutually exclusive.

              Your dataset must be formatted as a JSONL file, where each validation example is
              a JSON object with the keys "prompt" and "completion". Additionally, you must
              upload your file with the purpose `fine-tune`.

              See the [fine-tuning guide](/docs/guides/fine-tuning/creating-training-data) for
              more details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fine-tunes",
            body=maybe_transform(
                {
                    "batch_size": batch_size,
                    "classification_betas": classification_betas,
                    "classification_n_classes": classification_n_classes,
                    "classification_positive_class": classification_positive_class,
                    "compute_classification_metrics": compute_classification_metrics,
                    "learning_rate_multiplier": learning_rate_multiplier,
                    "model": model,
                    "n_epochs": n_epochs,
                    "prompt_loss_weight": prompt_loss_weight,
                    "training_file": training_file,
                    "validation_file": validation_file,
                },
                fine_tune_create_params.FineTuneCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTune,
        )

    def retrieve(
        self,
        fine_tune_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FineTune:
        """
        Gets info about the fine-tune job.

        [Learn more about Fine-tuning](/docs/guides/fine-tuning)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fine_tune_id:
            raise ValueError(f"Expected a non-empty value for `fine_tune_id` but received {fine_tune_id!r}")
        return self._get(
            f"/fine-tunes/{fine_tune_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTune,
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
    ) -> FineTuneListResponse:
        """List your organization's fine-tuning jobs"""
        return self._get(
            "/fine-tunes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTuneListResponse,
        )

    def cancel(
        self,
        fine_tune_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FineTune:
        """
        Immediately cancel a fine-tune job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fine_tune_id:
            raise ValueError(f"Expected a non-empty value for `fine_tune_id` but received {fine_tune_id!r}")
        return self._post(
            f"/fine-tunes/{fine_tune_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTune,
        )

    def get_events(
        self,
        fine_tune_id: str,
        *,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FineTuneGetEventsResponse:
        """
        Get fine-grained status updates for a fine-tune job.

        Args:
          stream: Whether to stream events for the fine-tune job. If set to true, events will be
              sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available. The stream will terminate with a `data: [DONE]`
              message when the job is finished (succeeded, cancelled, or failed).

              If set to false, only events generated so far will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fine_tune_id:
            raise ValueError(f"Expected a non-empty value for `fine_tune_id` but received {fine_tune_id!r}")
        return self._get(
            f"/fine-tunes/{fine_tune_id}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"stream": stream}, fine_tune_get_events_params.FineTuneGetEventsParams),
            ),
            cast_to=FineTuneGetEventsResponse,
        )


class AsyncFineTunesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFineTunesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/khulnasoft-openapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFineTunesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFineTunesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/khulnasoft-openapi-python#with_streaming_response
        """
        return AsyncFineTunesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        batch_size: Optional[int] | Omit = omit,
        classification_betas: Optional[Iterable[float]] | Omit = omit,
        classification_n_classes: Optional[int] | Omit = omit,
        classification_positive_class: Optional[str] | Omit = omit,
        compute_classification_metrics: Optional[bool] | Omit = omit,
        learning_rate_multiplier: Optional[float] | Omit = omit,
        model: Optional[str] | Omit = omit,
        n_epochs: Optional[int] | Omit = omit,
        prompt_loss_weight: Optional[float] | Omit = omit,
        training_file: str | Omit = omit,
        validation_file: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FineTune:
        """
        Creates a job that fine-tunes a specified model from a given dataset.

        Response includes details of the enqueued job including job status and the name
        of the fine-tuned models once complete.

        [Learn more about Fine-tuning](/docs/guides/fine-tuning)

        Args:
          batch_size: The batch size to use for training. The batch size is the number of training
              examples used to train a single forward and backward pass.

              By default, the batch size will be dynamically configured to be ~0.2% of the
              number of examples in the training set, capped at 256 - in general, we've found
              that larger batch sizes tend to work better for larger datasets.

          classification_betas: If this is provided, we calculate F-beta scores at the specified beta values.
              The F-beta score is a generalization of F-1 score. This is only used for binary
              classification.

              With a beta of 1 (i.e. the F-1 score), precision and recall are given the same
              weight. A larger beta score puts more weight on recall and less on precision. A
              smaller beta score puts more weight on precision and less on recall.

          classification_n_classes: The number of classes in a classification task.

              This parameter is required for multiclass classification.

          classification_positive_class: The positive class in binary classification.

              This parameter is needed to generate precision, recall, and F1 metrics when
              doing binary classification.

          compute_classification_metrics: If set, we calculate classification-specific metrics such as accuracy and F-1
              score using the validation set at the end of every epoch. These metrics can be
              viewed in the
              [results file](/docs/guides/fine-tuning/analyzing-your-fine-tuned-model).

              In order to compute classification metrics, you must provide a
              `validation_file`. Additionally, you must specify `classification_n_classes` for
              multiclass classification or `classification_positive_class` for binary
              classification.

          learning_rate_multiplier: The learning rate multiplier to use for training. The fine-tuning learning rate
              is the original learning rate used for pretraining multiplied by this value.

              By default, the learning rate multiplier is the 0.05, 0.1, or 0.2 depending on
              final `batch_size` (larger learning rates tend to perform better with larger
              batch sizes). We recommend experimenting with values in the range 0.02 to 0.2 to
              see what produces the best results.

          model: The name of the base model to fine-tune. You can select one of "ada", "babbage",
              "curie", or "davinci". To learn more about these models, see the
              [Engines](https://beta.khulnasoft.com/docs/engines) documentation.

          n_epochs: The number of epochs to train the model for. An epoch refers to one full cycle
              through the training dataset.

          prompt_loss_weight: The weight to use for loss on the prompt tokens. This controls how much the
              model tries to learn to generate the prompt (as compared to the completion which
              always has a weight of 1.0), and can add a stabilizing effect to training when
              completions are short.

              If prompts are extremely long (relative to completions), it may make sense to
              reduce this weight so as to avoid over-prioritizing learning the prompt.

          training_file: The ID of an uploaded file that contains training data.

              See [upload file](/docs/api-reference/files/upload) for how to upload a file.

              Your dataset must be formatted as a JSONL file, where each training example is a
              JSON object with the keys "prompt" and "completion". Additionally, you must
              upload your file with the purpose `fine-tune`.

              See the [fine-tuning guide](/docs/guides/fine-tuning/creating-training-data) for
              more details.

          validation_file: The ID of an uploaded file that contains validation data.

              If you provide this file, the data is used to generate validation metrics
              periodically during fine-tuning. These metrics can be viewed in the
              [fine-tuning results file](/docs/guides/fine-tuning/analyzing-your-fine-tuned-model).
              Your train and validation data should be mutually exclusive.

              Your dataset must be formatted as a JSONL file, where each validation example is
              a JSON object with the keys "prompt" and "completion". Additionally, you must
              upload your file with the purpose `fine-tune`.

              See the [fine-tuning guide](/docs/guides/fine-tuning/creating-training-data) for
              more details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fine-tunes",
            body=await async_maybe_transform(
                {
                    "batch_size": batch_size,
                    "classification_betas": classification_betas,
                    "classification_n_classes": classification_n_classes,
                    "classification_positive_class": classification_positive_class,
                    "compute_classification_metrics": compute_classification_metrics,
                    "learning_rate_multiplier": learning_rate_multiplier,
                    "model": model,
                    "n_epochs": n_epochs,
                    "prompt_loss_weight": prompt_loss_weight,
                    "training_file": training_file,
                    "validation_file": validation_file,
                },
                fine_tune_create_params.FineTuneCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTune,
        )

    async def retrieve(
        self,
        fine_tune_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FineTune:
        """
        Gets info about the fine-tune job.

        [Learn more about Fine-tuning](/docs/guides/fine-tuning)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fine_tune_id:
            raise ValueError(f"Expected a non-empty value for `fine_tune_id` but received {fine_tune_id!r}")
        return await self._get(
            f"/fine-tunes/{fine_tune_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTune,
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
    ) -> FineTuneListResponse:
        """List your organization's fine-tuning jobs"""
        return await self._get(
            "/fine-tunes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTuneListResponse,
        )

    async def cancel(
        self,
        fine_tune_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FineTune:
        """
        Immediately cancel a fine-tune job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fine_tune_id:
            raise ValueError(f"Expected a non-empty value for `fine_tune_id` but received {fine_tune_id!r}")
        return await self._post(
            f"/fine-tunes/{fine_tune_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTune,
        )

    async def get_events(
        self,
        fine_tune_id: str,
        *,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FineTuneGetEventsResponse:
        """
        Get fine-grained status updates for a fine-tune job.

        Args:
          stream: Whether to stream events for the fine-tune job. If set to true, events will be
              sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available. The stream will terminate with a `data: [DONE]`
              message when the job is finished (succeeded, cancelled, or failed).

              If set to false, only events generated so far will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fine_tune_id:
            raise ValueError(f"Expected a non-empty value for `fine_tune_id` but received {fine_tune_id!r}")
        return await self._get(
            f"/fine-tunes/{fine_tune_id}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"stream": stream}, fine_tune_get_events_params.FineTuneGetEventsParams
                ),
            ),
            cast_to=FineTuneGetEventsResponse,
        )


class FineTunesResourceWithRawResponse:
    def __init__(self, fine_tunes: FineTunesResource) -> None:
        self._fine_tunes = fine_tunes

        self.create = to_raw_response_wrapper(
            fine_tunes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            fine_tunes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            fine_tunes.list,
        )
        self.cancel = to_raw_response_wrapper(
            fine_tunes.cancel,
        )
        self.get_events = to_raw_response_wrapper(
            fine_tunes.get_events,
        )


class AsyncFineTunesResourceWithRawResponse:
    def __init__(self, fine_tunes: AsyncFineTunesResource) -> None:
        self._fine_tunes = fine_tunes

        self.create = async_to_raw_response_wrapper(
            fine_tunes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            fine_tunes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            fine_tunes.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            fine_tunes.cancel,
        )
        self.get_events = async_to_raw_response_wrapper(
            fine_tunes.get_events,
        )


class FineTunesResourceWithStreamingResponse:
    def __init__(self, fine_tunes: FineTunesResource) -> None:
        self._fine_tunes = fine_tunes

        self.create = to_streamed_response_wrapper(
            fine_tunes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            fine_tunes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            fine_tunes.list,
        )
        self.cancel = to_streamed_response_wrapper(
            fine_tunes.cancel,
        )
        self.get_events = to_streamed_response_wrapper(
            fine_tunes.get_events,
        )


class AsyncFineTunesResourceWithStreamingResponse:
    def __init__(self, fine_tunes: AsyncFineTunesResource) -> None:
        self._fine_tunes = fine_tunes

        self.create = async_to_streamed_response_wrapper(
            fine_tunes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            fine_tunes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            fine_tunes.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            fine_tunes.cancel,
        )
        self.get_events = async_to_streamed_response_wrapper(
            fine_tunes.get_events,
        )
