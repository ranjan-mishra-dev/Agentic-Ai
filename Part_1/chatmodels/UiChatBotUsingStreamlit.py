import streamlit as st
from dotenv import load_dotenv

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage
)
from langchain.chat_models import init_chat_model


# Load environment variables
load_dotenv()


# -----------------------------
# Model
# -----------------------------

model = init_chat_model("gpt-5.4-mini")


# -----------------------------
# System Prompt
# -----------------------------

sys_msg = SystemMessage(
    content="""
    You are the best physics teacher in the world.

    Teach every concept like you are teaching a child.

    For every question:
    1. Give a simple definition.
    2. Explain the concept clearly.
    3. Give an example.
    4. Explain real-world use cases when appropriate.
    """
)


# -----------------------------
# Streamlit UI
# -----------------------------

st.title("🤖 Physics AI Teacher")

st.write(
    "Ask me anything about Physics!"
)


# -----------------------------
# Chat History
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = [sys_msg]


# -----------------------------
# Display previous messages
# -----------------------------

for message in st.session_state.messages:

    if isinstance(message, HumanMessage):

        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):
            st.write(message.content)


# -----------------------------
# User Input
# -----------------------------

user_input = st.chat_input(
    "Ask a physics question..."
)


if user_input:

    # Add user message
    human_msg = HumanMessage(content=user_input)

    st.session_state.messages.append(human_msg)

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)


    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = model.invoke(
                st.session_state.messages
            )

        st.write(response.content)


    # Store AI response
    st.session_state.messages.append(
        AIMessage(content=response.content)
    )