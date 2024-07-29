from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt
import numpy as np

def display_image(array, title):
    plt.imshow(array.astype(np.uint8))  # Ensure the array is in uint8 format for proper display
    plt.title(title)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    image_path = 'landscape.jpg'
    array = ft_load(image_path)
    
    if array is not None:
        inverted = ft_invert(array)
        red = ft_red(array)
        green = ft_green(array)
        blue = ft_blue(array)
        grey = ft_grey(array)

        display_image(inverted, 'Inverted Image')
        display_image(red, 'Red Image')
        display_image(green, 'Green Image')
        display_image(blue, 'Blue Image')
        display_image(grey, 'Grey Image')

        print(ft_invert.__doc__)
