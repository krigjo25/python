def main():

    x = 0
    while True:

        try:

            #   Initializing Prompt
            prmpt = str(input('Item :').title())

            #   Initializing dicitionary
            dictionary = {
                            "Baja Taco": 4.00,
                            "Burrito": 7.50,
                            "Bowl": 8.50,
                            "Nachos": 11.00,
                            "Quesadilla": 8.50,
                            "Super Burrito": 8.50,
                            "Super Quesadilla": 9.50,
                            "Taco": 3.00,
                            "Tortilla Salad": 8.00}

            if prmpt in dictionary:
                x += dictionary[prmpt]

        except EOFError as e:
            print(e)
            break

        else :
            print('$%.2f' % (x))

if __name__ == '__main__':
    main()
