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

**Can I use a different Ollama model?**

Yes. In `app.py`, change:
```python
chatModel = ChatOllama(model="llama3")
```
to any model you have pulled locally, e.g. `mistral`, `llama3.2`, or `phi3`. Pull a model with `ollama pull <model-name>`.

---

**Why is the chat history lost when the app restarts?**

Chat history is stored in memory (`chat_history` list in `app.py`). It resets on every restart. For persistent history, you would need to integrate a database or session store.

---

**My Pinecone connection is failing — what do I check?**

1. Confirm `PINECONE_API_KEY` is set correctly in your `.env` or Render environment variables
2. Confirm the index name in `app.py` matches your actual Pinecone index (`medical-chatbot` by default)
3. Confirm the index dimension is `384` (matching the `all-MiniLM-L6-v2` embeddings model)

---

**What is the cost to run this?**

- **Ollama + Llama 3:** Free. Runs entirely on your local machine — no API costs.
- **Pinecone:** The free Starter plan supports one index and is sufficient for this project.
- **HuggingFace embeddings:** Free. The model runs locally after the initial download.
