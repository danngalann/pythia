from services.ingest.document.PDFIngestor import PDFIngestor

if __name__ == "__main__":
    pdf_ingestor = PDFIngestor()
    document = pdf_ingestor.ingest("/home/daniel/Documents/Attention Is All You Need.pdf")
    docs = pdf_ingestor.search(document, "What are transformers?")
    print(docs)
