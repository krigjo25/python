#   Importing Responsories
import re
import sys


def main():
    print(count(input("Text: ").lower()))


def count(arg):
    '''
        #   Author :    Krigjo25
        #   Date   :    05.11-22

        #   Description :
            Counts word

    '''

    #   Initializing a list
    arg = [i for i in str(arg).lower().split(' ')]

    #   Initializing variables
    regex = r'^(um)'
    counter = 0

    #   Iterating through the list
    for i in arg:

        #   Ensure the regex matches for each element in the list
        if re.search(regex, i):

            if not 'mm' in i:
                counter += 1

    #   Delete lists
    del arg

    return counter


if __name__ == "__main__":
    main()
