# store_embeddings.py
'''
from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv

load_dotenv()

# Environment variables
openai_api_key = os.environ['OPENAI_API_KEY']
client = MongoClient(os.environ["MONGODB_URI"])
db = client[os.environ["DATABASE_NAME"]]
collection = db[os.environ["COLLECTION_NAME"]]

ATLAS_VECTOR_SEARCH_INDEX_NAME = "vector_index"

# Load the data
loader = PyPDFLoader("test.pdf")
data = loader.load()
print(f"Number of pages loaded: {len(data)}")

# Split the docs and create embeddings
text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=100)
chunks = text_splitter.split_documents(data)
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key, disallowed_special=())

# Create embeddings in atlas vector store
vector_search = MongoDBAtlasVectorSearch.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection=collection,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME
)

print("Embeddings created and stored successfully.")
'''