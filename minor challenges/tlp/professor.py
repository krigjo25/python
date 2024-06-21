#   importing responsory
import random as r

def main():

  #   Prompting a level input
    lvl = get_level()

    # Calculating the integers
    x, y = generate_integer(lvl), generate_integer(lvl)

    #   Initializing the answer
    n = x + y

    #   Initializing Game Configurations
    lives = 3
    score = 0

    while True:

        try :

            #   Prompting the user for the output
            prompt = int(input(f'{x} + {y} ='))

        except ValueError:

            #   Decrease lives by one
            lives -= 1
            print("EEE")

        if prompt == n:

            #   Increasing the score
            score += 1

            #   Initializing the answer
            n = r.randint(0,10) + r.randrange(0,10)

        else:
            print("EEE")
            lives -= 1

        #   Breaking out of the loop
        if score == 9: return print(f"Score : {score}")
        if lives <= 0: return print(f"Correct number : {n} \n Score : {score}/9")


def get_level():

    '''
        Choosing the difficulty level,
        the level has to be a positive integer

    '''
    while True:

        try :

            lvl = int(input('level : '))

            if lvl >= 1 and lvl <= 3: return lvl

        except (ValueError, TypeError) as e:print(e)

        else:
            print('Choose a level between 1 & 3')
            continue


def generate_integer(lvl):

    if lvl == 1: return r.randint(0,10)
    elif lvl == 2: return r.randint(10, 99)
    elif lvl == 3: return r.randint(100, 999)


if __name__ == "__main__":
    main()
