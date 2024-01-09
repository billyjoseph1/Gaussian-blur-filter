import cv2
import numpy as np

def apply_median_filter(image, kernel_size):
    return cv2.medianBlur(image, kernel_size)

def apply_mean_filter(image, kernel_size):
    return cv2.blur(image, (kernel_size, kernel_size))

def apply_average_filter(image, kernel_size):
    return cv2.boxFilter(image, -1, (kernel_size, kernel_size))

def main():
    # Load the image
    original_image = cv2.imread('C:/Users/1josm/Downloads/1photo.jpg')

    if original_image is None:
        print("Error: Image not found.")
        return

    # Display the original image
    cv2.imshow('Original Image', original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Choose a kernel size (e.g., 3x3, 5x5, 7x7)
    kernel_size = 7

    # Apply median filter
    median_filtered_image = apply_median_filter(original_image, kernel_size)
    cv2.imshow('Median Filtered Image', median_filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Apply mean filter
    mean_filtered_image = apply_mean_filter(original_image, kernel_size)
    cv2.imshow('Mean Filtered Image', mean_filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Apply average filter
    average_filtered_image = apply_average_filter(original_image, kernel_size)
    cv2.imshow('Average Filtered Image', average_filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
