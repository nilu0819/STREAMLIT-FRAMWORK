# Step 1: Import libraries
import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Step 2: Load API key
load_dotenv()

# Step 3: Page configuration
st.set_page_config(
    page_title="AI Application",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("My AI Application")

# Step 4: Sidebar
st.sidebar.title("Settings")

selected_model = st.sidebar.selectbox(
    "Select Model",
    ["openai/gpt-oss-120b", "llama-3.1-8b-instant"]
)

temperature = st.sidebar.slider(
    "Temperature", 0.0, 1.0, 0.5
)

# Step 5: Create LLM
model = ChatGroq(
    model=selected_model,
    temperature=temperature
)

# Step 6: Create columns
col1, col2 = st.columns(2)

with col1:
    st.header("User Input")
    question = st.text_area("Enter your question")

with col2:
    st.header("AI Response")

    if st.button("Generate"):
        if question.strip():
            with st.spinner("Generating answer..."):
                response = model.invoke(question)
                st.write(response.content)
        else:
            st.warning("Please enter a question.")