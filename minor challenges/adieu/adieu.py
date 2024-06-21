#   Import responsories
import inflect

def main():

    """
        Title : Adieu, Adieu so long farwell
        Description :

            Implemented a program that sings the song
            So long farewell - The movie The Sound Of Music,
            https://www.youtube.com/watch?v=Qy9_lfjQopU
            where the implemented names is created by the user

            Usage : type in the terminal python adieu.py,
            wait for the prompted message then type in some names.

    """
    #   Initializing constant lists
    name = []

    #   Creating a loop to iterate through the program
    while True:

        try:
            #   Prompt user for name
            x = str(input('name :')).capitalize()
            if len(x) == 0: raise EOFError()

        except EOFError:
            break

        #   Append name
        name.append(x)

    print(f'Adieu, adieu, to {inflect.engine().join(name, final_sep=",")}')


main()
