# Step 1: Import libraries
import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Step 2: Load API key
load_dotenv()

# Step 3: Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Step 4: Application title
st.title("My AI Chatbot")

# Step 5: Create sidebar
st.sidebar.title("Settings")

selected_model = st.sidebar.selectbox(
    "Select Model",
    ["openai/gpt-oss-120b", "llama-3.1-8b-instant"]
)

temperature = st.sidebar.slider(
    "Temperature", 0.0, 1.0, 0.5
)

# Step 6: Initialize LLM
model = ChatGroq(
    model=selected_model,
    temperature=temperature
)

# Step 7: Accept user input
question = st.chat_input("Ask me anything")

# Step 8: Process user input
if question:

    with st.chat_message("user"):
        st.write(question)

    # Step 9: Generate and display response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):
            response = model.invoke(question)
            st.write(response.content)