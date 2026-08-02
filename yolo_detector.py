from ultralytics import YOLO
import fitz
import cv2
import numpy as np

model = YOLO("best.pt")

def detect(pdf_bytes):

    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    counts = {}

    for page in doc:

        pix = page.get_pixmap(dpi=300)

        img = np.frombuffer(pix.samples, dtype=np.uint8)
        img = img.reshape(pix.height, pix.width, pix.n)

        if pix.n == 4:
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)

        results = model(img)

        for r in results:

            for box in r.boxes:

                cls = int(box.cls[0])

                name = model.names[cls]

                counts[name] = counts.get(name, 0) + 1

    return counts