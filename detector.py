from symbol_detector import pdf_to_images


def analyze_pdf(pdf_bytes):

    pages = pdf_to_images(pdf_bytes)

    result = {
        "pages": len(pages),
        "lights": 0,
        "switches": 0,
        "sockets": 0,
        "dbs": 0,
        "message": "Image extraction successful. Symbol detection coming next."
    }

    return result