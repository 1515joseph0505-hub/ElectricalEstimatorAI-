import fitz
import os

OUTPUT = "dataset/images/train"

os.makedirs(OUTPUT, exist_ok=True)


def pdf_to_images(pdf_file):

    doc = fitz.open(pdf_file)

    for page_no in range(len(doc)):

        page = doc.load_page(page_no)

        pix = page.get_pixmap(dpi=300)

        filename = os.path.join(
            OUTPUT,
            f"page_{page_no+1}.png"
        )

        pix.save(filename)

        print(f"Saved {filename}")

    doc.close()


if __name__ == "__main__":
    pdf_to_images("GUZAPE MEP Rev2.pdf")