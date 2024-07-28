from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    try:
        # Open the image file
        with Image.open(path) as img:
            # Check if the image format is JPEG/JPG
            if img.format not in ['JPEG', 'JPG']:
                raise ValueError(f"Unsupported image format: {img.format}")
            
            # Convert the image to RGB
            img_rgb = img.convert('RGB')
            
            # Get the numpy array of the image
            img_array = np.array(img_rgb)
            
            # Print the image format
            print(f"The format of the image is: {img.format}")
            
            # Print the shape of the image
            print(f"The shape of image is: {img_array.shape}")
            
            # Return the numpy array of the image
            return img_array
    
    except Exception as e:
        # Handle any exceptions and print a clear error message
        print(f"An error occurred: {e}")
        return None
