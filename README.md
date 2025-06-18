# 🤖 Question Answering Bot

A simple Question Answering (QA) app built using [Hugging Face Transformers](https://huggingface.co/transformers/) and [Streamlit](https://streamlit.io/).  
You can input any paragraph and ask questions about it — the bot will return answers using a pre-trained Transformer model.

---

## 🚀 Features

- Input a custom paragraph or article.
- Ask any question related to the paragraph.
- Uses `distilbert-base-cased-distilled-squad` for answering.
- Fast, responsive Streamlit UI.

---

## 🛠️ Tech Stack

- Python 3.8+
- Streamlit
- Hugging Face Transformers
- PyTorch (for model backend)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/qa-bot.git
cd qa-bot


2. Create a Virtual Environment (Windows)

python -m venv venv
venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

▶️ Run the App

streamlit run qa_app.py

Deployed using Streamlit
LIVE DEMO[https://qna-bot-r2mhwgbntxe8bbvdpycjye.streamlit.app/]
