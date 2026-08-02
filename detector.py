from yolo_detector import detect

def analyze_pdf(pdf_bytes):

    result = detect(pdf_bytes)

    return result