from dotenv import load_dotenv
load_dotenv()
import os
index_name=os.getenv("INDEX")

from langchain_community.embeddings import CohereEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CohereRerank

embed = CohereEmbeddings(model="embed-english-v3.0")

vs = PineconeVectorStore(index_name=index_name, embedding=embed)

retr=vs.as_retriever(search_kwargs={"k": 30})

compressor = CohereRerank(user_agent="ct-app", top_n=10)

compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=retr
)

def search_file(query):
    out=compression_retriever.get_relevant_documents(query)
    ans=list(set([os.path.basename(i.metadata['source']) for i in out]))
    return ans