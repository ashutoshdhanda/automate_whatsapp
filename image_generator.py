from PIL import Image
import random

def generate_image_with_random_color(width, height, filename):
    # Create a new image with RGB mode
    image = Image.new("RGB", (width, height))

    # Get the pixel access object of the image
    pixels = image.load()

    # Generate a random color
    r = random.randint(0, 255)  # Random red value (0-255)
    g = random.randint(0, 255)  # Random green value (0-255)
    b = random.randint(0, 255)  # Random blue value (0-255)
    color = (r, g, b)

    # Assign the random color to all pixels
    for i in range(image.width):
        for j in range(image.height):
            pixels[i, j] = color

    # Save the image
    image.save(filename)