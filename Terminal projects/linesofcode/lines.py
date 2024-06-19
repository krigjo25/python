#   Importing Python responsories
import sys


def main():
    """
    #   Author      :    krigjo25
    #   Date        :      26.08-22
    #   Description :   Implements a command-line program
            to read python files.
    """
    try:
        if len(sys.argv) != 2:
            raise Exception("Usage python lines.py ")

        elif ".py" not in sys.argv[1]:
            raise Exception("Please Choose a python file. (.py)")


    except FileNotFoundError as e:
        sys.exit(f"{e}")

    lines = []
    with open(f"{sys.argv[1]}", "r") as f:
        #   iterating through the file and remove any white space
        lines = [str(i).lstrip() for i in f.readlines() if i.strip()]

    f.close()

    #   Iterate through list, remove comments
    lines = [i for i in lines if not i.startswith("#")]

    return print(len(lines))

if __name__ == '__main__':
    main()
