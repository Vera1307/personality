from PIL import Image

import pytesseract
import cv2
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
def extract_name(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(Image.fromarray(img), config = "tessedit_char_blacklist=0123456789/[]^")
    names = re.findall("[A-Z]+", text)
    black_list = ['REPUBLICA',
                 'MOLDOVA',
                 'MDA',
                 'CA',
                 'BULETIN',
                 'DE',
                 'IDENTITATE']
    names = [name for name in names if name not in black_list and len(name)>2]
    return ' '.join(names)
img = cv2.imread("test.jpg")
names = extract_name(img)
print(names)