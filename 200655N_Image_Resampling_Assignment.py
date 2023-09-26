import os
import cv2
import numpy as np

def bilinear_interpolation(image, new_width, new_height):
    
    height, width, channels = image.shape  # Get the dimensions of the original image
    
    x_scaleFactor, y_scaleFactor = width / new_width, height / new_height   # Calculate scaling factors
    
    result = np.zeros((new_height, new_width, channels), dtype=np.uint8) # Create a new empty image with the desired dimensions
    
    for y in range(new_height):
        for x in range(new_width):
            
            # Calculate the corresponding position in the original image
            src_x_point,src_y_point = x * x_scaleFactor,y * y_scaleFactor
            
            # Find the four nearest neighbors
            x1, x2 = int(src_x_point), min(int(src_x_point) + 1, width - 1)
            y1, y2 = int(src_y_point), min(int(src_y_point) + 1, height - 1)
            
            # Calculate the weights for bilinear interpolation
            a = src_x_point - x1
            b = src_y_point - y1
            
            # Perform bilinear interpolation for each channel
            for c in range(channels):
                result[y, x, c] = (1 - a) * (1 - b) * image[y1, x1, c] + a * (1 - b) * image[y1, x2, c] + (1 - a) * b * image[y2, x1, c] + a * b * image[y2, x2, c]
    
    return result


def nearest_neighbor_interpolation(image, new_width, new_height):
    
    height, width, channels = image.shape  # Get the dimensions of the original image
    
    # Calculate scaling factors
    x_scaleFactor, y_scaleFactor = width / new_width, height / new_height
    
    result = np.zeros((new_height, new_width, channels), dtype=np.uint8)  # Create a new empty image with the desired dimensions
    
    # Perform nearest neighbor interpolation
    for y in range(new_height):
        for x in range(new_width):
            src_x_point= int(x * x_scaleFactor)
            src_y_point = int(y * y_scaleFactor)
            result[y, x] = image[src_y_point, src_x_point]
    
    return result



print("Please set the image input and output paths in the code before running it.")

input_image = cv2.imread('C:\\Users\\kalya\\Downloads\\square.png')  # Specify the path to load the input image

new_width = int(input("Enter the new width: "))   # Get the new dimensions from user input
new_height = int(input("Enter the new height: "))

nearest_neighbor_result = nearest_neighbor_interpolation(input_image, new_width, new_height)   # Resample using nearest neighbor interpolation and bilinear interpolation
bilinear_result = bilinear_interpolation(input_image, new_width, new_height)

output_path = r'C:\Users\kalya\Desktop'  # Specify the path to the output directory

cv2.imwrite(os.path.join(output_path, 'nearest_neighbor_result.jpg'), nearest_neighbor_result)
cv2.imwrite(os.path.join(output_path, 'bilinear_result.jpg'), bilinear_result)

print("Done!" , "Check the output folder for the results.")