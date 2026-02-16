# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from khulnasoft_openapi import KhulnasoftOpenAPI, AsyncKhulnasoftOpenAPI
from khulnasoft_openapi.types import (
    FineTune,
    FineTuneListResponse,
    FineTuneGetEventsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFineTunes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: KhulnasoftOpenAPI) -> None:
        fine_tune = client.fine_tunes.create()
        assert_matches_type(FineTune, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: KhulnasoftOpenAPI) -> None:
        fine_tune = client.fine_tunes.create(
            batch_size=0,
            classification_betas=[0.6, 1, 1.5, 2],
            classification_n_classes=0,
            classification_positive_class="classification_positive_class",
            compute_classification_metrics=True,
            learning_rate_multiplier=0,
            model="model",
            n_epochs=0,
            prompt_loss_weight=0,
            training_file="file-ajSREls59WBbvgSzJSVWxMCB",
            validation_file="file-XjSREls59WBbvgSzJSVWxMCa",
        )
        assert_matches_type(FineTune, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: KhulnasoftOpenAPI) -> None:
        response = client.fine_tunes.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune = response.parse()
        assert_matches_type(FineTune, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: KhulnasoftOpenAPI) -> None:
        with client.fine_tunes.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune = response.parse()
            assert_matches_type(FineTune, fine_tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KhulnasoftOpenAPI) -> None:
        fine_tune = client.fine_tunes.retrieve(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )
        assert_matches_type(FineTune, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KhulnasoftOpenAPI) -> None:
        response = client.fine_tunes.with_raw_response.retrieve(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune = response.parse()
        assert_matches_type(FineTune, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KhulnasoftOpenAPI) -> None:
        with client.fine_tunes.with_streaming_response.retrieve(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune = response.parse()
            assert_matches_type(FineTune, fine_tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KhulnasoftOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fine_tune_id` but received ''"):
            client.fine_tunes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: KhulnasoftOpenAPI) -> None:
        fine_tune = client.fine_tunes.list()
        assert_matches_type(FineTuneListResponse, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KhulnasoftOpenAPI) -> None:
        response = client.fine_tunes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune = response.parse()
        assert_matches_type(FineTuneListResponse, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KhulnasoftOpenAPI) -> None:
        with client.fine_tunes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune = response.parse()
            assert_matches_type(FineTuneListResponse, fine_tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: KhulnasoftOpenAPI) -> None:
        fine_tune = client.fine_tunes.cancel(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )
        assert_matches_type(FineTune, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: KhulnasoftOpenAPI) -> None:
        response = client.fine_tunes.with_raw_response.cancel(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune = response.parse()
        assert_matches_type(FineTune, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: KhulnasoftOpenAPI) -> None:
        with client.fine_tunes.with_streaming_response.cancel(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune = response.parse()
            assert_matches_type(FineTune, fine_tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: KhulnasoftOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fine_tune_id` but received ''"):
            client.fine_tunes.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_events(self, client: KhulnasoftOpenAPI) -> None:
        fine_tune = client.fine_tunes.get_events(
            fine_tune_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )
        assert_matches_type(FineTuneGetEventsResponse, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_events_with_all_params(self, client: KhulnasoftOpenAPI) -> None:
        fine_tune = client.fine_tunes.get_events(
            fine_tune_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
            stream=True,
        )
        assert_matches_type(FineTuneGetEventsResponse, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_events(self, client: KhulnasoftOpenAPI) -> None:
        response = client.fine_tunes.with_raw_response.get_events(
            fine_tune_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune = response.parse()
        assert_matches_type(FineTuneGetEventsResponse, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_events(self, client: KhulnasoftOpenAPI) -> None:
        with client.fine_tunes.with_streaming_response.get_events(
            fine_tune_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune = response.parse()
            assert_matches_type(FineTuneGetEventsResponse, fine_tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_events(self, client: KhulnasoftOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fine_tune_id` but received ''"):
            client.fine_tunes.with_raw_response.get_events(
                fine_tune_id="",
            )


class TestAsyncFineTunes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        fine_tune = await async_client.fine_tunes.create()
        assert_matches_type(FineTune, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        fine_tune = await async_client.fine_tunes.create(
            batch_size=0,
            classification_betas=[0.6, 1, 1.5, 2],
            classification_n_classes=0,
            classification_positive_class="classification_positive_class",
            compute_classification_metrics=True,
            learning_rate_multiplier=0,
            model="model",
            n_epochs=0,
            prompt_loss_weight=0,
            training_file="file-ajSREls59WBbvgSzJSVWxMCB",
            validation_file="file-XjSREls59WBbvgSzJSVWxMCa",
        )
        assert_matches_type(FineTune, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        response = await async_client.fine_tunes.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune = await response.parse()
        assert_matches_type(FineTune, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        async with async_client.fine_tunes.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune = await response.parse()
            assert_matches_type(FineTune, fine_tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        fine_tune = await async_client.fine_tunes.retrieve(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )
        assert_matches_type(FineTune, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        response = await async_client.fine_tunes.with_raw_response.retrieve(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune = await response.parse()
        assert_matches_type(FineTune, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        async with async_client.fine_tunes.with_streaming_response.retrieve(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune = await response.parse()
            assert_matches_type(FineTune, fine_tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fine_tune_id` but received ''"):
            await async_client.fine_tunes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        fine_tune = await async_client.fine_tunes.list()
        assert_matches_type(FineTuneListResponse, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        response = await async_client.fine_tunes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune = await response.parse()
        assert_matches_type(FineTuneListResponse, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        async with async_client.fine_tunes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune = await response.parse()
            assert_matches_type(FineTuneListResponse, fine_tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        fine_tune = await async_client.fine_tunes.cancel(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )
        assert_matches_type(FineTune, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        response = await async_client.fine_tunes.with_raw_response.cancel(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune = await response.parse()
        assert_matches_type(FineTune, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        async with async_client.fine_tunes.with_streaming_response.cancel(
            "ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune = await response.parse()
            assert_matches_type(FineTune, fine_tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fine_tune_id` but received ''"):
            await async_client.fine_tunes.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_events(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        fine_tune = await async_client.fine_tunes.get_events(
            fine_tune_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )
        assert_matches_type(FineTuneGetEventsResponse, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_events_with_all_params(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        fine_tune = await async_client.fine_tunes.get_events(
            fine_tune_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
            stream=True,
        )
        assert_matches_type(FineTuneGetEventsResponse, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_events(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        response = await async_client.fine_tunes.with_raw_response.get_events(
            fine_tune_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune = await response.parse()
        assert_matches_type(FineTuneGetEventsResponse, fine_tune, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_events(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        async with async_client.fine_tunes.with_streaming_response.get_events(
            fine_tune_id="ft-AF1WoRqd3aJAHsqc9NY7iL8F",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune = await response.parse()
            assert_matches_type(FineTuneGetEventsResponse, fine_tune, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_events(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fine_tune_id` but received ''"):
            await async_client.fine_tunes.with_raw_response.get_events(
                fine_tune_id="",
            )
