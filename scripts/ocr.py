import pytesseract
from PIL import Image

def read(data):
    try:
        with Image.open(data) as img:
            img.seek(0)
            text = pytesseract.image_to_string(img)
            return text

    except:
        pass
