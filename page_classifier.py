def classify_page(text):

    text = text.upper()

    if "LIGHTING LAYOUT" in text:
        return "lighting"

    if "SOCKETS LAYOUT" in text:
        return "sockets"

    if "ELV LAYOUT" in text:
        return "elv"

    if "DISTRIBUTION BOARD SCHEDULE" in text:
        return "db_schedule"

    if "ELECTRICAL MAIN SCHEMATIC" in text:
        return "schematic"

    if "LEGEND" in text:
        return "legend"

    return "unknown"