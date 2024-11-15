import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

input_image_path = "images/input/low_contrast_image1.png"  # Replace with another path to use a different image
output_image_path = "images/output/equalized_image.png"

# Load image with PIL and convert to grayscale
original_img = Image.open(input_image_path).convert("L")
original_array = np.array(original_img) 

# Step 1: Compute histogram
histogram = np.zeros(256, dtype=int)
rows, cols = original_array.shape

for i in range(rows):
    for j in range(cols):
        intensity = original_array[i, j]
        histogram[intensity] += 1

# Step 2: Normalize histogram
normalized_histogram = histogram / (rows * cols)

# Step 3: Compute cumulative distribution function
cdf = np.zeros(256)
cdf[0] = normalized_histogram[0]
for i in range(1, 256):
    cdf[i] = cdf[i - 1] + normalized_histogram[i]

# Step 4: Create transfer function
transfer_function = np.round(cdf * 255).astype(np.uint8)

# Step 5: Apply transfer function to image
equalized_array = np.zeros_like(original_array)
for i in range(rows):
    for j in range(cols):
        equalized_array[i, j] = transfer_function[original_array[i, j]]

# Step 6: Save and display results
equalized_img = Image.fromarray(equalized_array)
equalized_img.save(output_image_path)

# Display input and output images with histograms
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(original_array, cmap="gray")
plt.title("Original Image")
plt.subplot(2, 2, 2)
plt.bar(range(256), histogram, color="gray")
plt.title("Original Histogram")

plt.subplot(2, 2, 3)
plt.imshow(equalized_array, cmap="gray")
plt.title("Equalized Image")
plt.subplot(2, 2, 4)
plt.bar(range(256), np.histogram(equalized_array, bins=256, range=(0, 256))[0], color="gray")
plt.title("Equalized Histogram")

plt.tight_layout()
plt.show()
