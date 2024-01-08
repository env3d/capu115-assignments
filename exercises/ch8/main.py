import image

"""
createNewImage() function is an example where we create an image with 3 colors.
The top third of the image is red
The middle third of the image is green
The last thrid of the image is blue

The image is save into a file called "output.jpg"

Exercise: Modify the function so that it creates an image with 2 colors.
Top half is black
Bottom half is white
"""
def exercise1():
    # Create a new empty image
    img = image.EmptyImage(320, 320)
    width = img.getWidth()
    height = img.getHeight()

    for row in range(height):
        for col in range(width):

            # below is algorithm for creating the image
            # we look at the current row number and
            # create a pixel object of a particular color            
            if row < height / 3:
                pixel = image.Pixel(255, 0, 0)
            elif row < height * 2 / 3:
                pixel = image.Pixel(0, 255, 0)
            else:
                pixel = image.Pixel(0, 0, 255)
            
            # We have created the pixel using the above
            # multi-branch, now we are ready to assign the pixel
            # to the image
            
            img.set_pixel(col, row, pixel)

    # we can now save the image after the entire nested loop is finished
    img.save('output.jpg')


"""
The following function opens the rick-and-morty image, 
and turn write a black and white version of it to output.jpg.

The algorithm simply take the average of red, green and blue channel

Exercise: turn it to a 2 color image, where if the average of the pixels
is < 128 then assign a black pixel to the image, otherwise assign a white
pixel to the image
"""
def exercise2():
    img = image.Image("rick-and-morty.jpg")
    width = img.getWidth()
    height = img.getHeight()

    for row in range(height):
        for col in range(width):
            original_pixel = img.getPixel(col, row)

            red = original_pixel.get_red()
            green = original_pixel.get_green()
            blue = original_pixel.get_blue()

            average_value = (red + green + blue) / 3

            # to complete this exercise, you will need to use a if statement below
            new_pixel = image.Pixel(average_value, average_value, average_value)

            img.setPixel(col, row, new_pixel)

    img.save('output.jpg')


"""
Below is a function to turn an image into a negative version as per 8.11 from 
the text.

Exercise: modify it so that instead of turning the image negative, multiply the
value of each color channel by 0.5
"""
def exercise3():
    img = image.Image("rick-and-morty.jpg")

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)

            newred = 255 - p.getRed()
            newgreen = 255 - p.getGreen()
            newblue = 255 - p.getBlue()

            newpixel = image.Pixel(newred, newgreen, newblue)

            img.setPixel(col, row, newpixel)

    img.save('output.jpg')
