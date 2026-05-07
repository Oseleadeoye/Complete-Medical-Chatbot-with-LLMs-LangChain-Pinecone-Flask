# Deploying to Fly.io

This guide walks through deploying the Medical Chatbot to [Fly.io](https://fly.io) using Docker.

**Live deployment:** https://medical-chatbot.fly.dev/

## Prerequisites

- A [Fly.io](https://fly.io) account (free, credit card required for verification — no charges on free tier)
- `flyctl` installed: `powershell -ExecutionPolicy ByPass -Command "iwr https://fly.io/install.ps1 -useb | iex"`
- A [Pinecone](https://pinecone.io) account with an index named `medical-chatbot`
- A [Groq](https://console.groq.com) API key (free)

---

## Step 1 — Log in to Fly.io

```bash
fly auth login
```

---

## Step 2 — Create the app

```bash
fly apps create medical-chatbot
```

---

## Step 3 — Set environment variables

```bash
fly secrets set PINECONE_API_KEY=your_key GROQ_API_KEY=your_key
```

---

## Step 4 — Deploy

```bash
fly deploy
```

Fly.io will build the Docker image and launch the app. First deploy takes 3–5 minutes.

Your app will be live at `https://<app-name>.fly.dev/`.

---

## Step 5 — Scale to 1 machine (recommended)

The default deploys 2 machines for high availability. On the free tier, scale to 1 to avoid OOM crashes:

```bash
fly scale count 1 --yes
```

---

## Step 6 — Subsequent deploys

Every time you push changes, redeploy with:

```bash
fly deploy
```

---

## Monitoring & Logs

```bash
fly logs
```

Live logs are also available at [fly.io/apps/medical-chatbot/monitoring](https://fly.io/apps/medical-chatbot/monitoring).
