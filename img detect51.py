
from  PIL import Image
import numpy as np

def detect_pixelation(image_path, scale_factor):
    # Open the image using PIL
    img = Image.open(r'E:\\ALL DECOUMENT\\AJAY  & NEERAJ\\3.jpg')

    # Get the original dimensions
    width, height = img.size

    # Downsample the image
    new_width = int(width / scale_factor)
    new_height = int(height / scale_factor)
    img_downsampled = img.resize((new_width, new_height), resample=Image.BICUBIC)

    # Upsample the image back to its original size
    img_upsampled = img_downsampled.resize((width, height), resample=Image.BICUBIC)

    # Save the upsampled image
    img_upsampled.save("pixelated_image.jpg")

    # Calculate the difference between the original and upsampled images
    img_diff = np.array(img) - np.array(img_upsampled)
    pixelation_score = np.mean(np.abs(img_diff))

    return pixelation_score


pixelation_score = detect_pixelation(r'E:\\ALL DECOUMENT\\AJAY  & NEERAJ\\3.jpg', 4)
print("Pixelation score:", pixelation_score)

import cv2

def detect_pixelation_opencv(image_path, threshold):
    # Read the image using OpenCV
    img = cv2.imread(r'E:\\ALL DECOUMENT\\AJAY  & NEERAJ\\3.jpg')

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply the Laplacian filter
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)

    # Calculate the variance of the Laplacian image
    variance = laplacian.var()
    print(variance)
    # Check if the variance is below the threshold
    if variance < threshold:
        return "Pixelated"
    else:
        return "Not pixelated"
    
result = detect_pixelation_opencv(r'E:\\ALL DECOUMENT\\AJAY  & NEERAJ\\3.jpg', 250.0)

print("Image is", result)



import cv2
import numpy as np
from matplotlib import pyplot as plt

def deblur_image(image_path):
    # Load the blurred image
    image = cv2.imread(r'E:\\ALL DECOUMENT\\AJAY  & NEERAJ\\3.jpg')
    
    # Convert the image from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define the kernel for Wiener filter
    kernel = np.ones((5, 5), np.float32) / 25

    # Initialize the deblurred image array
    deblurred = np.zeros_like(image_rgb)

    # Apply the Wiener filter to each channel separately
    for i in range(3):  # RGB channels
        deblurred[:, :, i] = cv2.filter2D(image_rgb[:, :, i], -1, kernel)

    # Display the original and deblurred images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title("Blurred Image")
    plt.imshow(image_rgb)

    plt.subplot(1, 2, 2)
    plt.title("Deblurred Image")
    plt.imshow(deblurred)

    plt.show()

# Provide the path to your blurred image
deblur_image(r'E:\\ALL DECOUMENT\\AJAY  & NEERAJ\\3.jpg')


