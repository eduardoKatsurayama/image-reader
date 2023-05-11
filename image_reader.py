from PIL import Image
import pytesseract

def ocr_core(filename):
    """
    Esta função irá lidar com o OCR para imagens
    """
    text = pytesseract.image_to_string(Image.open(filename))
    return text


ocr_core('to_read.png')
