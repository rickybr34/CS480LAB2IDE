---
title: Arxiv Agent Lab
emoji: 🔥
colorFrom: pink
colorTo: yellow
sdk: gradio
sdk_version: 6.27.0
python_version: '3.12'
app_file: app.py
pinned: false
license: mit
short_description: Agentic AI Lab
---

# Arxiv Agent Lab

## How to run (on your computer)

### 1. Put your Hugging Face token in a file

Create a file called `keys.env` in this project

Inside that file, put one line:

```
HF_TOKEN=hf_your_token_here
```

(Get a token from https://huggingface.co/settings/tokens)

### 2. Install the libraries (one time)

Open a terminal in this folder and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Start the app

```bash
source .venv/bin/activate
python app.py
```

### 4. Open it in your browser

Look in the terminal for a link like `http://127.0.0.1:7860` and open it.

Then try asking:

> Find 2 recent papers on Neural Stochastic Differential Equations and format them as BibTeX.
