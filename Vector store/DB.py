from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

from langchain_core.documents import Document

docs = [
    Document(page_content="Python is widely used in Artificial Intelligence.", metadata={"source": "AI_book"}),
    Document(page_content="Pandas is used for data analysis in Python.", metadata={"source": "DataScience_book"}),
    Document(page_content="Neural networks are used in deep learning.", metadata={"source": "DL_book"}),
]

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory= 'chroma-db'
)

result = vector_store.similarity_search("what is used for data analsis?",k=2)

for r in result:
    print(r.page_content)
    print(r.metadata)

retriver = vector_store.as_retriver()

docs = retriver.invoke("Explain deep learning")

for d in docs:
    print(d.page_content)