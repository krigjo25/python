class Division():

    def __init__(self):
        return

    def GetQuotientReminder(divider, ):

        '''
            #   Author : krigjo25
            #   Date   :  13.01-23

            #   Creating a list of ASCII Decimal

        '''
        try :

            Q = divider // 2
            R = divider % 2
            #   Converting to ASCII digits using ord()
            ASCIIdigits = [ord(i) for i in arg]

            #   Checking if the array contains any alphabetical letters
            for i in ASCIIdigits:
                if str(i).isalpha() : raise ValueError(f'Something went wrong with the conversion of {i}')
        
        except Exception as e : print(e)

        else:
            pass
            #  Deleting unnecsessary variables / list
            del arg
            del i

        # Returning the value
        return ASCIIdigits

    def DecimalToBinary(arg):
        pass