import fitz

def read_pdf(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    pages = []

    for page_number in range(len(doc)):
        page = doc.load_page(page_number)

        pages.append({
            "number": page_number + 1,
            "text": page.get_text()
        })

    doc.close()

    return pages