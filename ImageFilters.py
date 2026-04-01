# Lab 9 – Image Processing
# Name: Emma Barnes
# Date: 04/01/2026
# Assignment: Image Filters - Lab 09

from PIL import Image


def swapGreenBlue(img):
    """Swap the green and blue values for every pixel in the image."""
    
    pixels = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            red,green,blue, alpha = pixels[x,y]
            pixels[x,y] = (red,blue,green, alpha)

    # TODO: Loop through every pixel and swap green and blue values

    img.save("swapGB.png")


def darken(img, amount):
    """Darken the image by reducing RGB values by the given amount."""
    
    pixels = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            red,green,blue, alpha = pixels[x,y]
            red = max(red - amount, 0)
            blue = max(blue - amount, 0)
            green = max(green - amount, 0)
            pixels[x,y] = (red,green,blue, alpha)

    # TODO: Loop through every pixel and reduce RGB values by amount
    # Make sure values do not go below 0

    img.save("darkImg.png", 'png')


def bwFilter(img):
    """Example function: converts image to grayscale."""
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue, alpha = pixels[x, y]
            avg = (red + green + blue) // 3
            pixels[x, y] = (avg, avg, avg, alpha)

    img.save("bwImg.png", 'png')


def main():
    # Open the image file
    myImg = Image.open("durango.png")

    # Example (already completed)
    # bwFilter(myImg)

    # Uncomment each function as you complete it
    # swapGreenBlue(myImg)
    darken(myImg, 60)


if __name__ == "__main__":
    main()
