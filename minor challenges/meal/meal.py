#   Import responsories
import sys


def convert(time):

    try:

        if ':' not in time:
            raise Exception(time)

    except Exception as e:
        sys.exit(e)

    #   Handling the string
    h, m = time.split(':')
    h, m = float(h), float(m)

    #   Dividing the remaining minutes into a decimal place
    m /= 60

    #   Adding the result into x
    h += m

    return h


def main():

    """
        Title       :   Meals
        Author      :   krigjo25
        Description :
            Implements a program that prints out the meals of the day

            USEAGE : type in the terminal python meal.py,
            type in a floating point integer.

    """
    # Prompt the user for time
    n = convert(input('Insert time : '))

    if n < 8 and n < 10:
        return print("breakfast time")

    if n > 10 and n < 15:
        return print("lunch time")

    if n > 15 and n < 20:
        return print("dinner time")


if __name__ == '__main__':
    main()
