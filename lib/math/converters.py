class MathConverter():

    def __init__(self):
        return

    def TextToASCIID(arg):

        '''

            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Creating a list of ASCII Decimal
            #   Checking if there is alphabetical letters in ASCIIdigits


        '''
        try :
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