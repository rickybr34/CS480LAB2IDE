import os
import gradio as gr
import spaces
from smolagents import CodeAgent, InferenceClientModel
from tools import search_arxiv

# 1. Initialize Qwen 2.5 Coder via the Serverless API
model = InferenceClientModel(
    model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
    token=os.environ.get("HF_TOKEN")
)

# 2. Assemble the CodeAgent
agent = CodeAgent(
    tools=[search_arxiv], 
    model=model,
    add_base_tools=False,
    max_steps=5
)

# 3. Define the execution function and request ZeroGPU allocation
@spaces.GPU
def agent_chat(user_prompt):
    return agent.run(user_prompt)

# 4. Launch the Gradio Chat Interface
demo = gr.Interface(
    fn=agent_chat,
    inputs=gr.Textbox(lines=2, placeholder="E.g., Find 2 recent papers on Agentic AI and format them as BibTeX."),
    outputs=gr.Markdown(label="Agent Output"),
    title="Autonomous arXiv Research Agent",
    description="Powered by smolagents and Qwen 2.5 Coder"
)

demo.launch()
