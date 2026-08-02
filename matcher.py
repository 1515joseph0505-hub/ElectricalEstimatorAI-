import cv2
import os

TEMPLATES = {
    "light": cv2.imread("templates/light.png", 0),
    "socket": cv2.imread("templates/socket.png", 0),
    "switch": cv2.imread("templates/switch.png", 0),
    "db": cv2.imread("templates/db.png", 0),
}

def detect_symbols(image):

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    results = []

    for name, template in TEMPLATES.items():

        if template is None:
            continue

        w, h = template.shape[::-1]

        match = cv2.matchTemplate(
            gray,
            template,
            cv2.TM_CCOEFF_NORMED
        )

        threshold = 0.75

        locations = zip(*((match >= threshold).nonzero())[::-1])

        for pt in locations:
            results.append({
                "type": name,
                "x": int(pt[0]),
                "y": int(pt[1]),
                "w": int(w),
                "h": int(h)
            })

    return results