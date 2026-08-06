import streamlit as st
import requests
import os

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

st.set_page_config(page_title="Medical RAG Assistant", page_icon="🩺")
st.title(" Medical RAG Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Ask a medical question..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Retrieving medical context & generating answer..."):
            try:
                res = requests.post(f"{API_BASE_URL}/query", json={"question": user_input})
                if res.status_code == 200:
                    data = res.json()
                    answer = data["answer"]
                    sources = data["sources"]
                    
                    st.markdown(answer)
                    with st.expander("Source Context"):
                        for idx, src in enumerate(sources, 1):
                            st.write(f"**Source Chunk {idx}:** {src}")
                else:
                    st.error("Error received from Backend API.")
            except Exception as e:
                st.error(f"Failed to connect to backend server: {e}")

    st.session_state.messages.append({"role": "assistant", "content": answer})