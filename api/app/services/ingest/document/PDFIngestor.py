from typing import List

from .DocumentIngestor import DocumentIngestor
from PyPDF2 import PdfReader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS


class PDFIngestor(DocumentIngestor):
    """Ingestor for PDF documents"""

    def ingest(self, document_path: str):
        """Ingests a PDF document into the database"""
        reader = PdfReader(document_path)
        raw_text = self.__get_raw_text(reader)
        split_texts = self.__split_text(raw_text)
        document = self.__get_embeddings(split_texts)

        return document

    def search(self, document: FAISS, query: str) -> List[str]:
        return [doc.page_content for doc in document.similarity_search(query)]

    def __get_raw_text(self, reader: PdfReader) -> str:
        """Gets the raw text from a PDF document"""
        raw_text = ""
        for page in reader.pages:
            raw_text += page.extract_text()

        return raw_text

    def __split_text(self, raw_text: str) -> List[str]:
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )

        return text_splitter.split_text(raw_text)

    def __get_embeddings(self, texts: List[str]) -> FAISS:
        """Gets the embeddings for a text"""
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
        return FAISS.from_texts(texts, embeddings)
