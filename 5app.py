# Step 1: Import libraries
import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Step 2: Load API key
load_dotenv()

# Step 3: Application title
st.title("AI Chatbot with Memory")

# Step 4: Initialize LLM
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.5
)

# Step 5: Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Step 6: Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Step 7: Accept user input
question = st.chat_input("Ask me anything")

if question:

    # Step 8: Display user message
    with st.chat_message("user"):
        st.write(question)

    # Step 9: Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    # Step 10: Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.invoke(
                st.session_state.messages
            )
            st.write(response.content)

    # Step 11: Store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response.content
    })