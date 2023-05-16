from api.app.repository.ElasticRepository import ElasticRepository
from services.ingest.document.IngestorService import IngestorService

if __name__ == "__main__":
    ingestor = IngestorService()
    ingestor.ingest("/home/daniel/Documents/Attention Is All You Need.pdf")

    repository = ElasticRepository()
    results = repository.search("Who are the authors?")

    print(results[0].page_content)
