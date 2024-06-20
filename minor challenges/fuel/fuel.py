def main():

    """     Title       :   fuel up
            Description :   Implements a program to convert fraction to procentage
            Usage : type in the terminal python lines.py, follow the instruction from the prompted message
            Author      :   @krigjo25
            
    """
    print(convert(input("Type in a fraction :")))


def convert(arg):
    """ Converting the fraction to prosentage """

    while (True):

        try:
            for i in str(arg).split('/'):
                if not i.isdigit():
                    raise ValueError("Can not calculate alphabetical characters")

            x, y = str(arg).split('/')
            x, y = int(x), int(y)

            #   Ensuring the values does not raises any errors
            if y == 0:
                raise ZeroDivisionError("Can not be devided with zero.")

            elif x > y:
                raise ValueError(f"{x}(x) can not be greater than {y}(y).")

        except (Exception, ZeroDivisionError, ValueError) as e:
            print(f"{e}\nUsage python fuel.py and follow the instruction")
            arg = input("Type in a fraction :")

            continue

        break

    #   Ensuring the convertion to procetage
    arg = round((x / y) * 100)

    if arg <= 100:
        return gauge(arg)


def gauge(arg):

    #   Ensure the value is below
    if arg > 95:
        return "F"
    elif arg < 2:
        return "E"
    else:
        return f"{arg}%"


if __name__ == "__main__":
    main()
