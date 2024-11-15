# Histogram Equalization Script

This repository contains a Python script to perform histogram equalization, enhancing the contrast of grayscale images. The script processes a low-contrast image from the `input` folder and saves the enhanced image to the `output` folder.

---

## Prerequisites

- **Python**: Version 3.6 or higher
- **Required libraries**:
  - `numpy`
  - `Pillow`
  - `matplotlib`

### Install Required Libraries

Run the following command to install the necessary libraries:

  ```bash
  pip install numpy pillow matplotlib
  ```
## Usage
### Step 1: Prepare Your Input Image
* Place your low-contrast grayscale images in the images/input folder.
Note the filename of the image you want to process (e.g., image1.png).

## Step 2: Update the Input Path in the Script
* Open the histogram_equalization.py script in a code editor.

* Locate the variable input_image_path near the beginning of the script.

* Change its value to the relative path of your input image. For example:
  ```
  input_image_path = "images/input/image1.png"
  ```

* (Optional) Change the output_image_path if you'd like to save the processed image with a different name or location. For example:
  ```
  output_image_path = "images/output/equalized_image.png"
  ```

## Step 3: Run the Script
* Open a terminal in the root directory of the repository.

* Run the script using the following command:
  ```
  python histogram_equalization.py
  ```

## Notes
* Ensure that the paths to the input and output images are correctly set in the script.
* The script supports only grayscale images. If your input is in color, it will automatically be converted to grayscale.
