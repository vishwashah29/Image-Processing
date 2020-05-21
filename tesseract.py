import pytesseract
from PIL import Image

im=Image.open("handwritten text.jpeg")

result=pytesseract.image_to_string(im,lang= 'eng')
print(result)