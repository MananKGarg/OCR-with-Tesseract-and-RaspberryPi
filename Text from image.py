from PIL import Image
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = (r"C:\Users\Manan K. Garg\PycharmProjects\practice\venv\Lib\site-packages\tesseract.exe") # path for tesseract application

img = Image.open("testimage.jpeg")

text = pytesseract.image_to_string(img)                            # pytesseract converts text in image to UTF - 8 format text
print(text)
