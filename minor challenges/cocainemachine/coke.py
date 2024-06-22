def main ():

    """
        Title       :   Cocaine Machine
        author      :   krigjo25
        Description :
            A program to insert specific coins to pay a due bill.
            USAGE : type in the terminal python coke.py,
            wait for the prompt then type some integers which is listed.
    """

    #   Initializing Ammount due
    x = 50

    #   Initializing a list
    coins = ['5', '10', '25', '50']

    #   Creating a while loop to iterate the program
    while True:

        #   prompt the user for a coin
        print(f'Amount Due: {x}')
        coin = input('')

        try:

            #   Ensure the that the coin type is in coins list
            if coin not in coins:
                raise ValueError(f"Amount Due: {x}")

        except ValueError as e:
            return print(e)

        #   Substract owned coins
        x -= int(coin)

        #   Ensures that x is less than one before breaking out of the loop
        if x < 1:
            break

    return print(f"Change Owed: {abs(x)}")

if __name__ == '__main__':
    main()
