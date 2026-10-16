import streamlit as st

from agents.orchestrator_agent import OrchestratorAgent
from agents.memory_logger import MemoryLogger


# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Aditi AI Twin",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------------
# Session State
# -----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------------
# Agent Initialization
# -----------------------------------

agent = OrchestratorAgent()


# -----------------------------------
# Sidebar
# -----------------------------------

with st.sidebar:

    st.title("🤖 Aditi AI Twin")

    if st.button("➕ New Chat"):

        st.session_state.messages = []

    st.divider()

    st.subheader("Agent System")

    st.success("Memory Agent")
    st.success("Personality Agent")
    st.success("Decision Agent")
    st.success("Writing Agent")

    st.divider()

    st.subheader("Modes")

    mode = st.radio(
        "Select Mode",
        [
            "Normal Twin",
            "Future Aditi"
        ]
    )

    st.divider()

    st.caption(
        "Personal AI Twin powered by GPT"
    )


# -----------------------------------
# Main Header
# -----------------------------------

st.title("🤖 Aditi Personal AI Twin")

st.markdown(
    """
Ask anything and I'll respond based on
Aditi's personality, goals, projects,
experience and learning journey.
"""
)


# -----------------------------------
# Suggested Prompts
# -----------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    if st.button(
        "📚 What should I learn next?"
    ):

        st.session_state.prompt = (
            "What should I learn next?"
        )

with col2:

    if st.button(
        "🚀 Analyze my career path"
    ):

        st.session_state.prompt = (
            "Analyze my career path"
        )

with col3:

    if st.button(
        "✉️ Write a professional email"
    ):

        st.session_state.prompt = (
            "Write a project completion email"
        )


# -----------------------------------
# Chat History Display
# -----------------------------------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# -----------------------------------
# User Prompt
# -----------------------------------

prompt = st.chat_input(
    "Ask your AI Twin anything..."
)

if "prompt" in st.session_state:

    prompt = st.session_state.prompt

    del st.session_state.prompt


# -----------------------------------
# Process Query
# -----------------------------------

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner(
            "Twin is thinking..."
        ):

            response = agent.process_query(
                prompt
            )

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    MemoryLogger.save_conversation(
        prompt,
        response
    )