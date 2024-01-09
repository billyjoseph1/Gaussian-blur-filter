import cv2
import numpy as np

# Load the image
image = cv2.imread('C:/Users/1josm/Downloads/figure2.png')

# Apply a Gaussian blur to the image
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Subtract the blurred image from the original image
sharp = cv2.addWeighted(image, 1.5, blurred, -0.5, 0)

# Save the sharpened image
cv2.imwrite('sharp.png', sharp)

