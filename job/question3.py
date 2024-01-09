import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('D:/Pictures/facebook/photo3.JPG')

# Apply a Gaussian blur to the image
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Subtract the blurred image from the original image to deblur
deblurred = cv2.addWeighted(image, 1.5, blurred, -0.5, 0)

# Display the original and deblurred images side by side
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(deblurred, cv2.COLOR_BGR2RGB))
plt.title('Deblurred Image')

plt.show()
