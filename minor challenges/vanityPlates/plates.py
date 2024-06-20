def main():

    if PlateValidation(input("Plate: ").upper()):
        return print("valid")

    else:
        return print("invalid")


def PlateValidation(plate):

    #   Ensure the string meets the requirements
    if CheckLengthAndSymbols(plate):
        if CheckTheNumbers(plate):
            if PlateDesign(plate):
                return True else: return False
        else:
            return False
    else:
        return False


def CheckLengthAndSymbols(arg):

    #   Ensures the maximum of characters is 6 while minimum is 2
    if len(arg) <= 6 and len(arg) > 1:

        #   Ensures that the string is numeric
        if str(arg).isalnum():
            return True
        else:
            return False

    else:
        return False


def CheckTheNumbers(arg):
    '''
        Checking for the first digit in the string,
        if the number starts with 0 return false.
    '''

    #   Iterating through the argument
    for i in str(arg):

        #   Ensures the first digts is not 0
        if i.isdigit():
            if i.startswith('0'):
                return False
            else:
                return True

    return True


def PlateDesign(arg):
    '''
                    PlateDesign
        If the numbers are in the middle of the prompt
        the user will recive an error.

    '''

    #   Ensures the first two character is letters
    if str(arg[0:2]).isalpha():

        #   Ensures the numbers is at the end of the plate
        if str(arg[2:]).isnumeric():
            return True
        elif str(arg[3:]).isnumeric():
            return True
        elif str(arg[4:]).isnumeric():
            return True
        elif str(arg).isalpha():
            return True
        else:
            return False

    else:
        return False


if __name__ == "__main__":
    main()
