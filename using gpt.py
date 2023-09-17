from PIL import Image
import pytesseract
import cv2
import numpy as np

# Path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'  # Update this path

# Load an image using PIL (Python Imaging Library)
image_path = 'roi_1.jpg'  # Update this path
image = Image.open(image_path)

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Convert the image to a numpy array and then to grayscale
image_np = np.array(image)
cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# Get bounding box estimates
h, w, _ = image_np.shape
boxes = pytesseract.image_to_boxes(image)
for b in boxes.splitlines():
    b = b.split(' ')
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(image_np, (x, h), (w, y), (0, 255, 0), 2)
    cv2.putText(image_np, b[0], (x, h-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

# Save the image
cv2.imwrite('highlighted_text.jpg', image_np)

# Display the image
cv2.imshow('Highlighted Text', image_np)
cv2.waitKey(0)
cv2.destroyAllWindows()
