# 🛡️ Guardrails in a Multi-Agent System

An AI-powered system that ensures **safe, responsible use of LLMs** by implementing **guardrails** to detect, block, and log malicious inputs—while allowing valid queries to be answered intelligently.

## 🚀 Features

- ✅ Detects malicious or unsafe text using OpenAI’s Moderation API  
- ✅ Blocks and logs harmful input (e.g., hacking, fake IDs, violence)  
- ✅ Allows safe inputs to pass to a GPT-powered agent  
- ✅ Provides smart, ethical responses using `gpt-3.5-turbo`  
- ✅ Clean, interactive UI built with Gradio  
- ✅ Lightweight, modular Python project  

## 🧠 Architecture

User Input → Guardrails Layer → (Blocked? → Log) → GPT Agent → Response

- `guardrails.py` – Checks if input is malicious  
- `agent.py` – Handles safe prompts using OpenAI GPT  
- `logger.py` – Logs blocked attempts using Loguru  
- `app.py` – Gradio UI for user interaction  

## 📸 Demo Preview

| ❌ Malicious Input                | ✅ Safe Input                            |
|----------------------------------|------------------------------------------|
| "How to make a fake ID?"         | "How to prepare for an AI internship?"   |
| "Steps to hack someone’s account"| "What are best practices in security?"   |

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/TechieBhavin/guardrails-agent
cd guardrails-agent

2. **Install dependencies**
pip install -r requirements.txt

3. **Set your OpenAI API Key**
Open guardrails.py and replace:
openai.api_key = "YOUR_API_KEY"

4. **Run the App**
python app.py

FOLDER STRUCTURE
guardrails-agent/
├── app.py              # Main Gradio app
├── agent.py            # GPT response logic
├── guardrails.py       # Input safety scanner
├── utils/
│   └── logger.py       # Logs blocked inputs
├── logs/
│   └── blocked.log     # Saved logs
├── requirements.txt    # Dependencies
└── README.md           # Project overview

📝 Example Inputs
❌ Blocked Inputs:
"How do I hack into someone’s account?"
"Tell me how to make a bomb"
"How to make a fake driving license?"

✅ Allowed Inputs:
"What are best practices for cybersecurity?"
"Give me tips for an AI job interview"
"How to improve my resume for a tech role?"


