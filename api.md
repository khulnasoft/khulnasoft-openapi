# Engines

Types:

```python
from khulnasoft_openapi.types import (
    Engine,
    EngineListResponse,
    EngineCreateCompletionResponse,
    EngineCreateEmbeddingResponse,
    EngineSearchResponse,
)
```

Methods:

- <code title="get /engines/{engine_id}">client.engines.<a href="./src/khulnasoft_openapi/resources/engines.py">retrieve</a>(engine_id) -> <a href="./src/khulnasoft_openapi/types/engine.py">Engine</a></code>
- <code title="get /engines">client.engines.<a href="./src/khulnasoft_openapi/resources/engines.py">list</a>() -> <a href="./src/khulnasoft_openapi/types/engine_list_response.py">EngineListResponse</a></code>
- <code title="post /engines/{engine_id}/completions">client.engines.<a href="./src/khulnasoft_openapi/resources/engines.py">create_completion</a>(engine_id, \*\*<a href="src/khulnasoft_openapi/types/engine_create_completion_params.py">params</a>) -> <a href="./src/khulnasoft_openapi/types/engine_create_completion_response.py">EngineCreateCompletionResponse</a></code>
- <code title="post /engines/{engine_id}/embeddings">client.engines.<a href="./src/khulnasoft_openapi/resources/engines.py">create_embedding</a>(engine_id, \*\*<a href="src/khulnasoft_openapi/types/engine_create_embedding_params.py">params</a>) -> <a href="./src/khulnasoft_openapi/types/engine_create_embedding_response.py">EngineCreateEmbeddingResponse</a></code>
- <code title="post /engines/{engine_id}/search">client.engines.<a href="./src/khulnasoft_openapi/resources/engines.py">search</a>(engine_id, \*\*<a href="src/khulnasoft_openapi/types/engine_search_params.py">params</a>) -> <a href="./src/khulnasoft_openapi/types/engine_search_response.py">EngineSearchResponse</a></code>

# Files

Types:

```python
from khulnasoft_openapi.types import (
    KhulnaSoftFile,
    FileListResponse,
    FileDeleteResponse,
    FileGetContentResponse,
)
```

Methods:

- <code title="get /files/{file_id}">client.files.<a href="./src/khulnasoft_openapi/resources/files.py">retrieve</a>(file_id) -> <a href="./src/khulnasoft_openapi/types/khulna_soft_file.py">KhulnaSoftFile</a></code>
- <code title="get /files">client.files.<a href="./src/khulnasoft_openapi/resources/files.py">list</a>() -> <a href="./src/khulnasoft_openapi/types/file_list_response.py">FileListResponse</a></code>
- <code title="delete /files/{file_id}">client.files.<a href="./src/khulnasoft_openapi/resources/files.py">delete</a>(file_id) -> <a href="./src/khulnasoft_openapi/types/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="get /files/{file_id}/content">client.files.<a href="./src/khulnasoft_openapi/resources/files.py">get_content</a>(file_id) -> str</code>
- <code title="post /files">client.files.<a href="./src/khulnasoft_openapi/resources/files.py">upload</a>(\*\*<a href="src/khulnasoft_openapi/types/file_upload_params.py">params</a>) -> <a href="./src/khulnasoft_openapi/types/khulna_soft_file.py">KhulnaSoftFile</a></code>

# Answers

Types:

```python
from khulnasoft_openapi.types import AnswerCreateResponse
```

Methods:

- <code title="post /answers">client.answers.<a href="./src/khulnasoft_openapi/resources/answers.py">create</a>(\*\*<a href="src/khulnasoft_openapi/types/answer_create_params.py">params</a>) -> <a href="./src/khulnasoft_openapi/types/answer_create_response.py">AnswerCreateResponse</a></code>

# Classifications

Types:

```python
from khulnasoft_openapi.types import ClassificationCreateResponse
```

Methods:

- <code title="post /classifications">client.classifications.<a href="./src/khulnasoft_openapi/resources/classifications.py">create</a>(\*\*<a href="src/khulnasoft_openapi/types/classification_create_params.py">params</a>) -> <a href="./src/khulnasoft_openapi/types/classification_create_response.py">ClassificationCreateResponse</a></code>

# FineTunes

Types:

```python
from khulnasoft_openapi.types import (
    FineTune,
    FineTuneEvent,
    FineTuneListResponse,
    FineTuneGetEventsResponse,
)
```

Methods:

- <code title="post /fine-tunes">client.fine_tunes.<a href="./src/khulnasoft_openapi/resources/fine_tunes.py">create</a>(\*\*<a href="src/khulnasoft_openapi/types/fine_tune_create_params.py">params</a>) -> <a href="./src/khulnasoft_openapi/types/fine_tune.py">FineTune</a></code>
- <code title="get /fine-tunes/{fine_tune_id}">client.fine_tunes.<a href="./src/khulnasoft_openapi/resources/fine_tunes.py">retrieve</a>(fine_tune_id) -> <a href="./src/khulnasoft_openapi/types/fine_tune.py">FineTune</a></code>
- <code title="get /fine-tunes">client.fine_tunes.<a href="./src/khulnasoft_openapi/resources/fine_tunes.py">list</a>() -> <a href="./src/khulnasoft_openapi/types/fine_tune_list_response.py">FineTuneListResponse</a></code>
- <code title="post /fine-tunes/{fine_tune_id}/cancel">client.fine_tunes.<a href="./src/khulnasoft_openapi/resources/fine_tunes.py">cancel</a>(fine_tune_id) -> <a href="./src/khulnasoft_openapi/types/fine_tune.py">FineTune</a></code>
- <code title="get /fine-tunes/{fine_tune_id}/events">client.fine_tunes.<a href="./src/khulnasoft_openapi/resources/fine_tunes.py">get_events</a>(fine_tune_id, \*\*<a href="src/khulnasoft_openapi/types/fine_tune_get_events_params.py">params</a>) -> <a href="./src/khulnasoft_openapi/types/fine_tune_get_events_response.py">FineTuneGetEventsResponse</a></code>
