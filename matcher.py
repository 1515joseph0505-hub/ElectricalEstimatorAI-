import cv2

def detect_symbols(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    _, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    symbols = []

    for c in contours:

        area = cv2.contourArea(c)

        if area < 20:
            continue

        x, y, w, h = cv2.boundingRect(c)

        symbols.append({
            "x": x,
            "y": y,
            "w": w,
            "h": h,
            "area": area
        })

    return symbols