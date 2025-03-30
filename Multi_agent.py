import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv

class SentimentChatbot:
    def __init__(self):
        self.model_api = "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"
        self.llm = ChatGroq(groq_api_key=self.model_api, model_name="llama-3.3-70b-versatile")
        
    def analyze_sentiment(self, user_input):
        prompt = f"""
        Analyze the sentiment of the following text and classify it into one of the three categories:
        1. Worse
        2. Middle Range
        3. Pretty Good
        Additionally, identify and describe the emotional cues associated with the user’s sentiment.
        Text: {user_input}
        """
        response = self.llm.invoke([{"role": "user", "content": prompt}])
        return response.content

    def provide_advice(self, user_input, sentiment_analysis):
        prompt = f"""
        You are a good friend, but your friend is suffering from the following problem:
        Problem: {user_input}
        And he/she has the following emotions, so give him/her good advice and a list of good solutions:
        Emotions: {sentiment_analysis}
        """
        response = self.llm.invoke([{"role": "user", "content": prompt}])
        return response.content


st.set_page_config(page_title="ArogyaBharat", layout="centered")
st.title("ArogyaBharat")

bot = SentimentChatbot()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("Start New Chat"):
    st.session_state.chat_history = []
    st.success("New chat session started!")

with st.form("chat_form"):
    user_input = st.text_area("How are you feeling today?", "")
    submit = st.form_submit_button("Send")

if submit and user_input.strip():
    sentiment_analysis = bot.analyze_sentiment(user_input)
    advice = bot.provide_advice(user_input, sentiment_analysis)
    
    st.session_state.chat_history.append((user_input, sentiment_analysis, advice))
    
    st.subheader("ArogyaBharat:")
    st.write(advice)

st.subheader("Chat History")
for idx, (user_msg, sentiment, advice) in enumerate(st.session_state.chat_history[::-1]):
    with st.expander(f"Previous Conversation {idx+1}"):
        st.write(f"**ArogyaBharat:** {advice}")
