import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
from load_image import load_image

def zoom_image(image_array, offset_right=150, offset_up=50):
    try:
        height, width, channels = image_array.shape
        target_size = 400  # We want a 400x400 region
        center_x, center_y = width // 2, height // 2

        # Adjust center_x to move the image to the right
        center_x += offset_right
        # Adjust center_y to move the image up
        center_y -= offset_up

        # Ensure the slicing doesn't go out of image bounds
        left = max(center_x - target_size // 2, 0)
        right = min(center_x + target_size // 2, width)
        top = max(center_y - target_size // 2, 0)
        bottom = min(center_y + target_size // 2, height)

        zoomed_array = image_array[top:bottom, left:right]

        # Convert to single channel if needed
        if channels == 3:
            zoomed_array = zoomed_array[:, :, 0:1]  # Take only one channel

        # Print the new shape after slicing
        new_shape = zoomed_array.shape
        print(f"New shape after slicing: {new_shape} or {(new_shape[0], new_shape[1])}")

        # Print the zoomed pixel content
        print(zoomed_array)

        zoomed_image = Image.fromarray(zoomed_array.squeeze())
        draw = ImageDraw.Draw(zoomed_image)

        try:
            font = ImageFont.truetype("arial.ttf", 15)
        except IOError:
            font = ImageFont.load_default()

        for i in range(0, zoomed_image.width, zoomed_image.width // 10):
            draw.line((i, 0, i, 10), fill="red")
            draw.text((i, 10), str(i), fill="red", font=font)

        for i in range(0, zoomed_image.height, zoomed_image.height // 10):
            draw.line((0, i, 10, i), fill="red")
            draw.text((10, i), str(i), fill="red", font=font)

        plt.imshow(zoomed_image, cmap='gray')
        plt.title("Zoomed Image with Scales")
        plt.show()

    except Exception as e:
        print(f"An error occurred during zooming: {e}")

if __name__ == "__main__":
    image_path = 'animal.jpeg'
    image_array = load_image(image_path)
    if image_array is not None:
        zoom_image(image_array)
