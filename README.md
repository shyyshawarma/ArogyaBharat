# 🧘 ArogyaBharat - Mental Wellness Chatbot  

ArogyaBharat is an AI-powered mental wellness chatbot built with **Streamlit** and **Groq's Llama 3.3-70B**.  
It helps users by analyzing their sentiments, providing emotional support, and offering personalized advice.  

## ✨ Features  
✔ **Sentiment Analysis** – Classifies user emotions into three categories (Worse, Middle Range, Pretty Good).  
✔ **Multilingual Support** –Main reason to use LLAMA models is for multilingual support as they are trained on a variety of languages.  
✔ **Minority checker** –Uses RAG to check whether the person is suffering from a specific discrimination or not.  
✔ **ERS** –incase of very severe conditions it will run and emergency SOS. 
✔ **AI-Powered Advice** – Offers personalized support and solutions based on user sentiment.  
✔ **Modern UI/UX** – Clean, responsive design with a user-friendly experience.  
✔ **Chat History** – View past conversations for reference.  
✔ **New Chat Option** – Start fresh conversations anytime.  

## 🚀 Tech Stack  
### 💻 Frontend  
- **Streamlit** – Interactive UI for chatbot conversation.  
- **Custom CSS** – Enhanced UI styling for a modern look.  

### 🧠 AI & NLP  
- **Groq's Llama 3.3-70B** – Large Language Model for sentiment analysis and advice generation.  
- **LangChain** – API wrapper for handling LLM interactions.  

### 🏗️ Backend  
- **Python** – Core programming language.  
- **FastAPI (Optional)** – Can be integrated for API-based backend support.  

### 📦 Deployment & DevOps  
- **Docker** – Containerization for deployment.  
- **Streamlit Sharing / Hugging Face Spaces** – Potential hosting platforms.  
- **GitHub Actions** – CI/CD automation for updates.  

### 📊 Data Handling  
- **Session State (Streamlit)** – Stores chat history for user sessions.  
- **ChromaDB (Optional)** – Can be integrated for advanced conversational memory.  

## 📦 Installation  
```bash
git clone https://github.com/yourusername/ArogyaBharat.git
cd ArogyaBharat
pip install -r requirements.txt
streamlit run app.py
