import streamlit as st
from dotenv import load_dotenv
from langchain_openai import OpenAI
from utils import query_agent

load_dotenv()

llm = OpenAI(temperature=0)

st.title("💬 Talk with your CSV file")
st.header("Upload your CSV file:")

data = st.file_uploader("Upload your CSV file", type=["csv"])

# query = st.text_area("Enter your query", height=100)
# submit = st.button("Submit")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello, how can I help you today?"}]

def show_messages():
    for msg in st.session_state.messages:
        st.chat_message(msg['role']).write(msg["content"])

show_messages()

if query := st.chat_input():
    if data is not None: 
        st.session_state.messages.append({"role": "user", "content": query})
        st.chat_message("user").write(query)
        response = query_agent(data, llm, query)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)