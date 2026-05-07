# Complete Medical Chatbot with LLMs, LangChain, Pinecone & Flask


# How to run?
### STEPS:

Clone the repository

```bash
git clone https://github.com/Oseleadeoye/Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask.git
```

### STEP 01 - Create a conda environment after opening the repository

```bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
```


### STEP 02 - Install the requirements

```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone & OpenAI credentials:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# Run the following command to store embeddings to Pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now open `http://localhost:8080` in your browser.


### Tech Stack:

- Python
- LangChain
- Flask
- GPT-4o
- Pinecone



# Deployment on Render (with GitHub Actions CI/CD)

## 1. Create a Render account

Sign up at [render.com](https://render.com).

## 2. Create a new Web Service

1. Go to **Dashboard → New → Web Service**
2. Connect your GitHub repository
3. Render will automatically detect the `Dockerfile`
4. Set the following:
   - **Environment:** Docker
   - **Branch:** `main`
   - **Region:** Choose one closest to your users

## 3. Set environment variables in Render

In your Render service dashboard go to **Environment** and add:

| Key | Value |
|-----|-------|
| `PINECONE_API_KEY` | your Pinecone API key |
| `OPENAI_API_KEY` | your OpenAI API key |

## 4. Deploy

Click **Deploy**. Render will build the Docker image and start the service.

Every subsequent push to `main` will trigger an automatic redeploy.

## 5. Set up GitHub Actions (optional CI step)

If you want to run tests or checks before Render deploys, add a `.github/workflows/ci.yaml`:

```yaml
name: CI

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Build Docker image
        run: docker build -t medical-chatbot .
```

Render's GitHub integration handles the actual deployment automatically after CI passes.

## 6. GitHub Secrets required

Only your API keys are needed — no cloud provider credentials:

- `PINECONE_API_KEY`
- `OPENAI_API_KEY`
