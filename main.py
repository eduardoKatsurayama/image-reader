from time import sleep

from PIL import ImageGrab
import pytesseract
import clipboard


def ocr_core():
    image = _read_image_from_transfer_area()
    text = pytesseract.image_to_string(image)
    clipboard.copy(text)


def _read_image_from_transfer_area():
    # Obtendo a imagem da área de transferência
    image = ImageGrab.grabclipboard()
    return image


ocr_core()
