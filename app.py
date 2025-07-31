import gradio as gr
from guardrails import is_malicious_text
from agent import ask_agent
from utils.logger import logger

def main(user_input):
    if is_malicious_text(user_input):
        logger.warning(f"Blocked input: {user_input}")
        return "❌ Input blocked due to unsafe content."
    else:
        response = ask_agent(user_input)
        return response

iface = gr.Interface(fn=main, inputs="text", outputs="text", title="Secure AI Agent")
iface.launch()
