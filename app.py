import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"  # FastAPI server URL

st.title("CSV Chatbot with RAG")

# File Upload Section
st.header("Upload CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if st.button("Upload File") and uploaded_file:
    files = {"file": uploaded_file}
    response = requests.post(f"{BASE_URL}/upload", files=files)
    if response.status_code == 200:
        st.success("File uploaded successfully!")
    else:
        st.error(f"Error: {response.json()['detail']}")

# List Files Section
st.header("Available Files")
response = requests.get(f"{BASE_URL}/files")
if response.status_code == 200:
    files = response.json()["files"]
    file_options = {f"{file['file_name']}": file["file_id"] for file in files}
    selected_file = st.selectbox("Select a file to query:", list(file_options.keys()))
    file_id = file_options[selected_file] if selected_file else None
else:
    st.error("Failed to retrieve files")

# Query Section
st.header("Ask Questions About Your CSV")
user_query = st.text_input("Enter your query")

if st.button("Submit Query") and user_query and file_id:
    query_payload = {"file_id": file_id, "query": user_query}
    response = requests.post(f"{BASE_URL}/query", json=query_payload)
    if response.status_code == 200:
        st.write("### Response:")
        st.write(response.json()["response"])
    else:
        st.error(f"Error: {response.json()['detail']}")
