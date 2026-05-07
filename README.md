# Complete Medical Chatbot with LLMs, LangChain, Pinecone & Flask

A conversational AI assistant that answers medical questions using Retrieval-Augmented Generation (RAG). Built with LangChain, Llama 3 (via Ollama), Pinecone, and Flask — runs entirely locally at no cost.

---

## Documentation

- [Project Overview](docs/overview.md) — what it is, tech stack, design decisions
- [How It Works](docs/workflow.md) — architecture, data flow, key files
- [Deploying to Render](docs/deployment.md) — step-by-step deployment guide
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

### 4. Install Ollama and pull Llama 3

Download Ollama from [ollama.com](https://ollama.com), then run:

```bash
ollama pull llama3
```

Keep Ollama running in the background — it starts automatically on most installs.

### 5. Add your Pinecone API key

Create a `.env` file in the root directory:

```ini
PINECONE_API_KEY = "your-pinecone-api-key"
```

### 6. Index the knowledge base (first time only)

```bash
python store_index.py
```

### 7. Run the app

```bash
python app.py
```

Open `http://localhost:8080` in your browser.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Web framework | Flask |
| LLM | Llama 3 (via Ollama, runs locally) |
| Embeddings | HuggingFace `all-MiniLM-L6-v2` |
| Vector database | Pinecone |
| RAG orchestration | LangChain |
| Containerisation | Docker |
