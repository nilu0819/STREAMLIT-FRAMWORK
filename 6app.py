# STEP 1: IMPORT REQUIRED LIBRARIES

# Streamlit is used to create the web application
import streamlit as st

# ChatGroq connects our application to the LLM
from langchain_groq import ChatGroq

# load_dotenv loads the API key from the .env file
from dotenv import load_dotenv


# STEP 2: LOAD API KEY

# Load environment variables from the .env file
load_dotenv()


# STEP 3: CREATE APPLICATION TITLE

# Display the main heading on the webpage
st.title("AI Chatbot with Memory")


# STEP 4: INITIALIZE THE LLM

# Create an AI model using ChatGroq
model = ChatGroq(

    # Select the AI model
    model="openai/gpt-oss-120b",

    # Control the randomness of the response
    temperature=0.5
)


# STEP 5: INITIALIZE CONVERSATION HISTORY

# Check whether the messages variable already exists
# inside the session state
if "messages" not in st.session_state:

    # If it does not exist, create an empty list
    # This list will store user and assistant messages
    st.session_state.messages = []


# STEP 6: CREATE SIDEBAR

# Display the Settings heading inside the sidebar
st.sidebar.title("Settings")


# STEP 7: CREATE CLEAR CHAT BUTTON

# Check whether the user clicks the Clear Chat button
if st.sidebar.button("Clear Chat"):

    # Remove all previously stored messages
    st.session_state.messages = []

    # Restart the script to refresh the interface
    st.rerun()


# STEP 8: DISPLAY PREVIOUS CONVERSATIONS

# Retrieve each message from the conversation history
for message in st.session_state.messages:

    # Create a chat container based on the message role
    # The role can be user or assistant
    with st.chat_message(message["role"]):

        # Display the actual message content
        st.write(message["content"])


# STEP 9: ACCEPT USER INPUT

# Create a chat input box
# Store the submitted message in the question variable
question = st.chat_input("Ask me anything")


# Check whether the user has submitted a message
if question:

    # STEP 10: DISPLAY USER MESSAGE

    # Create a user message container
    with st.chat_message("user"):

        # Display the user's question
        st.write(question)


    # STEP 11: STORE USER MESSAGE

    # Add the user's question to the conversation list
    st.session_state.messages.append({

        # Identify the sender as the user
        "role": "user",

        # Store the actual question
        "content": question
    })


    # STEP 12: GENERATE AI RESPONSE

    # Create an assistant message container
    with st.chat_message("assistant"):

        # Display a loading indicator
        with st.spinner("Thinking..."):

            # Send the entire conversation history
            # to the LLM to generate a contextual answer
            response = model.invoke(
                st.session_state.messages
            )

            # Extract and display the generated answer
            st.write(response.content)


    # STEP 13: STORE ASSISTANT RESPONSE

    # Add the generated answer to conversation history
    st.session_state.messages.append({

        # Identify the sender as the assistant
        "role": "assistant",

        # Store the generated AI answer
        "content": response.content
    })