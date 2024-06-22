def main():

    """
        Title       :   Sms Faces
        Author      :   krigjo25
        Description :
            Implements a program that prompts the user to
            type in a message with sms emojis

            USEAGE : In the terminal type python faces.py
            Follow the instructions given in the prompt.
    """
    return print(input('Type a message:').replace(':)', '\U0001F642').replace(':(', '\U0001F641'))


if __name__ == '__main__':
    main()
