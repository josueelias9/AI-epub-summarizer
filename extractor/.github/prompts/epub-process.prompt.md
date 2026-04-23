---
mode: agent
description: End-to-end workflow for processing a new EPUB file via the API
---

Process the EPUB file at **${input:epubFilePath}** end-to-end using the running API.

Base URL: `http://localhost:8000/api/v1`  
See [`api.http`](../../api.http) for ready-to-use request examples.

## Steps

### 1 — Create a book record
```
POST /api/v1/books
{ "title": "<title>", "file_path": "<epubFilePath>" }
```
Save the returned `id` as `BOOK_ID`.

### 2 — Create a processing job
```
POST /api/v1/jobs
{ "book_id": BOOK_ID, "job_type": "extraction" }
```
Save the returned `id` as `JOB_ID`.

### 3 — Poll until complete
```
GET /api/v1/jobs/JOB_ID
```
Repeat until `status` is `"completed"` or `"failed"`.  
On failure, inspect `error_message` in the response.

### 4 — Verify chapters were stored
```
GET /api/v1/books/BOOK_ID/chapters
```
Confirm `total` > 0.

### 5 — (Optional) Generate Marp presentation
The extractor writes a Marp-compatible markdown file.  
Output lands in the `OUTPUT_PATH` directory (see env var in [`app/core/config.py`](../../app/core/config.py)).  
Open `output/book_presentation.md` with the Marp VS Code extension to preview.

### 6 — (Optional) Trigger AI summarization
```
POST /api/v1/jobs
{ "book_id": BOOK_ID, "job_type": "summarization" }
```
Requires Ollama running at `http://ollama:11434` with a model loaded (see `/workspace/ollama/init_ollama.sh`).

## Troubleshooting
- **DB connection error**: run `python tests/test_db.py` and check env vars.
- **Ollama unreachable**: verify Ollama service is up; check `AIAgent.test_connection()` in [`app/infrastructure/ai/ollama_agent.py`](../../app/infrastructure/ai/ollama_agent.py).
