
def main():

        #   Print converted text
        print(shorten(input("Type a text with vowels:")))

        return

def shorten(arg):

    #   Initializing variables
    string = ''

    #   Initializing a list with vowels
    x = [   'a','e','i','o','u',
            'A','E','I','O','U',
        ]

    for i in str(arg):

        if i not in x:
            string += i

    #   Clear memories
    del arg

    return string

if __name__ == '__main__':
    main()
