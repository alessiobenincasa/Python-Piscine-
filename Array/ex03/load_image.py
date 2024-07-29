import numpy as np
from PIL import Image

def load_image(image_path):
    try:
        # Load the image
        image = Image.open(image_path)
        
        # Convert image to numpy array
        image_array = np.array(image)
        
        # Get image dimensions and number of channels
        height, width, channels = image_array.shape
        print(f"The shape of image is: {image_array.shape}")

        # Print the pixel content of the image
        print(image_array)

        return image_array
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    image_path = 'animal.jpeg'
    load_image(image_path)
