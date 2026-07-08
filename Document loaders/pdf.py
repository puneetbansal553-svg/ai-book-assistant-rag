from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

data = PyPDFLoader("Document loaders/24bec048.pdf")

docs = data.load()

# splitter = TokenTextSplitter(
#     chunk_size = 100,
#     chunk_overlap = 10
# )
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 10
)

chunks = splitter.split_documents(docs)
print(chunks[0].page_content)