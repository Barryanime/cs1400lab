'''Program: Lab4.py
Do some simple image processing
'''
# This brings in functions from the graphics.py file
from graphics import *

#
# Study the pattern of the loop inside a loop (called nested loops). Each time the first loop
# does a single repeat, the entire inner loop does all its repetitions.


def count_pixels(image):
    pixel_count = 0
    # go across the image with the for x loop and then move down a row
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):  # This does its whole loop for every one repetition above!
            pixel_count = pixel_count + 1
    return pixel_count  # replace the 0 with the number of pixels

# Make a function that flips the image left-to-right. A pixel with an x location
# needs to go that distance from the right side. Use image.clone() to make a
# new image of the same size and pixels.


def flip_image_horizontally(image):
    new_image = image.clone()
    # Add code here
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()): # This does its whole loop for every one repetition above!
            red_value = image.getPixelRed(x, y)
            green_value = image.getPixelGreen(x, y)
            blue_value = image.getPixelBlue(x, y)

            new_image.setPixelRed(image.getWidth() - 1 - x, y, red_value)
            new_image.setPixelGreen(image.getWidth() - 1 - x, y, green_value)
            new_image.setPixelBlue(image.getWidth() - 1 - x, y, blue_value)
            # image.getWidth() - 1 - x
    return new_image

# This function loads the image file and centers it in the window. The image is returned so
# it can be drawn.


def load_image(filename):
    # Load the image
    image = Image(Point(0, 0), filename)
    # Center it
    image.move(int(image.getWidth()/2), int(image.getHeight()/2))
    return image

# This is where the program starts


def main():
    # Load the image first so we know how big to make the window.
    image = load_image("university_of_utah.gif")
#    image = load_image("me2.gif")
    # Setup the window using the image size
    win = GraphWin('Image Art', image.getWidth(), image.getHeight(), autoflush=False)
    win.setBackground('yellow') # This is here to help see if the image is centered.

    # Draw the original image and wait for a mouse click to move to the next step
    image.draw(win)
    win.getMouse()

    # Get pixel color values
    red_value = image.getPixelRed(0, 0)
    print(red_value)
    green_value = image.getPixelGreen(0, 0)
    print(green_value)
    blue_value = image.getPixelBlue(0, 0)
    print(blue_value)

    # Set to pure red at (0,0)
    image.setPixelRed(0, 0, 255)
    image.setPixelGreen(0, 0, 0)
    image.setPixelBlue(0, 0, 0)

    # Set to pure red at (200,50)
    image.setPixelRed(200, 50, 255)
    image.setPixelGreen(200, 50, 0)
    image.setPixelBlue(200, 50, 0)

    # Count the pixels
    print("Counting pixels")
    number_of_pixels = count_pixels(image)
    print("There are", number_of_pixels, "pixels in the image.")
    win.getMouse()

    # Flip the image
    print("Flipping image")
    flipped_image = flip_image_horizontally(image)
    flipped_image.draw(win)
    win.getMouse()

    win.close()

# This is the only code the is not indented, so this is the first line executed.
if __name__ == "__main__":
    main()
