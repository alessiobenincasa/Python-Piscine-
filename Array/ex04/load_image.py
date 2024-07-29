import numpy as np
from PIL import Image

def load_image(image_path, offset_right=0, offset_up=0, target_size=400):
    try:
        # Load the image
        image = Image.open(image_path)
        
        # Convert image to numpy array
        image_array = np.array(image)
        
        # Get image dimensions and number of channels
        height, width, channels = image_array.shape
        
        # Determine the center of the image
        center_x, center_y = width // 2, height // 2
        
        # Adjust center_x and center_y if needed
        center_x += offset_right
        center_y -= offset_up
        
        # Ensure the slicing doesn't go out of image bounds
        left = max(center_x - target_size // 2, 0)
        right = min(center_x + target_size // 2, width)
        top = max(center_y - target_size // 2, 0)
        bottom = min(center_y + target_size // 2, height)
        
        # Cut the square part of the image
        cut_image_array = image_array[top:bottom, left:right]

        # Convert to single channel if needed
        if channels == 3:
            cut_image_array = cut_image_array[:, :, 0:1]  # Take only one channel

        # Print the shape of the cut image
        cut_image_shape = cut_image_array.shape
        print(f"The shape of image is: {cut_image_shape} or {(cut_image_shape[0], cut_image_shape[1])}")
        print(cut_image_array)

        return cut_image_array
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    image_path = 'animal.jpeg'
    load_image(image_path)
