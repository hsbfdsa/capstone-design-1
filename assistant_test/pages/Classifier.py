import time
import streamlit as st

from agent import chain_clf

# ------------------------------------------------------------
# Config
# ------------------------------------------------------------
st.set_page_config(
    page_title="ClassifyGPT",
    page_icon="🤖",
)
st.title("🤖 ClassifyGPT")

# ------------------------------------------------------------
# Initialize chat history
# ------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# ------------------------------------------------------------
# Display chat messages from history on app rerun
# ------------------------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["message"])
    
# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
if user_message := st.chat_input("Ask anything here!"):
    
    # Add user message to chat history'
    st.session_state.messages.append({"role": "human", "message": user_message})
    
    # Display user message in chat message container
    with st.chat_message("human"):
        st.markdown(user_message)
        
    # Get result of classification from assistant response
    with st.spinner("Thinking..."):
        response = chain_clf.invoke({"message": user_message})
        result = response["text"]
    
    # Display assistant response in chat message container
    with st.chat_message("ai"):
        st.markdown(result)                  
            
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "ai", "message": result})