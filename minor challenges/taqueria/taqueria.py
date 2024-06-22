def main():

    '''
        Title   : Taqueria Shop
        author  : krigjo25
        Description :
            Usage : type in the terminal python taqueria.py,
            wait for the prompt then type something
    '''
    #   Initializing a counter variable
    n = 0

    #   Initializing a dicitionary
    menu = {
                "Baja Taco": 4.00, "Burrito": 7.50,
                "Bowl": 8.50, "Nachos": 11.00,
                "Quesadilla": 8.50, "Super Burrito": 8.50,
                "Super Quesadilla": 9.50, "Taco": 3.00,
                "Tortilla Salad": 8.00}
    while True:

        try:

            #   Initializing Prompt
            item = str(input('Item :').title())

            if item in menu:
                n += menu[item]

        except EOFError as e:
            break

        print('$%.2f' % (n))

main()
