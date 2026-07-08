from langchain_community.document_loaders import WebBaseLoader

url = "https://iiitdwd.ac.in/placements/#placement-statistics"

data = WebBaseLoader(url)

docs = data.load()

print(len(docs))