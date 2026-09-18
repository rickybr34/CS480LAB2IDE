import os
from pathlib import Path

import gradio as gr
from smolagents import CodeAgent, InferenceClientModel

from tools import search_arxiv


def load_hf_token() -> str | None:
    """Prefer HF_TOKEN from the environment; otherwise read ../keys.env or .env."""
    token = os.environ.get("HF_TOKEN")
    if token:
        return token

    for candidate in (
        Path(__file__).resolve().parent.parent / "keys.env",
        Path(__file__).resolve().parent / ".env",
        Path(__file__).resolve().parent / "keys.env",
    ):
        if not candidate.is_file():
            continue
        for line in candidate.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            if key.strip() == "HF_TOKEN":
                return value.strip().strip('"').strip("'")
    return None


# Load your Hugging Face API token (needed to call Qwen online)
hf_token = load_hf_token()
if not hf_token:
    raise SystemExit(
        "HF_TOKEN not found. Set it in the environment or put it in ../keys.env"
    )

# 1. Initialize Qwen 2.5 Coder via the Serverless API
model = InferenceClientModel(
    model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
    token=hf_token,
)

# 2. Assemble the CodeAgent (registers our arXiv search tool)
agent = CodeAgent(
    tools=[search_arxiv],
    model=model,
    add_base_tools=False,
    max_steps=5,
)

# 3. Define the chat function that runs the agent on the user's prompt
def agent_chat(user_prompt: str):
    return agent.run(user_prompt)

# 4. Launch the Gradio Chat Interface
demo = gr.Interface(
    fn=agent_chat,
    inputs=gr.Textbox(
        lines=2,
        placeholder="E.g., Find 2 recent papers on Agentic AI and format them as BibTeX.",
    ),
    outputs=gr.Markdown(label="Agent Output"),
    title="Autonomous arXiv Research Agent",
    description="Powered by smolagents and Qwen 2.5 Coder (local Gradio)",
)

if __name__ == "__main__":
    # Runs on your computer only (opens a local link in the terminal)
    demo.launch(server_name="127.0.0.1", share=False)
