from rembg import remove
import numpy as np
import cv2
import os

def process_images(image_paths):
    for index, input_path in enumerate(image_paths, start=1):
        # Generate a unique output path in the same directory with a numbered filename
        directory = os.path.dirname(input_path)
        output_filename = f"{index}.png"
        output_path = os.path.join(directory, output_filename)
        
        # Process and save each image
        process_and_save_image(input_path, output_path)

def process_and_save_image(input_path, output_path):
    # Open the image file
    with open(input_path, 'rb') as i:
        input_data = i.read()

    # Remove the background from the image
    output_data = remove(input_data)

    # Save the output data to a new image file
    with open(output_path, 'wb') as out:
        out.write(output_data)

    # Read the image with transparent background
    image = cv2.imread(output_path, cv2.IMREAD_UNCHANGED)

    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create a mask where the transparent parts are 0 and the rest is 255
    mask = np.where(gray_image == 0, 0, 255).astype(np.uint8)

    # Find contours from the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on the image
    contour_image = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)

    # Save the final image with the contour
    cv2.imwrite(output_path, contour_image)
    print(f'Processed {input_path} and saved as {output_path}')

image_paths = ['/Users/kasum.hussain/Desktop/BestOf/9 Bobby Lee Compilations/9/Screenshot 2024-01-19 at 11.02.10.png', '/Users/kasum.hussain/Desktop/BestOf/9 Bobby Lee Compilations/9/Screenshot 2024-01-19 at 11.02.32.png']  # Replace with your actual image paths

# Process all images
process_images(image_paths)
