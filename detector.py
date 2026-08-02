import fitz

def analyze_pdf(pdf_bytes):

    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    result = {
        "total_pages": len(doc),
        "lighting_pages": [],
        "socket_pages": [],
        "elv_pages": [],
        "db_pages": [],
        "schematic_pages": []
    }

    for i, page in enumerate(doc):

        text = page.get_text().upper()

        if "LIGHTING LAYOUT" in text:
            result["lighting_pages"].append(i + 1)

        if "SOCKETS LAYOUT" in text:
            result["socket_pages"].append(i + 1)

        if "ELV LAYOUT" in text:
            result["elv_pages"].append(i + 1)

        if "DISTRIBUTION BOARD SCHEDULE" in text:
            result["db_pages"].append(i + 1)

        if "ELECTRICAL MAIN SCHEMATIC" in text:
            result["schematic_pages"].append(i + 1)

    doc.close()

    return result