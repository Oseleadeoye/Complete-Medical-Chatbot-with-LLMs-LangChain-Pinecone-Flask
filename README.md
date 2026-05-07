# Complete Medical Chatbot with LLMs, LangChain, Pinecone & Flask

A conversational AI assistant that answers medical questions using Retrieval-Augmented Generation (RAG). Built with LangChain, Llama 3.3 (via Groq), Pinecone, and Flask — deployable to the cloud at no cost.

**Live demo:** https://medical-chatbot.fly.dev/

---

## Documentation

- [Project Overview](docs/overview.md) — what it is, tech stack, design decisions
- [How It Works](docs/workflow.md) — architecture, data flow, key files
- [Deploying to Fly.io](docs/deployment.md) — step-by-step deployment guide
- [FAQ](docs/faq.md) — common questions and troubleshooting

---

## Quickstart

### 1. Clone the repo

```bash
git clone https://github.com/Oseleadeoye/Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask.git
cd Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask
```

### 2. Create and activate a conda environment

```bash
conda create -n medibot python=3.10 -y
conda activate medibot
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API keys

Create a `.env` file in the root directory:

```ini
PINECONE_API_KEY=your-pinecone-api-key
GROQ_API_KEY=your-groq-api-key
```

Get a free Groq API key at [console.groq.com](https://console.groq.com).

### 5. Index the knowledge base (first time only)

```bash
python store_index.py
```

### 6. Run the app

```bash
python app.py
```

Open `http://localhost:8080` in your browser.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Web framework | Flask |
| LLM | Llama 3.3 70B (via Groq API, free tier) |
| Embeddings | HuggingFace `all-MiniLM-L6-v2` |
| Vector database | Pinecone |
| RAG orchestration | LangChain |
| Containerisation | Docker |
