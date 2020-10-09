# Add OCR setup from https://github.com/UB-Mannheim/tesseract/wiki
# add python library using pip install tesseract and pip install pytesseract

import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #Path to the tesseract

def convert():
    img = Image.open('Life-quote.jpg') # Add the image name here
    text = pytesseract.image_to_string(img)
    print(text)

convert()