# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from khulnasoft_openapi import KhulnasoftOpenAPI, AsyncKhulnasoftOpenAPI
from khulnasoft_openapi.types import AnswerCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnswers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: KhulnasoftOpenAPI) -> None:
        answer = client.answers.create()
        assert_matches_type(AnswerCreateResponse, answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: KhulnasoftOpenAPI) -> None:
        answer = client.answers.create(
            documents=["string"],
            examples=[["x", "x"]],
            examples_context="Ottawa, Canada's capital, is located in the east of southern Ontario, near the city of Montréal and the U.S. border.",
            expand=[{}],
            file="file",
            logit_bias={},
            logprobs=0,
            max_rerank=0,
            max_tokens=0,
            model="model",
            n=1,
            question="What is the capital of Japan?",
            return_metadata=True,
            return_prompt=True,
            search_model="search_model",
            stop="\n",
            temperature=0,
        )
        assert_matches_type(AnswerCreateResponse, answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: KhulnasoftOpenAPI) -> None:
        response = client.answers.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        answer = response.parse()
        assert_matches_type(AnswerCreateResponse, answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: KhulnasoftOpenAPI) -> None:
        with client.answers.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            answer = response.parse()
            assert_matches_type(AnswerCreateResponse, answer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAnswers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        answer = await async_client.answers.create()
        assert_matches_type(AnswerCreateResponse, answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        answer = await async_client.answers.create(
            documents=["string"],
            examples=[["x", "x"]],
            examples_context="Ottawa, Canada's capital, is located in the east of southern Ontario, near the city of Montréal and the U.S. border.",
            expand=[{}],
            file="file",
            logit_bias={},
            logprobs=0,
            max_rerank=0,
            max_tokens=0,
            model="model",
            n=1,
            question="What is the capital of Japan?",
            return_metadata=True,
            return_prompt=True,
            search_model="search_model",
            stop="\n",
            temperature=0,
        )
        assert_matches_type(AnswerCreateResponse, answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        response = await async_client.answers.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        answer = await response.parse()
        assert_matches_type(AnswerCreateResponse, answer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        async with async_client.answers.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            answer = await response.parse()
            assert_matches_type(AnswerCreateResponse, answer, path=["response"])

        assert cast(Any, response.is_closed) is True
