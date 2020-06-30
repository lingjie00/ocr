import pdf2image
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file)


def ocr_core(file):
    text = pytesseract.image_to_string(file)
    return text


def print_pages(pdf_file):
    result = ''
    images = pdf_to_img(pdf_file)
    for pg, img in enumerate(images):
        result += ocr_core(img)
    return result

result = print_pages("input.pdf")

with open('output.txt','w') as file:
    file.write(result)