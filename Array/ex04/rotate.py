import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from load_image import load_image

def transpose_image(image_array):
    try:
        # Transpose the image
        transposed_array = np.transpose(image_array, (1, 0, 2))
        
        # Print the new shape after transpose
        transposed_shape = transposed_array.shape
        print(f"New shape after Transpose: {transposed_shape} or {(transposed_shape[0], transposed_shape[1])}")

        # Print the data of the transposed image
        print(transposed_array.squeeze())

        # Display the transposed image
        transposed_image = Image.fromarray(transposed_array.squeeze())
        plt.imshow(transposed_image, cmap='gray')
        plt.title("Transposed Image")
        plt.show()

    except Exception as e:
        print(f"An error occurred during transposing: {e}")

if __name__ == "__main__":
    image_path = 'animal.jpeg'
    cut_image_array = load_image(image_path)
    if cut_image_array is not None:
        transpose_image(cut_image_array)

