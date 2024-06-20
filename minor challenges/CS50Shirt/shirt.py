#   Importing Responsories
import sys
import os
from PIL import Image, ImageOps


def main():
    """
    #   Title: CS50Shirt
    #   Description :
            This function ensures that the user has inputted the command-line prompts
            correctly, and ensures the file extension is in the command-line argument.

    """

    #   Configuring file extensions
    path = []
    ext = ['.jpg', '.jpeg', '.png']

    #   Iterating over the comman-line arguments
    for i in sys.argv:
        path.append(os.path.splitext(i))

    try:
        #   Ensuring the Command-line arguments is less than three
        if len(sys.argv) < 3:
            raise Exception('Too few command line arguments')

        #   Ensuring the Command-line arguments is greater than 3
        if len(sys.argv) > 3:
            raise Exception('Too many Command line arguments')

        #   Ensuring the file path extention is not in the list
        if path[1][1] not in ext or path[2][1] not in ext:
            raise Exception('Not a valid extension name')
        if path[1][1] != path[2][1]:
            raise Exception('The extentions is not equal')
    except Exception as e:
        sys.exit("Usage python shirt.py [file path], [output path]", e)

    return CropImage()


def CropImage():
    """ #   Description :
                This function crops the image. """
    try:
        with Image.open(sys.argv[1]) as photo, Image.open(r'shirt.png') as shirt:

            #   Crop the image
            top, bottom = shirt.size
            photo = ImageOps.fit(photo, (top, bottom))

            #   Paste the overlay and save the new photo
            photo.paste(shirt, shirt)
            photo.save(sys.argv[2])

    except FileNotFoundError as e:
        sys.exit(e)


if __name__ == '__main__':
    main()
