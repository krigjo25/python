#   Importing responsories
import sys
from pyfiglet import Figlet, FontNotFound


def main():

    #   Initalizing command-line arguments
    arg = ['-f', '--font']

    try:

        #   Ensure the command-line arguments does not exceed 3 arguments
        if len(sys.argv) > 3:
            raise Exception('To many command-line arguments')

        #   Ensure the command-line command exsists
        if sys.argv[1] not in arg:
            raise Exception("Command not found")

        #   Ensure the font exists
        if not Figlet(font=str(sys.argv[2])):
            raise FontNotFound

    except (FontNotFound, ValueError, Exception) as e:

        sys.exit(
            f"{e}, USEAGE : python pyfiglet.py [Optional : -f / --fonts] [Optional : font name]")

    #   Initializing a prompt
    prompt = input('Type a text:')

    #   Ensure the command-line arguments equals 1
    if len(sys.argv) == 1:

        print(Figlet().renderText(prompt))

    #   Ensure the command-line arguments equals 2
    elif len(sys.argv) == 3:

        print(Figlet(font=str(sys.argv[2])).renderText(prompt))

    return sys.exit()

if __name__ == '__main__':
    main()
