# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from khulnasoft_openapi import KhulnasoftOpenAPI, AsyncKhulnasoftOpenAPI
from khulnasoft_openapi.types import (
    Engine,
    EngineListResponse,
    EngineSearchResponse,
    EngineCreateEmbeddingResponse,
    EngineCreateCompletionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEngines:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: KhulnasoftOpenAPI) -> None:
        engine = client.engines.retrieve(
            "davinci",
        )
        assert_matches_type(Engine, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: KhulnasoftOpenAPI) -> None:
        response = client.engines.with_raw_response.retrieve(
            "davinci",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = response.parse()
        assert_matches_type(Engine, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: KhulnasoftOpenAPI) -> None:
        with client.engines.with_streaming_response.retrieve(
            "davinci",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = response.parse()
            assert_matches_type(Engine, engine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: KhulnasoftOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engine_id` but received ''"):
            client.engines.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: KhulnasoftOpenAPI) -> None:
        engine = client.engines.list()
        assert_matches_type(EngineListResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: KhulnasoftOpenAPI) -> None:
        response = client.engines.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = response.parse()
        assert_matches_type(EngineListResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: KhulnasoftOpenAPI) -> None:
        with client.engines.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = response.parse()
            assert_matches_type(EngineListResponse, engine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_completion(self, client: KhulnasoftOpenAPI) -> None:
        engine = client.engines.create_completion(
            engine_id="davinci",
        )
        assert_matches_type(EngineCreateCompletionResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_completion_with_all_params(self, client: KhulnasoftOpenAPI) -> None:
        engine = client.engines.create_completion(
            engine_id="davinci",
            best_of=0,
            echo=True,
            frequency_penalty=-2,
            logit_bias={},
            logprobs=0,
            max_tokens=16,
            n=1,
            presence_penalty=-2,
            prompt="This is a test.",
            stop="\n",
            stream=True,
            temperature=1,
            top_p=1,
        )
        assert_matches_type(EngineCreateCompletionResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_completion(self, client: KhulnasoftOpenAPI) -> None:
        response = client.engines.with_raw_response.create_completion(
            engine_id="davinci",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = response.parse()
        assert_matches_type(EngineCreateCompletionResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_completion(self, client: KhulnasoftOpenAPI) -> None:
        with client.engines.with_streaming_response.create_completion(
            engine_id="davinci",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = response.parse()
            assert_matches_type(EngineCreateCompletionResponse, engine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_completion(self, client: KhulnasoftOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engine_id` but received ''"):
            client.engines.with_raw_response.create_completion(
                engine_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_embedding(self, client: KhulnasoftOpenAPI) -> None:
        engine = client.engines.create_embedding(
            engine_id="babbage-similarity",
        )
        assert_matches_type(EngineCreateEmbeddingResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_embedding_with_all_params(self, client: KhulnasoftOpenAPI) -> None:
        engine = client.engines.create_embedding(
            engine_id="babbage-similarity",
            input="The quick brown fox jumped over the lazy dog",
        )
        assert_matches_type(EngineCreateEmbeddingResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_embedding(self, client: KhulnasoftOpenAPI) -> None:
        response = client.engines.with_raw_response.create_embedding(
            engine_id="babbage-similarity",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = response.parse()
        assert_matches_type(EngineCreateEmbeddingResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_embedding(self, client: KhulnasoftOpenAPI) -> None:
        with client.engines.with_streaming_response.create_embedding(
            engine_id="babbage-similarity",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = response.parse()
            assert_matches_type(EngineCreateEmbeddingResponse, engine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_embedding(self, client: KhulnasoftOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engine_id` but received ''"):
            client.engines.with_raw_response.create_embedding(
                engine_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: KhulnasoftOpenAPI) -> None:
        engine = client.engines.search(
            engine_id="davinci",
        )
        assert_matches_type(EngineSearchResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: KhulnasoftOpenAPI) -> None:
        engine = client.engines.search(
            engine_id="davinci",
            documents=["string"],
            file="file",
            max_rerank=1,
            query="the president",
            return_metadata=True,
        )
        assert_matches_type(EngineSearchResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: KhulnasoftOpenAPI) -> None:
        response = client.engines.with_raw_response.search(
            engine_id="davinci",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = response.parse()
        assert_matches_type(EngineSearchResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: KhulnasoftOpenAPI) -> None:
        with client.engines.with_streaming_response.search(
            engine_id="davinci",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = response.parse()
            assert_matches_type(EngineSearchResponse, engine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_search(self, client: KhulnasoftOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engine_id` but received ''"):
            client.engines.with_raw_response.search(
                engine_id="",
            )


class TestAsyncEngines:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        engine = await async_client.engines.retrieve(
            "davinci",
        )
        assert_matches_type(Engine, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        response = await async_client.engines.with_raw_response.retrieve(
            "davinci",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = await response.parse()
        assert_matches_type(Engine, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        async with async_client.engines.with_streaming_response.retrieve(
            "davinci",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = await response.parse()
            assert_matches_type(Engine, engine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engine_id` but received ''"):
            await async_client.engines.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        engine = await async_client.engines.list()
        assert_matches_type(EngineListResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        response = await async_client.engines.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = await response.parse()
        assert_matches_type(EngineListResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        async with async_client.engines.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = await response.parse()
            assert_matches_type(EngineListResponse, engine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_completion(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        engine = await async_client.engines.create_completion(
            engine_id="davinci",
        )
        assert_matches_type(EngineCreateCompletionResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_completion_with_all_params(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        engine = await async_client.engines.create_completion(
            engine_id="davinci",
            best_of=0,
            echo=True,
            frequency_penalty=-2,
            logit_bias={},
            logprobs=0,
            max_tokens=16,
            n=1,
            presence_penalty=-2,
            prompt="This is a test.",
            stop="\n",
            stream=True,
            temperature=1,
            top_p=1,
        )
        assert_matches_type(EngineCreateCompletionResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_completion(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        response = await async_client.engines.with_raw_response.create_completion(
            engine_id="davinci",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = await response.parse()
        assert_matches_type(EngineCreateCompletionResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_completion(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        async with async_client.engines.with_streaming_response.create_completion(
            engine_id="davinci",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = await response.parse()
            assert_matches_type(EngineCreateCompletionResponse, engine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_completion(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engine_id` but received ''"):
            await async_client.engines.with_raw_response.create_completion(
                engine_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_embedding(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        engine = await async_client.engines.create_embedding(
            engine_id="babbage-similarity",
        )
        assert_matches_type(EngineCreateEmbeddingResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_embedding_with_all_params(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        engine = await async_client.engines.create_embedding(
            engine_id="babbage-similarity",
            input="The quick brown fox jumped over the lazy dog",
        )
        assert_matches_type(EngineCreateEmbeddingResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_embedding(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        response = await async_client.engines.with_raw_response.create_embedding(
            engine_id="babbage-similarity",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = await response.parse()
        assert_matches_type(EngineCreateEmbeddingResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_embedding(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        async with async_client.engines.with_streaming_response.create_embedding(
            engine_id="babbage-similarity",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = await response.parse()
            assert_matches_type(EngineCreateEmbeddingResponse, engine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_embedding(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engine_id` but received ''"):
            await async_client.engines.with_raw_response.create_embedding(
                engine_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        engine = await async_client.engines.search(
            engine_id="davinci",
        )
        assert_matches_type(EngineSearchResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        engine = await async_client.engines.search(
            engine_id="davinci",
            documents=["string"],
            file="file",
            max_rerank=1,
            query="the president",
            return_metadata=True,
        )
        assert_matches_type(EngineSearchResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        response = await async_client.engines.with_raw_response.search(
            engine_id="davinci",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engine = await response.parse()
        assert_matches_type(EngineSearchResponse, engine, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        async with async_client.engines.with_streaming_response.search(
            engine_id="davinci",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engine = await response.parse()
            assert_matches_type(EngineSearchResponse, engine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_search(self, async_client: AsyncKhulnasoftOpenAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engine_id` but received ''"):
            await async_client.engines.with_raw_response.search(
                engine_id="",
            )
