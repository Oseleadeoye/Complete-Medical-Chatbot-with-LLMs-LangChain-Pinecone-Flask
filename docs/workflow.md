# How the Application Works

A walkthrough of the full pipeline — from PDF ingestion to answering a question in the chat.

---

## Architecture Overview

```
User Question
     │
     ▼
Flask App (app.py)
     │
     ├── Contextualize question using chat history
     │        │
     │        ▼
     │   History-Aware Retriever
     │        │
     ▼        ▼
Pinecone Vector Store  ←──  HuggingFace Embeddings
     │
     ▼
Relevant document chunks (top 3)
     │
     ▼
GPT-4o (OpenAI)  +  System Prompt
     │
     ▼
Answer returned to user
```

---

## 1. Indexing (one-time setup)

Run `store_index.py` once before the app starts. It:

1. **Loads** the PDF from `data/Medical_book.pdf` using `PyPDFLoader`
2. **Splits** the text into 500-character chunks with 20-character overlap
3. **Embeds** each chunk using `sentence-transformers/all-MiniLM-L6-v2` (384 dimensions)
4. **Upserts** the vectors into a Pinecone index named `medical-chatbot`

This only needs to be run again if the source PDF changes.

---

## 2. App Startup

When `app.py` starts, it:

1. Loads environment variables (`PINECONE_API_KEY`, `OPENAI_API_KEY`)
2. Downloads the HuggingFace embeddings model (cached after first run)
3. Connects to the existing Pinecone index
4. Initialises the LangChain RAG chain (retriever + GPT-4o)

---

## 3. Handling a Chat Message

When a user sends a message (`POST /get`):

1. **Contextualize** — the chat history and new question are passed to GPT-4o, which reformulates the question as a standalone query (so follow-up questions work correctly)
2. **Retrieve** — the reformulated question is embedded and used to search Pinecone for the 3 most similar document chunks
3. **Answer** — GPT-4o receives the retrieved chunks as context and generates a concise answer (max 3 sentences)
4. **History update** — the question and answer are appended to the in-memory `chat_history` list for future context

---

## 4. Key Files

| File | Purpose |
|------|---------|
| `app.py` | Flask web server and RAG chain setup |
| `store_index.py` | One-time script to embed and index the PDF |
| `src/helper.py` | PDF loading, text splitting, embeddings download |
| `src/prompt.py` | System prompts for the LLM |
| `templates/chat.html` | Chat UI |
| `data/Medical_book.pdf` | Source knowledge base |
| `Dockerfile` | Container definition for deployment |

---

## 5. CI/CD

Pushing to `main` triggers Render's automatic redeploy via its GitHub integration. No workflow file is required — Render handles the build and deploy pipeline natively.
