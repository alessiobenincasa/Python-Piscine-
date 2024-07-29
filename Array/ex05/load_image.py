import numpy as np
from PIL import Image

def ft_load(image_path):
    try:
        # Load the image
        image = Image.open(image_path)
        
        # Convert image to numpy array
        image_array = np.array(image)
        
        # Print the shape of the image
        print(f"The shape of image is: {image_array.shape}")
        print(image_array)
        
        return image_array
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    image_path = 'landscape.jpg'
    ft_load(image_path)
