import cv2
import numpy as np

# Load your image
image = cv2.imread('your_image.jpg')

# Convert the image to the HSV color space (Hue, Saturation, Value)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper color range for segmentation (adjust these values based on your image)
lower_color = np.array([0, 0, 0])  # Lower range for black
upper_color = np.array([255, 255, 100])  # Upper range for a lighter color (e.g., yellow)

# Create a mask to segment the regions of interest
mask = cv2.inRange(hsv, lower_color, upper_color)

# Find contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize a counter for saved cropped images
crop_counter = 0

# Loop through the detected contours
for contour in contours:
    # Get the bounding box of the contour
    x, y, w, h = cv2.boundingRect(contour)

    # Crop the region of interest (ROI) from the original image
    roi = image[y:y + h, x:x + w]

    # Save the cropped ROI as a separate image
    cv2.imwrite(f'roi_{crop_counter}.jpg', roi)

    # Increment the counter
    crop_counter += 1

# Print the number of cropped regions
print(f"{crop_counter} regions of interest cropped and saved.")
