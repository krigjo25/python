class VanityPlates():

    '''
        VanityPlates

        1. Has to start with at least two letters :v:
        2. Length has to be maximum of 6 characters and no less than 2 characters :v:
        3. Numbers can only be at the end. (AAA222), (AAAAAA) not (AA22AA)(AA2AA2)
        4. Only numbers or letters and numbers can not start with 0 :v:
    '''

    def __init__(self):
        self.e = 'Invalid'

    def PlateValidation(self):

        #   Initializing variables
        plate = str(input('Plate: ').upper())

        #   Iterating throught the plate
        if self.CheckLengthAndSymbols(plate):
            if self.CheckTheNumbers(plate):

                if self.PlateDesign(plate): print('Valid')

                else : print(self.e)

            else: print(self.e)

        else: print(self.e)

        return

    def CheckLengthAndSymbols(self, arg):

        #   Checking if there is maximum of 6 character
        if len(arg) <= 6 and len(arg) > 1:

            #   Return True if arg is only number and letters
            if str(arg).isalnum(): return True
            else: return False

        else: return False

    def CheckTheNumbers(self, arg):

        '''
            Checking for the first digit in the string,
            if the number starts with 0 return false.
        '''

        #   Iterating through the argument
        for i in str(arg):

            #   Checking the first Integer
            if i.isdigit():
                if i.startswith('0'): return False
                else: return True

            else:
                continue

        return True

    def PlateDesign(self, arg):

        '''
                        PlateDesign
            If the numbers are in the middle of the prompt
            the user will recive an error.

        '''

        #   Checking if the first Two Characters is letters

        if str(arg[0:2]).isalpha():

            #   Checking if the numbers is at the end
            a = len(arg)

            if str(arg[2:]).isnumeric():return 'True'
            elif str(arg[3:]).isnumeric(): return 'True'
            elif str(arg[4:]).isnumeric(): return 'True'
            elif str(arg).isalpha(): return 'True'
            else: return False

        else: return False



if __name__ == '__main__':

    vp = VanityPlates()
    vp.PlateValidation()
