from utils import ocr
image_path="car.jpg"
text = ''

text = ocr.read(image_path)
print("text- ", text)
