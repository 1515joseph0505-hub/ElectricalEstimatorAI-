def classify(text):

    text = text.upper()

    if "LIGHTING LAYOUT" in text:
        return "lighting"

    if "SOCKETS LAYOUT" in text:
        return "socket"

    if "ELV LAYOUT" in text:
        return "elv"

    if "DISTRIBUTION BOARD SCHEDULE" in text:
        return "db"

    if "ELECTRICAL MAIN SCHEMATIC" in text:
        return "schematic"

    return "other"