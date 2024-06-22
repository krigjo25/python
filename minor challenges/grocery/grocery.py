def main():
    '''
        #   Title       :   Grocery list
        #   Author      :   krigjo25
        #   Date        :   20.09-22
        #   Description :
                Implements a program that behaves like a grocery list
                it increases number of item if its already inputted.

                Usage : type in the terminal python grocery.py,
                wait for the prompt then type something

    '''

    #   initializing a dictionary called items
    items = {}

    while True:

        try:
            #   Prompting the user to input, case-insensitively
            item = str(input("")).upper()

        except EOFError:
            break

        #   Ensure the item is already inside the dictionary
        if item in items:

            #   Increase the item
            items[f'{item}'] += 1

        else:
            #   Registering the item
            items[f'{item}'] = 1

    #   Print out a sorted version of the dictionar
    for i in dict(sorted(items.items())):
        print(f'{items[i]} {i}')


if __name__ == '__main__':
    main()
