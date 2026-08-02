import fitz
from page_classifier import classify_page

def analyze_pdf(pdf_bytes):

    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    pages = []

    for page_number, page in enumerate(doc):

        text = page.get_text()

        page_type = classify_page(text)

        pages.append({
            "page": page_number + 1,
            "type": page_type
        })

    doc.close()

    return {
        "total_pages": len(pages),
        "pages": pages
    }