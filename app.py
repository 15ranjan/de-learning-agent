import streamlit as st
from agent import run_agent

st.title("🤖 DE Learning Agent")
st.caption("Your personal Data Engineering mentor")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Input box at bottom
if question := st.chat_input("Ask me anything about Data Engineering..."):
    
    # Show your question
    with st.chat_message("user"):
        st.write(question)
    st.session_state.messages.append({"role": "user", "content": question})
    
    # Get agent response
    with st.spinner("Thinking..."):
        response = run_agent(question)
    
    # Show agent response
    with st.chat_message("assistant"):
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})