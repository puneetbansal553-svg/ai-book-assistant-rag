import os
import shutil
import gc
from dotenv import load_dotenv

import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(
    page_title="📚 AI Book Assistant",
    page_icon="📖",
    layout="wide"
)

# ---------------------- CSS ----------------------

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.stChatMessage{
    border-radius:15px;
    padding:10px;
}

.uploadBox{
    border:2px dashed #4CAF50;
    padding:20px;
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------- Models ----------------------

@st.cache_resource
def load_embedding():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


@st.cache_resource
def load_llm():
    return ChatMistralAI(
        model="mistral-small-2506"
    )


embedding_model = load_embedding()
llm = load_llm()

prompt = ChatPromptTemplate.from_messages([
(
"system",
"""
You are a helpful AI assistant.

Use ONLY the provided context.

If the answer is not present say:

I could not find the answer in the document.
"""
),
(
"human",
"""
Context:
{context}

Question:
{question}
"""
)
])

UPLOAD_DIR = "uploads"
DB_DIR = "chroma-db"

os.makedirs(UPLOAD_DIR, exist_ok=True)

# ---------------------- Sidebar ----------------------

with st.sidebar:

    st.title("📚 Book Manager")

    uploaded_files = st.file_uploader(
        "Upload PDF Books",
        type="pdf",
        accept_multiple_files=True
    )

    if st.button("📥 Create / Update Database"):

        if uploaded_files:

            docs = []

            for file in uploaded_files:

                save_path = os.path.join(
                    UPLOAD_DIR,
                    file.name
                )

                with open(save_path, "wb") as f:
                    f.write(file.getbuffer())

                loader = PyPDFLoader(save_path)
                docs.extend(loader.load())

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )

            chunks = splitter.split_documents(docs)

            st.cache_resource.clear()
            gc.collect()

            if os.path.exists(DB_DIR):
                try:
                    shutil.rmtree(DB_DIR)
                except PermissionError:
                    st.error(
                        "Database is currently in use. Please refresh the page and try again."
                    )
                    st.stop()

            Chroma.from_documents(
                documents=chunks,
                embedding=embedding_model,
                persist_directory=DB_DIR
            )

            st.success("Database Created Successfully!")

        else:
            st.warning("Upload PDFs first.")

    st.divider()

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------------- Main ----------------------

st.title("📖 AI Book Assistant")

st.caption("Ask questions from your uploaded books.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input("Ask something...")

if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    if not os.path.exists(DB_DIR):

        answer = "Please upload PDF(s) and create the database first."

    else:

        vectorstore = Chroma(
            persist_directory=DB_DIR,
            embedding_function=embedding_model
        )

        retriever = vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k":2,
                "fetch_k":10,
                "lambda_mult":0.5
            }
        )

        docs = retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        final_prompt = prompt.invoke(
            {
                "context":context,
                "question":question
            }
        )

        response = llm.invoke(final_prompt)

        answer = response.content
        del vectorstore
        gc.collect()

    with st.chat_message("assistant"):
        st.markdown(answer)

        if os.path.exists(DB_DIR):

            with st.expander("📄 Retrieved Chunks"):

                try:
                    for i, doc in enumerate(docs):
                        st.markdown(f"### Chunk {i+1}")
                        st.write(doc.page_content)
                except:
                    pass

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )