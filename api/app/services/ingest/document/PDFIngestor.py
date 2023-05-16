from typing import List

from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

from api.app.repository.ElasticRepository import ElasticRepository
from .DocumentIngestor import DocumentIngestor


class PDFIngestor(DocumentIngestor):
    """Ingestor for PDF documents"""

    def __init__(self):
        self.vectorstore = ElasticRepository()

    def ingest(self, document_path: str):
        """Ingests a PDF document into the database"""
        reader = PdfReader(document_path)
        raw_text = self.__get_raw_text(reader)
        split_texts = self.__split_text(raw_text)
        self.__store_embeddings(split_texts)

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

    def __store_embeddings(self, texts: List[str]):
        """Stores the embeddings for a document"""
        self.vectorstore.add_texts(texts)
