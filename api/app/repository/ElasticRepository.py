from typing import List

from langchain.vectorstores import ElasticVectorSearch
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document


class ElasticRepository:
    def __init__(self):
        self.vectorstore = ElasticVectorSearch(
            elasticsearch_url='http://localhost:9200',
            index_name="pythia",
            embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
        )

    def add_texts(self, texts: List[str]):
        """Adds a list of texts to the vector store"""
        self.vectorstore.add_texts(texts)

    def search(self, query: str, top_k: int = 4) -> List[Document]:
        """Searches the vector store for similar texts"""
        return self.vectorstore.similarity_search(query, k=top_k)
