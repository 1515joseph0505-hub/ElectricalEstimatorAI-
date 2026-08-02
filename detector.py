from collections import Counter
from symbol_detector import pdf_to_images
from matcher import detect_symbols

def analyze_pdf(pdf_bytes):

    pages = pdf_to_images(pdf_bytes)

    counts = Counter()

    for img in pages:

        symbols = detect_symbols(img)

        for s in symbols:
            counts[s["type"]] += 1

    return {
        "pages": len(pages),
        "lighting_points": counts["light"],
        "sockets": counts["socket"],
        "switches": counts["switch"],
        "distribution_boards": counts["db"]
    }