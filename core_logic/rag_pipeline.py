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
from numpy import dot
from numpy.linalg import norm

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


# Function to generate SHA-256 hash for the file
def get_file_hash(file_path):
    """Generate a SHA-256 hash for the file."""
    hash_func = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()


# Function to check and store metadata and embeddings
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

        # Split the documents into manageable chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
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


# Function to format documents for display
def format_docs(docs):
    """Concatenate the content of retrieved documents into a single string."""
    return "\n\n".join(doc.page_content for doc in docs)


# Function to calculate cosine similarity for embeddings
def calculate_cosine_similarity(query_embedding, document_embedding):
    return dot(query_embedding, document_embedding) / (norm(query_embedding) * norm(document_embedding))


# Hybrid search using both keyword and vector similarity
def hybrid_search(question, similarity_threshold=0.5, k=10):
    """
    Perform hybrid search combining keyword search and vector similarity search.

    Parameters:
    - question: The user's input query.
    - similarity_threshold: The threshold to filter documents by similarity.
    - k: The number of top documents to retrieve based on similarity.

    Returns:
    - relevant_docs: A list of relevant documents.
    """
    # Keyword-based search
    keyword_results = list(collection.find({"$text": {"$search": question}}))

    # Perform vector search
    vector_search = MongoDBAtlasVectorSearch(
        collection=collection,
        index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
        embedding=embeddings_model
    )
    retriever = vector_search.as_retriever(search_type="similarity", search_kwargs={"k": k})
    vector_results = retriever.get_relevant_documents(question)

    # Combine keyword and vector search results
    combined_results = keyword_results + vector_results

    # Filter based on similarity threshold
    relevant_docs = [doc for doc in combined_results if doc.metadata.get('similarity_score', 0) >= similarity_threshold]

    return relevant_docs


# Function to retrieve and generate a response using OpenAI
def retrieve_and_generate_response(question, template_text, similarity_threshold=0.5, k=5):
    """
    Retrieves relevant documents from MongoDB based on similarity and generates a response using OpenAI.

    Parameters:
    - question: The input question or query.
    - template_text: The template for structuring the response.
    - similarity_threshold: The minimum similarity score to consider a document relevant.
    - k: Number of documents to retrieve.

    Returns:
    - response: The generated response.
    - cost: The cost of the OpenAI API request.
    """
    # Hybrid search
    relevant_docs = hybrid_search(question, similarity_threshold=similarity_threshold, k=k)

    if not relevant_docs:
        return "No relevant documents found based on the similarity threshold.", 0

    # Prepare the prompt with retrieved documents
    context = format_docs(relevant_docs)
    prompt = PromptTemplate.from_template(template=template_text)
    output_parser = StrOutputParser()
    model = ChatOpenAI(api_key=openai_api_key, model_name='gpt-4o', temperature=0.7)

    # Build the retrieval and generation pipeline
    retrieval_chain = (
            {"context": context, "question": RunnablePassthrough()} | prompt | model | output_parser
    )

    # Track cost using OpenAI callback
    with get_openai_callback() as cb_rag:
        rag_response = retrieval_chain.invoke(question)
        rag_cost = cb_rag.total_cost

    return rag_response, rag_cost

