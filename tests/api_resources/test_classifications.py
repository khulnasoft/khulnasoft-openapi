# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from khulnasoft_openapi import KhulnasoftOpenAPI, AsyncKhulnasoftOpenAPI
from khulnasoft_openapi.types import ClassificationCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClassifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: KhulnasoftOpenAPI) -> None:
        classification = client.classifications.create()
        assert_matches_type(ClassificationCreateResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: KhulnasoftOpenAPI) -> None:
        classification = client.classifications.create(
            examples=[["x", "x"], ["x", "x"]],
            expand=[{}],
            file="file",
            labels=["Positive", "Negative"],
            logit_bias={},
            logprobs=0,
            max_examples=0,
            model="model",
            query="The plot is not very attractive.",
            return_metadata=True,
            return_prompt=True,
            search_model="search_model",
            temperature=0,
        )
        assert_matches_type(ClassificationCreateResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: KhulnasoftOpenAPI) -> None:
        response = client.classifications.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classification = response.parse()
        assert_matches_type(ClassificationCreateResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: KhulnasoftOpenAPI) -> None:
        with client.classifications.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classification = response.parse()
            assert_matches_type(ClassificationCreateResponse, classification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClassifications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        classification = await async_client.classifications.create()
        assert_matches_type(ClassificationCreateResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        classification = await async_client.classifications.create(
            examples=[["x", "x"], ["x", "x"]],
            expand=[{}],
            file="file",
            labels=["Positive", "Negative"],
            logit_bias={},
            logprobs=0,
            max_examples=0,
            model="model",
            query="The plot is not very attractive.",
            return_metadata=True,
            return_prompt=True,
            search_model="search_model",
            temperature=0,
        )
        assert_matches_type(ClassificationCreateResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        response = await async_client.classifications.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classification = await response.parse()
        assert_matches_type(ClassificationCreateResponse, classification, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        async with async_client.classifications.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classification = await response.parse()
            assert_matches_type(ClassificationCreateResponse, classification, path=["response"])

        assert cast(Any, response.is_closed) is True
