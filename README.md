# 🤖 Question Answering Bot
<p align="center"> <img src="https://img.shields.io/badge/Transformers-HuggingFace-yellow?style=for-the-badge&logo=huggingface" /> <img src="https://img.shields.io/badge/Framework-Streamlit-ff4b4b?style=for-the-badge&logo=streamlit" /> <img src="https://img.shields.io/badge/Backend-PyTorch-red?style=for-the-badge&logo=pytorch" /> <img src="https://img.shields.io/badge/Model-DistilBERT-blue?style=for-the-badge" /> </p> <p align="center"> <b>A Transformer-based Question Answering Web App built using Hugging Face & Streamlit.</b> </p>

<br> <div align="center"> <h2>📚 Project Overview</h2> </div> <br> <div style=" background: linear-gradient(135deg,#0f2027,#203a43,#2c5364); padding:25px; border-radius:18px; box-shadow: 0px 0px 20px rgba(44,83,100,0.5); color:white; line-height:1.8; "> <h3>🤖 What is this Project?</h3>

This is a <b>Transformer-based Question Answering Web App</b>
that allows users to input any paragraph and ask questions based on that context.

The system uses a <b>pre-trained DistilBERT model</b> fine-tuned on the SQuAD dataset
to generate accurate extractive answers in real-time.

</div> <br> <div style=" background: linear-gradient(135deg,#42275a,#734b6d); padding:25px; border-radius:18px; box-shadow: 0px 0px 20px rgba(115,75,109,0.5); color:white; line-height:1.8; "> <h3>⚡ How It Works</h3>
🔹 User provides a paragraph (context)
🔹 User asks a question
🔹 The model extracts the most relevant text span
🔹 Returns the most probable answer

Model Used:
<b>distilbert-base-cased-distilled-squad</b>

</div> <br> <div style=" background: linear-gradient(135deg,#134E5E,#71B280); padding:25px; border-radius:18px; box-shadow: 0px 0px 20px rgba(113,178,128,0.5); color:white; line-height:1.8; "> <h3>🎯 Why This Project?</h3>

✔ Demonstrates NLP & Transformer knowledge
✔ Implements real-world Extractive QA
✔ Shows deployment capability with Streamlit
✔ Lightweight & fast inference

</div>
<br> <div align="center"> <h2>🚀 Features</h2> </div> <br> <div style=" background: linear-gradient(135deg,#1f4037,#99f2c8); padding:25px; border-radius:18px; box-shadow: 0px 0px 20px rgba(153,242,200,0.4); color:black; line-height:1.8; ">

✨ Custom paragraph input
❓ Ask unlimited questions
⚡ Fast DistilBERT inference
🎯 Extractive answers from context
🌐 Fully deployed Streamlit app

</div>

<br> <div align="center"> <h2>🌐 Live Demo</h2> </div> <br> <div style=" background: linear-gradient(135deg,#000428,#004e92); padding:30px; border-radius:20px; box-shadow: 0px 0px 25px rgba(0,78,146,0.6); color:white; text-align:center; line-height:1.8; "> <h3>🚀 Experience the App Live</h3>

Try the deployed Question Answering Bot and test it with your own paragraph.

<br><br>

<a href="https://qna-bot-r2mhwgbntxe8bbvdpycjye.streamlit.app/" target="_blank"> <img src="https://img.shields.io/badge/Click%20Here-Live%20App-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white"> </a>

<br><br>

✨ Built with Streamlit
🤖 Powered by DistilBERT
⚡ Real-time Transformer inference

</div>
<br> <div align="center"> <h2>🛠️ Tech Stack</h2> </div> <br> <div style=" background: linear-gradient(135deg,#232526,#414345); padding:25px; border-radius:18px; box-shadow: 0px 0px 20px rgba(65,67,69,0.5); color:white; text-align:center; "> <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python" /> <img src="https://img.shields.io/badge/Streamlit-App-ff4b4b?style=for-the-badge&logo=streamlit" /> <img src="https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=for-the-badge&logo=huggingface" /> <img src="https://img.shields.io/badge/PyTorch-Backend-ee4c2c?style=for-the-badge&logo=pytorch" /> </div>
<br> <div align="center"> <h2>📦 Installation</h2> </div> <br> <div style=" background: linear-gradient(135deg,#1f1c2c,#928DAB); padding:20px; border-radius:15px; box-shadow: 0px 0px 15px rgba(146,141,171,0.6); color:white; "> <h3>1️⃣ Clone Repository</h3> <pre> git clone https://github.com/YOUR_USERNAME/QnA-Bot.git cd QnA-Bot </pre> </div> <br> <div style=" background: linear-gradient(135deg,#0f2027,#203a43,#2c5364); padding:20px; border-radius:15px; box-shadow: 0px 0px 15px rgba(44,83,100,0.6); color:white; "> <h3>2️⃣ Create Virtual Environment</h3> <pre> python -m venv venv venv\Scripts\activate </pre> </div> <br> <div style=" background: linear-gradient(135deg,#42275a,#734b6d); padding:20px; border-radius:15px; box-shadow: 0px 0px 15px rgba(115,75,109,0.6); color:white; "> <h3>3️⃣ Install Dependencies</h3> <pre> pip install -r requirements.txt </pre> </div> <br> <div style=" background: linear-gradient(135deg,#134E5E,#71B280); padding:20px; border-radius:15px; box-shadow: 0px 0px 15px rgba(113,178,128,0.6); color:white; "> <h3>▶️ Run the Application</h3> <pre> streamlit run qa_app.py </pre> </div>
<br> <div align="center"> <h2>🧩 Future Improvements</h2> </div> <br> <div style=" background: linear-gradient(135deg,#3a1c71,#d76d77,#ffaf7b); padding:25px; border-radius:18px; box-shadow: 0px 0px 20px rgba(215,109,119,0.5); color:white; line-height:1.8; ">

🔄 Add conversational memory
📄 PDF document upload support
🔍 Multi-document QA
🧠 Upgrade to LLM-based generative answers
⚙️ Performance optimization & caching

</div>
<br> <div align="center">

⭐ If you like this project, consider giving it a star!

</div>
