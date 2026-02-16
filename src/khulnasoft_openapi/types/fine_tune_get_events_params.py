# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FineTuneGetEventsParams"]


class FineTuneGetEventsParams(TypedDict, total=False):
    stream: bool
    """Whether to stream events for the fine-tune job.

    If set to true, events will be sent as data-only
    [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
    as they become available. The stream will terminate with a `data: [DONE]`
    message when the job is finished (succeeded, cancelled, or failed).

    If set to false, only events generated so far will be returned.
    """
