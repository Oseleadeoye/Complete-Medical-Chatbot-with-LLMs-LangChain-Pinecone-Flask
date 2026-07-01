# Project Overview

## What is this?

The Medical Chatbot is a conversational AI assistant that answers medical questions based on a curated knowledge base. It uses Retrieval-Augmented Generation (RAG) to ground every answer in real source material rather than relying purely on the language model's training data.

Users type a question in the chat UI and receive a concise, sourced answer. The system maintains conversation history so follow-up questions are understood in context.

---

## Why RAG?

Large language models can hallucinate — generating confident but incorrect medical information. RAG addresses this by:

1. Searching a trusted document index for relevant content
2. Passing only that content to the LLM as context
3. Instructing the model to answer only from that context, and to say "I don't know" if the answer isn't there

This makes the chatbot safer and more reliable for a medical domain.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Web framework | Flask |
| LLM | Qwen3.6 27B (via Groq API, free tier) |
| Embeddings | `sentence-transformers/all-MiniLM-L6-v2` (HuggingFace) |
| Vector database | Pinecone |
| RAG orchestration | LangChain |
| Containerisation | Docker |
| Hosting | Fly.io (1 GB RAM, 1 CPU) |

---

## Project Structure

```
├── app.py                  # Flask app, RAG chain, API routes
├── store_index.py          # One-time script: embed PDF → Pinecone
├── src/
│   ├── helper.py           # PDF loading, text splitting, embeddings
│   └── prompt.py           # LLM system prompts
├── templates/
│   └── chat.html           # Chat UI
├── static/
│   └── style.css           # Styles
├── data/
│   └── Medical_book.pdf    # Source knowledge base
├── docs/                   # Project documentation
├── Dockerfile              # Container definition
├── requirements.txt        # Python dependencies
└── .env                    # Local environment variables (not committed)
```

---

## Key Design Decisions

**In-memory chat history** — conversation context is stored in a Python list per server session. Simple and fast, but resets on restart. Suitable for a demo; a production system would persist this per user in a database.

**Top-3 retrieval** — the retriever fetches the 3 most semantically similar chunks from Pinecone for each query. This balances context richness against token cost.

**3-sentence answer limit** — the system prompt constrains the LLM to concise answers, which is appropriate for a medical context where brevity reduces the risk of misinterpretation.

**Temperature 0.2** — a low temperature is used to keep responses factual and deterministic, reducing hallucination risk for a medical domain.

**Thinking mode disabled** — Qwen3.6 27B's built-in chain-of-thought reasoning is disabled via `reasoning_effort: none` to prevent internal reasoning traces from appearing in user-facing responses.

**1 GB memory on Fly.io** — the HuggingFace embeddings model requires ~500 MB RAM to load. The Fly.io machine is configured with 1 GB to prevent OOM kills. `min_machines_running = 1` keeps the machine always warm to avoid cold-start delays.

---

## Further Reading

- [How the application works](workflow.md)
- [Deploying to Render](deployment.md)
- [FAQ](faq.md)
