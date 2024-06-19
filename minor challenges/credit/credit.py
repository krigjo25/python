'''
    Title : Credit
    Description :   A program that prompts user for credit card

    Base by : CS50, Problem set 07
    Developed by : @krigjo25
    Date Started : 16.11-23

'''

def main(): return CreditDebitCard()

def CreditDebitCard():

    """
        #   Prompting the user for numbers
        #   Check if promted message is digits

        #   For each second number multiply with 2
        #   For every second element in array even single number, sum them together
        #   For every odd single number, sum them together
        #   Sum the even and odd numbers
        #   If the result is divisible by 10, Card valid, else Invalid
    """

    while True:

      try:

        #   Prompting the user for a credit card number
        n = input("Credit Card Number : ")

        #   Reversing the order of the array
        array = [int(i) for i in n]

        #   Check if promted message is digits
        if not str(n).isdigit(): raise Exception("INVALID CREDIT CARD")
        #   Checking the length of the prompted message
        elif len(n) > 19 or len(n) < 12: raise Exception ("INVALID CREDIT CARD")

      except Exception as e:
        print(f"{e}, Try again..")
        continue

      else:

        #   Checking for VISA
        if int(n[0]) == 4 and len(n)< 17: n = "VISA"
        else:

            # Checking for American Express
            for i in range(34,37,3):
              if int(n[0:2]) == i and len(n) == 15: n = "AMEX"

            #   Checking for MASTER CARD
            for i in range(51,55):
              if int(n[0:2]) == i and len(n) == 16: n = "MASTERCARD"

        # Initializing variables
        x = 0

        # Fetching every even indexes
        for i in array[0::2]:

          i = array.index(i)

          # Multiple every second element by two
          array[i] = array[i] * 2

          #     Summing the two digits values together
          print(array)

          if array[i] > 9:

            array[i] = str(array[i])
            array[i] = int(array[i][0]) + int(array[i][1])

          x += array[i]

        y = 0

        for i in array[1::2]:
          i = array.index(i)
          y = y + array[i]

        # Iterating over every elements in the array
        #for i in array[1::2]: x += array[i]

        x += y
        #   Summing both values together
      if x % 10 == 0: print(n)
      else:
        print("INVALID")

      del x, array, n

      return False

if __name__ == "__main__": main()
