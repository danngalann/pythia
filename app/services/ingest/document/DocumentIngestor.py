# Import ABC for abstract class
from abc import ABC, abstractmethod


class DocumentIngestor(ABC):
    """Abstract class for document ingestors"""

    @abstractmethod
    def ingest(self, document):
        """Ingests a document into the database"""
        pass
