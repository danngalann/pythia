from .DocumentIngestor import DocumentIngestor
import magic


class IngestorService(DocumentIngestor):
    def ingest(self, document_path: str):
        ingestor = self.__get_ingestor(document_path)
        ingestor.ingest(document_path)

    def __get_ingestor(self, document_path: str) -> DocumentIngestor:
        mime_type = magic.from_file(document_path, mime=True)
        if mime_type == "application/pdf":
            from .PDFIngestor import PDFIngestor
            return PDFIngestor()
        else:
            raise ValueError("Unknown document type")
