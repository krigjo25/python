#   Importing responsories
import sys


def main():

    #   Initializing 3D array (Images / Applications / Other)
    extensions = [
        ['gif', 'jpg', 'jpeg', 'png'],
        ['pdf', 'zip'], ['txt']
    ]

    #   Prompting the user for file name with extention and handling the string
    ext = input('Type in a file name: ').strip()

    #   Handling the string
    ext = ext[-4:].replace('.', '').lower()

    try:

        if extensions:
            for i in extensions:
                if ext in extensions[extensions.index(i)]:
                    break
            else:
                raise Exception("application/octet-stream")

    except Exception as e:
        sys.exit(e)

    for i in extensions:

        for j in extensions[extensions.index(i)]:

            #   Ensure that the extension lies in index :
            if ext == j and extensions.index(i) == 0:
                if ext == 'jpg':
                    return print(f"image/jpeg")

                return print(f"image/{j}")

            if ext == j and extensions.index(i) == 1:
                return print(f"application/{j}")

            if ext == j and extensions.index(i) == 2:
                return print(f"text/plain")


if __name__ == '__main__':
    main()
