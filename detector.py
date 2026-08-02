import fitz  # PyMuPDF

def analyze_pdf(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    results = {
        "pages": len(doc),
        "lights": 0,
        "switches": 0,
        "sockets": 0,
        "dbs": 0
    }

    for page in doc:
        text = page.get_text().upper()

        # These are placeholders. We'll replace them with
        # real symbol detection later.
        results["lights"] += text.count("LIGHT")
        results["switches"] += text.count("SWITCH")
        results["sockets"] += text.count("SOCKET")
        results["dbs"] += text.count("DISTRIBUTION BOARD")

    return results