import numpy as np

def ft_invert(array):
    """
    Inverts the color of the image received.
    """
    return 255 - array

def ft_red(array):
    """
    Keeps only the red channel of the image.
    """
    red_array = np.zeros_like(array)
    red_array[:, :, 0] = array[:, :, 0]
    return red_array

def ft_green(array):
    """
    Keeps only the green channel of the image.
    """
    green_array = np.zeros_like(array)
    green_array[:, :, 1] = array[:, :, 1]
    return green_array

def ft_blue(array):
    """
    Keeps only the blue channel of the image.
    """
    blue_array = np.zeros_like(array)
    blue_array[:, :, 2] = array[:, :, 2]
    return blue_array

def ft_grey(array):
    """
    Converts the image to greyscale.
    """
    grey_array = np.mean(array, axis=2, dtype=int)
    grey_array = np.repeat(grey_array[:, :, np.newaxis], 3, axis=2)
    return grey_array
