from api.app.repository.ElasticRepository import ElasticRepository
from services.ingest.document.PDFIngestor import PDFIngestor

if __name__ == "__main__":
    pdf_ingestor = PDFIngestor()
    pdf_ingestor.ingest("/home/daniel/Documents/Attention Is All You Need.pdf")

    repository = ElasticRepository()
    results = repository.search("Who are the authors?")

    print(results[0].page_content)
