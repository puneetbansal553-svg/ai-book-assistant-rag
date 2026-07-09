# 📚 AI Book Assistant (RAG)

An AI-powered **Retrieval-Augmented Generation (RAG)** application that allows users to upload one or more PDF books and ask questions based on their content.

The application processes uploaded PDFs, creates a vector database using Hugging Face embeddings, retrieves the most relevant document chunks with ChromaDB, and generates accurate answers using Mistral AI.

---

## 🚀 Features

- 📄 Upload multiple PDF books
- 🔍 Ask questions about uploaded documents
- 🧠 Retrieval-Augmented Generation (RAG)
- 📚 Chroma Vector Database
- 🤖 Mistral AI for answer generation
- 📝 Displays retrieved document chunks
- 💬 Interactive chat interface
- ⚡ Fast semantic search using Hugging Face embeddings

---

## 🛠️ Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### AI & Machine Learning

- LangChain
- Mistral AI
- Hugging Face Embeddings
- ChromaDB

### Document Processing

- PyPDFLoader
- Recursive Character Text Splitter

---

## 📂 Project Structure

```
AI-Book-Assistant-RAG/
│
├── app.py
├── create_database.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-book-assistant-rag.git
```

### Navigate to the project

```bash
cd ai-book-assistant-rag
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. Upload one or more PDF books.
2. Documents are loaded using **PyPDFLoader**.
3. Text is split into chunks using **RecursiveCharacterTextSplitter**.
4. Chunks are converted into embeddings using **Hugging Face MiniLM**.
5. Embeddings are stored in **ChromaDB**.
6. User questions are converted into embeddings.
7. Chroma retrieves the most relevant chunks.
8. Retrieved context is sent to **Mistral AI**.
9. The generated answer is displayed along with the retrieved chunks.

---

## 📦 Libraries Used

- Streamlit
- LangChain
- LangChain Community
- LangChain Chroma
- LangChain HuggingFace
- LangChain MistralAI
- ChromaDB
- Sentence Transformers
- python-dotenv

---



## 📈 Future Improvements

- Conversation memory
- Citation with page numbers
- Source highlighting
- PDF preview
- Hybrid search
- Support for DOCX and TXT files
- Deploy on Streamlit Community Cloud

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---


## 👨‍💻 Author

**Puneet Bansal**

ECE Undergraduate | IIIT Dharwad

GitHub: https://github.com/YOUR_USERNAME
