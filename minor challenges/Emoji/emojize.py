#   importing reposories
from emoji import emojize


def main():

    #   Prompting the user for the input
    prmpt = input("emoji : ")
    print(emojize(prmpt))


if __name__ == '__main__':
    main()
