#   Importing Responsories
import random as r
from os import getenv


class MathGame():

    #   Integer games
    def GuessTheNumber(self, n, x):

        if x < n:

            dictionary = {
                            1:'Well well, we like the answer more humble than a greater answer',
                            2:'The given number is not humble enough, try again.',
                            3:'is less than the answer ',
                            4:'Do you know why the equal sign are so humble? neither were less or greater !',
                            5:""
                            }

            string = f"{x} is less than n\n"

        elif x > n:

            dictionary = {
                            1:f'{x} is greater than n',
                            2: ""
                            }
            string = f"{x} is greater than n\n"
        
        else:

            dictionary = {
                            1:f'What a humble answer !',
                            2:f'{x} is equal to {n}',
                            3:f'How is 10 + 10 equal to 11 + 11?\nBecause 11 + 11 = 22 (twenty too)',
                            4:f'*What does 1 plus 1 equal? (Dinner for 2)',
                            5:""
                        }

            string = f" "

        #   Randomize the dictionary
        print(len(dictionary))
        x = r.randrange(1,len(dictionary))

        string += dictionary.get(x)

        #   Clear some memory
        del dictionary, x, n

        return string

    def GenerateIntegers(self, lvl):

        #   Matching the argument

        if lvl <= 10: return r.randrange(0, lvl * 10)
        elif lvl > 10 and lvl < 20:

            #   Match the level
            match lvl :
                case 11: return r.randrange(0, 200)
                case 12: return r.randrange(0, 300)
                case 13: return r.randrange(0, 400)
                case 14: return r.randrange(0, 500)
                case 15: return r.randrange(0, 600)
                case 16: return r.randrange(0, 700)
                case 17: return r.randrange(0, 800)
                case 18: return r.randrange(0, 900)
                case 19: return r.randrange(0, 1000)

        elif lvl >=20 and lvl < 30: return r.randrange(0, lvl * 10)


        return
    #   Little Proffessor
class GameOver():

    '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Dictionary for game won, losses, tie
    '''

    def __init__(self):
        return


    #   When the answer is correct
    def CorrectAnswer(self):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Dictionary for game Won
        '''

        dictionary =  {
                        1:'Congratulation you guessed correct',
                        2:'',
                    }

        #   Randomize the dictionary
        x = r.randrange(1,len(dictionary))

        #   Returning the value
        return dictionary.get(x)

    def IncorrectAnswer(self):
        
        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Dictionary for game losses
        '''

        dictionary = {
                        1:f'Game Over.',
                        2:'The answer were not humble enough.',
                        3:'Not the answer which were requested.',
                    }

        #   Randomize the dictionary
        x = r.randrange(1,len(dictionary))

        return dictionary.get(x)

    def TowTie(self):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Dictionary for game Ties
        '''
        dictionary = {

                    1:f'The computer draws a tie',
                    2:'let\'s tie a tie',
                    3:'What did the tie say to the **bowtie**? You\'re a weirdo',
                    4:f'The cumputer drawing a toe.',
                    5:f'Thank you for the humble answer, sir ',
                    6:f'Well thats equal..'
                }

        #   Randomize the dictionary
        x = r.randrange(1,len(dictionary))

        return dictionary.get(x)
