import random as r

def GameLevel():

    '''
        Choosing the difficulty level,
        the level has to be a positive integer

    '''
    while True:

        try :

            lvl = int(input('level : '))

            if lvl > 0: return lvl

        except (ValueError, TypeError) as e:
            print(e)
            continue

def GuessTheNumber():

    #   Prompting a level input & randomizing the n
    lvl = GameLevel()
    n = r.randint(1,lvl)

    while True:

        #   Prompting the user
        try :
            x = int(input('Guess: '))

            if x < 1: pass

        except (ValueError, TypeError) as e: continue

        else:
            #   Comparing the values

            if x == n: return print('Just right!')
            elif x > n: print(f'Too large!')
            else: print(f'Too small!')

GuessTheNumber()