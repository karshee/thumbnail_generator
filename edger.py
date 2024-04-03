import cv2
import numpy as np

def add_thin_white_edge(input_path, output_path='result_with_thin_border.png', border_thickness=2):
    # Load the image with transparency (alpha channel)
    image = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    
    # Create an alpha mask from the alpha channel
    alpha_channel = image[:, :, 3]
    
    # Find contours in the alpha mask
    contours, _ = cv2.findContours(alpha_channel, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw the contours with a white border
    cv2.drawContours(image, contours, -1, (255, 255, 255, 255), border_thickness)
    
    # Save the result
    cv2.imwrite(output_path, image)

# Usage
add_thin_white_edge('cropped_image.png')
