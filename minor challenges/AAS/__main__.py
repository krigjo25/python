#   Importing responsories
from PIL import Image
from PIL.ExifTags import TAGS

def main():
    fetch_metadata('cv.jpg')

def fetch_metadata(file):

    # Starting the workbench
    with Image.open(file) as f:

        #   Fetch image metadata
        exif = f.getexif()

        for id in exif:
            tn = TAGS.get(id, id)
            value = exif.get(id)

            print(f'{tn:25}: {value}')



if __name__ =='__main__':
    main()