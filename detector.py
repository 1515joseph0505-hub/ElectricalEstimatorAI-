from core.pdf_reader import read_pdf
from core.page_classifier import classify

def analyze_pdf(pdf_bytes):

    pages = read_pdf(pdf_bytes)

    analysis = []

    for page in pages:

        analysis.append({
            "page": page["number"],
            "type": classify(page["text"])
        })

    return {
        "pages": analysis
    }