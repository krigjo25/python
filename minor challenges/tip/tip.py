
#   TipCalculator.py
def main():

    """
        Title       :   Tip
        Author      :   krigjo25
        Description :
            Implements a program to calculate the tip by procentage.

            USEAGE : In your terminal type python tip.py and follow the instruction
            for the prompted message

    """
    #   Initializing the variables
    #   Asking the user for a input

    #   Calculate the output and return the string
    return print(f'Leave ${dollarsToFloat(input('How much was the meal?'))*percentToFloat(input('What procentage would you like to tip?')):.2f}\n')


def dollarsToFloat(arg):

    #   Handling the string
    arg = str(arg).replace('$', '')

    #   Returning the argument
    return float(arg)

def percentToFloat(arg):

    #   Handling the string
    arg = str(arg).replace('%', '')
    arg = float(arg)

    return arg / 100

if __name__ == '__main__':
    main()
