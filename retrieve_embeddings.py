# retrieve_embeddings.py
'''
from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from langchain_community.callbacks.manager import get_openai_callback
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load environment variables
openai_api_key = os.environ['OPENAI_API_KEY']
client = MongoClient(os.environ["MONGODB_URI"])
db = client[os.environ["DATABASE_NAME"]]
collection = db[os.environ["COLLECTION_NAME"]]

ATLAS_VECTOR_SEARCH_INDEX_NAME = "vector_index"

# Ensure the vector store is correctly initialized
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key, disallowed_special=())
vector_search = MongoDBAtlasVectorSearch(
    collection=collection,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
    embedding=embeddings
)

retriever = vector_search.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 1}
)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def retrieve_and_generate_response(question, template_text):
    prompt = PromptTemplate.from_template(template=template_text)
    output_parser = StrOutputParser()
    model = ChatOpenAI(api_key=openai_api_key, model_name='gpt-3.5-turbo', temperature=0)

    retrieval_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | model
            | output_parser
    )

    with get_openai_callback() as cb_rag:
        rag_response = retrieval_chain.invoke(question)
        rag_cost = cb_rag.total_cost

    return rag_response, rag_cost
'''