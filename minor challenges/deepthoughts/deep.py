#   Importing responsories
import sys


def main():
    """
        Title       :   Deep Thoughts
        author      :   krigjo25
        Description :
            Implements a functionallity that prints out
            either Yes or No.

            Usage : type in the terminal python deep.py,
            wait for the prompt then type 42 / forty two etc

    """
    #   Prompting the user for an input to answer
    prompt = input('Forty two or 42? :').replace('-', ' ').lower()

    arg = ["42", 'forty two']

    try:

        #   Ensure that this exist in prompted message
        if prompt.strip() not in arg:
            raise Exception("No")

    except Exception as e:
        return sys.exit(e)

    return sys.exit('Yes')


if __name__ == '__main__':

    main()
