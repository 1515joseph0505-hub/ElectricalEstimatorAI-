from symbol_detector import pdf_to_images
from matcher import detect_symbols

def analyze_pdf(pdf_bytes):

    pages = pdf_to_images(pdf_bytes)

    total_symbols = 0

    for img in pages:
        symbols = detect_symbols(img)
        total_symbols += len(symbols)

    return {
        "pages": len(pages),
        "symbols_found": total_symbols,
        "message": "Symbol detection engine running."
    }