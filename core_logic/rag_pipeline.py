import hashlib
import os
import uuid
from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.callbacks.manager import get_openai_callback
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
mongo_uri = os.getenv('MONGO_DB_URI', 'undefined')
db_name = os.getenv('DATABASE_NAME', 'undefined')
files_metadata = os.getenv('META_COLLECTION', 'undefined')
embeddings_collection = os.getenv('EMBEDDINGS_COLLECTION', 'undefined')

# Initialize MongoDB connection
client = MongoClient(mongo_uri)
db = client[db_name]
files_metadata = db[files_metadata]
collection = db[embeddings_collection]
openai_api_key = os.getenv("OPENAI_API_KEY")

ATLAS_VECTOR_SEARCH_INDEX_NAME = "vector_index"

# Initialize OpenAI embeddings
embeddings_model = OpenAIEmbeddings(openai_api_key=os.getenv('OPENAI_API_KEY'))


def get_file_hash(file_path):
    """Generate a SHA-256 hash for the file."""
    hash_func = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def check_and_store_metadata_and_embeddings(file_path):
    """
    Check if the file metadata (hash and name) and embeddings exist.
    If not, store them in MongoDB and generate embeddings.
    """
    # Step 1: Calculate the file hash
    file_hash = get_file_hash(file_path)

    # Step 2: Check and store metadata and embeddings
    if files_metadata.find_one({"filehash": file_hash}) is None:
        files_metadata.insert_one(
            {"_id": uuid.uuid4().hex, "filename": os.path.basename(file_path), "filehash": file_hash})
        print(f"File metadata stored for {os.path.basename(file_path)}")

        # Load the PDF and split text into chunks
        loader = PyPDFLoader(file_path)
        data = loader.load()
        print(data)

        # Split the documents into manageable chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=100)
        chunks = text_splitter.split_documents(data)

        # Store the chunks and embeddings into MongoDB
        MongoDBAtlasVectorSearch.from_documents(
            documents=chunks,
            embedding=embeddings_model,
            collection=collection,
            index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME
        )
        return "Embeddings created and stored successfully."
    else:
        return "File metadata already exists."

    return file_hash

def format_docs(docs):
    """Concatenate the content of retrieved documents into a single string."""
    return "\n\n".join(doc.page_content for doc in docs)

# Function to retrieve and generate response
def retrieve_and_generate_response(question, template_text):
    """
    Retrieves relevant documents from MongoDB and generates a response using OpenAI.
    """
    # Vector search to retrieve relevant documents
    vector_search = MongoDBAtlasVectorSearch(collection=collection,index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,embedding=embeddings_model)
    retriever = vector_search.as_retriever(search_type="similarity",search_kwargs={"k": 1})
    prompt = PromptTemplate.from_template(template=template_text)
    output_parser = StrOutputParser()
    model = ChatOpenAI(api_key=openai_api_key, model_name='gpt-4o', temperature=0.7)
    # Build the retrieval and generation pipeline
    retrieval_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | model
            | output_parser
    )
    # Track cost using OpenAI callback
    with get_openai_callback() as cb_rag:
        rag_response = retrieval_chain.invoke(question)
        rag_cost = cb_rag.total_cost
    return rag_response, rag_cost



