# Frequently Asked Questions

---

**Why does the app take a long time to start?**

On first startup, the HuggingFace model (`all-MiniLM-L6-v2`) is downloaded from the internet. This can take 1–2 minutes. Subsequent starts are faster as the model is cached inside the container.

---

**Do I need to run `store_index.py` every time?**

No. Run it once to populate your Pinecone index. Only re-run it if you change or replace `data/Medical_book.pdf`.

---

**The chatbot says it doesn't know the answer — why?**

The chatbot only answers based on content in the indexed PDF. If the question is outside the scope of `Medical_book.pdf`, it will say it doesn't know. This is by design to prevent hallucinations.

---

**Can I use a different PDF?**

Yes. Replace `data/Medical_book.pdf` with your own PDF, then re-run `store_index.py` to re-index the content. Make sure your Pinecone index is cleared first or use a different index name.

---

**Can I use a different model?**

Yes. In `app.py`, change the model name in:
```python
chatModel = ChatGroq(model="qwen/qwen3.6-27b")
```
to any model supported by Groq, e.g. `openai/gpt-oss-120b` or `llama3-8b-8192`. See the full list at [console.groq.com/docs/models](https://console.groq.com/docs/models).

---

**Why is the chat history lost when the app restarts?**

Chat history is stored in memory (`chat_history` list in `app.py`). It resets on every restart. For persistent history, you would need to integrate a database or session store.

---

**My Pinecone connection is failing — what do I check?**

1. Confirm `PINECONE_API_KEY` is set correctly in your `.env` or Render environment variables
2. Confirm the index name in `app.py` matches your actual Pinecone index (`medical-chatbot` by default)
3. Confirm the index dimension is `384` (matching the `all-MiniLM-L6-v2` embeddings model)

---

**The deployed app shows a 502 error or takes a very long time to load — why?**

There are two common causes:

1. **Out-of-Memory (OOM) crash** — The HuggingFace `all-MiniLM-L6-v2` model requires ~500 MB RAM just to load. If the Fly.io machine has less than 1 GB memory, the Linux OOM killer will terminate the Python process during startup, causing 502 errors. The `fly.toml` is configured with `memory = "1gb"` to prevent this.

2. **Cold start** — If `min_machines_running = 0`, the machine shuts down after periods of inactivity. The next visitor triggers a cold boot (pulling the Docker image, loading embeddings), which takes 20–40 seconds before the app is reachable. `min_machines_running = 1` is set to keep the machine always warm.

---

**What is the cost to run this?**

- **Groq API:** Free tier includes generous rate limits, more than enough for a demo or portfolio project.
- **Pinecone:** The free Starter plan supports one index and is sufficient for this project.
- **HuggingFace embeddings:** Free. The model runs locally after the initial download.
- **Fly.io:** The 1 GB / 1 CPU machine with `min_machines_running = 1` stays within the Fly.io free tier allowance (3 shared-CPU-1x 256 MB machines free, or equivalent compute hours).
