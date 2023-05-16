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
        print(raw_text)

    def __get_raw_text(self, reader: PdfReader) -> str:
        """Gets the raw text from a PDF document"""
        raw_text = ""
        for page in reader.pages:
            raw_text += page.extract_text()

        return raw_text