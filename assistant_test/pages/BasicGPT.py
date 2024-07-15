import time
import streamlit as st

from agent import chain_basic

# ------------------------------------------------------------
# Config
# ------------------------------------------------------------
st.set_page_config(
    page_title="BasicGPT",
    page_icon="🤖",
)
st.title("🤖 BasicGPT")

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
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "human", "message": user_message})
    
    # Display user message in chat message container
    with st.chat_message("human"):
        st.markdown(user_message)
    
    # Display assistant response in chat message container
    with st.chat_message("ai"):
        message_placeholder = st.empty()
        full_response = ""
               
        # Get assistant response
        with st.spinner("Thinking..."):
            response = chain_basic.invoke({"message": user_message})
            print(response)
            
        for chunk in response["text"].split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "ai", "message": full_response})
