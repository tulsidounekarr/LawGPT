import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
import os

# =========================
# 🔹 PAGE CONFIG
# =========================
st.set_page_config(page_title="LawGPT", layout="wide")

# =========================
# 🔹 TITLE
# =========================
st.title("⚖️ LawGPT - Legal Chatbot")

# =========================
# 🔹 SIDEBAR
# =========================
st.sidebar.title("LawGPT")

st.sidebar.write("AI-powered legal assistant using LLaMA 3")

st.sidebar.write("### How to use:")
st.sidebar.write("1. Enter your legal question")
st.sidebar.write("2. Press Enter")
st.sidebar.write("3. Get AI-powered answer")

st.sidebar.markdown("---")

st.sidebar.write("👨‍💻 Developed by Tulsi")

# Clear Chat Button
if st.sidebar.button("Clear Chat"):
    st.session_state.clear()

# =========================
# 🔹 LOAD DOCUMENTS
# =========================
def load_documents():
    docs = []
    for file in os.listdir("data"):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(f"data/{file}")
            docs.extend(loader.load())
    return docs

# =========================
# 🔹 CACHE VECTORSTORE
# =========================
@st.cache_resource
def get_vectorstore():
    documents = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)
    chunks = chunks[:200]  # limit for speed

    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)

    return vectorstore

# Load vectorstore (cached)
vectorstore = get_vectorstore()

# =========================
# 🔹 GROQ LLM
# =========================
import os

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

# =========================
# 🔹 ASK FUNCTION
# =========================
def ask_question(query):
    docs = vectorstore.similarity_search(query)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer the legal question based on the context below:
    {context}

    Question: {query}
    """

    response = llm.invoke(prompt)
    return response.content

# =========================
# 🔹 CHAT HISTORY
# =========================
if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# 🔹 INPUT BOX
# =========================
query = st.text_input("Ask your legal question:", key="user_input")

# =========================
# 🔹 PROCESS QUERY
# =========================
if query:
    with st.spinner("Thinking..."):
        answer = ask_question(query)
        st.session_state.history.append((query, answer))

# =========================
# 🔹 DISPLAY CHAT
# =========================
for q, a in st.session_state.history:
    st.markdown(f"**🧑‍💻 You:** {q}")
    st.markdown(f"**🤖 LawGPT:** {a}")
    st.markdown("---")