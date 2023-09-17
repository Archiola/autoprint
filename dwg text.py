from PIL import Image
from PIL import ImageDraw
import pytesseract
import pytesseract
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/Cellar/tesseract/5.3.2_1'  # 'tesseract' 바이너리 파일의 경로로 설정하세요.

# Load the image
img = Image.open('8dong.jpg')

# Preprocess the image (e.g., resize, enhance contrast)
#img = img.resize((width, height)).convert('L')

# Perform OCR using Tesseract with custom config
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, config=custom_config)

# Extracted text contains letters




# Draw bounding boxes around text regions
draw = ImageDraw.Draw(img)
for box in pytesseract.image_to_boxes(img):
    draw.rectangle([int(box.split()[1]), int(box.split()[2]), int(box.split()[3]), int(box.split()[4])], outline="red")

# Save the image with bounding boxes
img.save('output_image.png')
