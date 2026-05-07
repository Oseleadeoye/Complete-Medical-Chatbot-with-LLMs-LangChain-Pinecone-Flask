# Deploying to Render

This guide walks through deploying the Medical Chatbot to [Render](https://render.com) using Docker.

## Prerequisites

- A [Render](https://render.com) account
- Your GitHub repository connected to Render
- A [Pinecone](https://pinecone.io) account with an index named `medical-chatbot`
- A [Groq](https://console.groq.com) API key (free)

---

## Step 1 — Connect your GitHub repo

1. Log in to Render and go to **Dashboard → New → Web Service**
2. Select **Build and deploy from a Git repository**
3. Authorize Render to access your GitHub account and select this repo

---

## Step 2 — Configure the service

| Setting | Value |
|---------|-------|
| **Environment** | Docker |
| **Branch** | `main` |
| **Region** | Closest to your users |
| **Instance Type** | Starter ($7/mo) or higher — free tier may run out of memory |

Render automatically detects the `Dockerfile` at the root of the project.

---

## Step 3 — Set environment variables

In your Render service dashboard, go to **Environment** and add:

| Key | Value |
|-----|-------|
| `PINECONE_API_KEY` | Your Pinecone API key |
| `GROQ_API_KEY` | Your Groq API key |

> These are the only credentials required. No cloud provider keys needed.

---

## Step 4 — Deploy

Click **Deploy**. Render will:
1. Pull your code from GitHub
2. Build the Docker image using your `Dockerfile`
3. Start the container and expose it on a public URL

First deploy typically takes 3–5 minutes due to the HuggingFace model download.

---

## Step 5 — Subsequent deploys

Every push to `main` triggers an automatic redeploy. No manual action needed.

To trigger a manual redeploy, go to your Render service dashboard and click **Manual Deploy → Deploy latest commit**.

---

## Monitoring & Logs

- Live logs are available under the **Logs** tab in your Render dashboard
- Check startup logs to confirm the HuggingFace embeddings model loaded successfully
