# Python Repositories
import random as r
import requests as req

from os import getenv

#   Dotenv Repositories
from dotenv import load_dotenv

#   Custom libraries
from pylib.databasePython import MariaDB

load_dotenv()

class Philosopher():

    '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Dictionary for Eightball game
    '''

    def __init__(self):
        return

    #   AskQ dictionaries
    def Answer(self):

        dictionary = {
                    1:'What do you sense about it?',
                    2:'What can  you actually do about it?',
                    3:'What are you really, deep down?',
                    4:'Just let it go, its not your issue.',
                    5:'Just let your self, experience the question.',
                    6:'Visualize the question, and the answer will arrive.',
                    7:'If an human is a genious, then The best answers always comes from with-in, just believe in your self enough.',
                    8:'As Socrates once said, you already know the answer of the question, since you had the idea of asking the question.',
                    9:'Would you be able to let it go?',
                    10:'A Question does not arise with out it\'s answer, so place your attention on where the question has arised',
                    11:'From where does the question actually arise? Your mind or heart?',
                    12:'Life is just like one of the elements on earth, just flow with it',
                    13:'Einstein said once if the world were ending, and i had one hour to solve a problem " i would use 50 minutes to think about the issue, then use the 10 last minutes to solve the issue".',
                    14:'As the thought araises from with-in it can only be answered from with-in',
                    15:'Answers comes from with-in your self.'
}

        #   Randomize the dictionary
        x = r.randrange(1,len(dictionary))

        return dictionary.get(x)

    def DumbFacts(self):

        dictionary = {
                        1:'Thoughts are like a librarynth, you will be lost',
                        2:'Dear lost boy, thoughts are like a labarynth you won\'t find the exit, when you take the wrong turn',
                        3:'When you search after an answer with why, it\'s like searching for something which doesn\'t exists.',
                        4:'life is why',
                        5:'Things tends to be what it is, neither less or more, but equal to what it is.',
                        6:'The opposite sides of a die will always add up to seven.',
                        7:'The King of Hearts is the only king in a deck of cards without a mustache.',
                        8:'There is always an answer with-in, just compenplate on it',
                        9:'Alaska is the only state whose name is on one row on a keyboard.',
                        10:'A "jiffy" is about one trillionth of a second.',
                        11:'The ocean is blue',
                        12:'Mulan has the highest kill-count of any Disney character.',
                        13:'The infinity sign is called a lemniscate.',
                        14:'why do you ask me?. '

}

        #   Randomize the dictionary
        x = r.randrange(1,len(dictionary))

        return dictionary.get(x)

class ReactionGame():

    '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Dictionary for Emoji game
    '''
    #   arg Game Dictionaries
    def RockScissorPaper(self):

        dictionary = {
                        1:'\U0001FAA8',          #  somewhat rock
                        2:'\U00002702',          #  ✂️
                        3:'\U0001F4C4'           #  📄
}

        #   Randomize the dictionary
        r.shuffle(dictionary)
        x = r.randrange(1,len(dictionary))

        return dictionary.get(x)

    def Computer(self, arg):

        #   Initializing variables
        bot = 'The Computer'
        string = "Python won\n"

        if arg == '\U0001FAA8':

            dictionary = {
                            1:f'Python won\nThat moment, when you realize stone doesn\'t play along with Scissors',
                            2:f'Congratulations, this game were Rock Hard !',
                            3:f'It were crushing days for the scissors',
                            4:f'Player Says : look behind you. **running away **.',
                            5:""
}
        elif arg == '\U0001F4C4':

            dictionary = {
                            1:f'{bot} sent your stone to North-Korea !',
                            2:f'You recieved a new stone as a christmas :gift:',
                            3:f'You have been mumified by {bot}',
                            4:""
}

        else:
        
            dictionary = {
                            1:f'Noone : \"\"\n{bot} : Oh snap',
                            2:f'The paper were succsessfully cut in two by {bot} ',
                            3:f'{bot} flexed with his scissors, you lost',
                            4: ""
}

        #   Randomize the dictionary
        x = r.randrange(1,len(dictionary))
        string += dictionary.get(x)

        return dictionary.get(x)

    def Player(self, arg, arg1):

        #   Initializing variables
        bot = 'Computer'
        string = "Player won\n"

        if arg == '\U0001FAA8':

            dictionary = {
                            1:f'{bot} had the idea of using a {arg1} against your {arg}, {bot} thought the {arg1} were strong enough to cut thorugh your {arg}, lets do a wii-match',
                            2:f'A thoughtful choice',
                            3:f'You just had a {arg}, while {bot} had the thought of {arg1} would be a grate choice.',
                            4:f'OH SNAP, you just scared {bot}, he never returned to the battle field.',
                            5:""
                    }

        elif arg == '\U0001F4C4':

            dictionary = {
                            1:f'{bot} threw {arg1} at you, but you grabbed it with his {arg}, and wrapped it into a :package: \n you gave a :package: to {bot}, how considerate of you !',
                            2:f'You wrappend {bot}\'s {arg1} into a :gift: and sent it to the North-Pole, Santa were stoned for the Christmas ',
                            3:f'You made a mumified version of {bot}',
                            4:""
                    }

        else:
        
            dictionary = {
                            1:f'Noone : \'\'\n{bot} : Oh snap',
                            2:f'You succsessfully cut the {arg1} with a {arg}',
                            3:f'you showed of with his :scissors: which he thought were a knife, but the goal were reached, {bot} ran.',
                            4:""
                    }

        #   Randomize the dictionary
        x = r.randrange(1,len(dictionary))
        string += dictionary.get(x)
        return dictionary.get(x)

class ScrabbleGame():

    '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Dictionary for Scrabble Game
    '''

    def ComputeScore(self, word):
        
        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Prompts the words for each player
            #   Calculating the score for both words
            #   Returning score from string

        '''

        #   Initializing variables
        result = 0
        word = str(word).lower()

        #   Initializing arrays
        alpha = [   'a', 'b', 'c', 'd',
                    'e', 'f', 'g', 'h',
                    'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p',
                    'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x',
                    'y', 'z']

        POINTS = [  1, 3, 3, 2,
                    1, 4, 2, 4, 
                    1, 8, 5, 1,
                    3, 1, 1, 3,
                    10, 1, 1, 1,
                    1, 4, 4, 8,
                    4, 10 ]

        for i in word: 
            if i in alpha: result += POINTS[alpha.index(i)]

        return result

    def CheckWord(self, arg):

        #print(bool(self.APINinja(arg)))
        #   Checking if api ninja has the word
        if APITools().NinjaCheck(arg): return True
        else: return False

class JumbleCategory():

    '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Dictionary for JumbleGame
    '''

    def __init__(self) -> None:
        pass


    def JumbleGenerator(self, jumble):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Shuffles the characters of the word
            #   Creating a new word with joining the elements of the iterator

        '''

        #   Shuffle the characters of the word
        jumble = r.sample(jumble, len(jumble))
    
        #   Join the elements of the iterator with particular character.
        jumble = ''.join(jumble)
        
        #   Returning the jumbled word
        return jumble

    def RetrieveCategory(self, category, sub):

        """
            #   Retrieve a category from the database,
            #   choose one of the selected values
        """

        category = str(category).lower().replace(" ", "")

        #   Initializing database connection
        db = MariaDB(database=getenv("db2"))

        try:

            word = db.SelectTable(category, sub)

            #   Counting the rows in the database
            x = db.RowCount(word) + 1

        except Exception as e : print(e)
        else:

            x = r.randint(1, x)

        #   Closing the connection
        db.closeConnection()

        #   Clear some space
        del x
        del db

        return  word[x]

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
        
        x = "Congratulation you guessed correct"

        #   Returning the value
        return x

    def IncorrectAnswer(self):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Dictionary for game losses
        '''

        x = r.randrange(0, 3)
        
        match x:
            case 0: x = "Incorrect Answer"
            case 1: x = "EEE"
            case 2: x = "Try again..."

        return x

    def TowTie(self):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Dictionary for game Ties
        '''

        #   Randomizing an integer
        x = r.randrange(0,2)

        #   Matching x
        match x:
            case 0 : x = "The computer draws a tie"
            case 1 : x = "let's tie a tie"
            case 2 : x = "What did the tie say to the bowtie?, What a tie"

        return x
 
class MathDictionary():

    def Operators(self):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Dictionary for game Won
        '''

        #   Randomizing an integer
        x = r.randrange(0,2)

        #   Matching x
        match x:
            case 0 : x = "+"
            case 1 : x = "-"
            case 2 : x = "/"
            case 3 : x = "*"

        return x

    def intGame(self, num, x):

        if x > num:


            dictionary = {
                            1:'Well well, we like the answer more humble than a greater answer',
                            2:'The given number is not humble enough, try again.',
                            3:'is greater than the answer ',
                            4:'Do you know why the equal sign are so humble? neither were less or greater !',
                            }

        elif x < num:

            dictionary = {
                            1:f"is less, we want more",
                            2:f'is less than i ask for',
                            3:f'is less akward than :100:',
                            4:f'is less humble',
                            }

        else:

            dictionary = {
                            1:f'Thank you for the humble answer, sir ',
                            2:f'Well thats equal..'
                           }

        #   Randomize the dictionary
        x = r.randrange(1,len(dictionary))

        #   Clear some space
        del x, num

        return dictionary.get(x)

class APITools():

    #   API-Ninja
    def NinjaCheck(self, word):

        """
            #   API by API-Ninja
            # Using an api to check if the word exist in the online dictionary.
        """

        parse = f'https://api.api-ninjas.com/v1/dictionary?word={word}'
        response = req.get(parse, headers={'X-Api-Key': getenv("DictionaryToken")})

        try:
            if response.text["valid"] == False: raise ValueError()

        except Exception : return False

        #   Clear some space
        del word
        del parse
        del response

        return 

    def NinjaChoice(self):

        '''
            #   API by API-Ninja
            #   API to choose a randomly generated word
        '''

        parse = 'https://api.api-ninjas.com/v1/randomword'
        response = req.get(parse, headers={'X-Api-Key': getenv("DictionaryToken")})
        string = ""

        try:

            if response.status_code != req.codes.ok: raise Exception("Something went wrong with the connection to Ninja API")
        except Exception as e : return e
        else:

            for i in response.text:
                if i.isalpha(): string += i

        #   Clear some space
        del parse, response

        return string
    
    def NinjaDefinition(self, word):

        """
            #   API by API-Ninja
            # Using an api to check wether the word exist or not.
        """
        print("Test ninja definition")
        parse = f'https://api.api-ninjas.com/v1/dictionary?word={word}'
        response = req.get(parse, headers={'X-Api-Key': getenv("DictionaryToken")})
        json = dict(response.json())

        try:
            if response.status_code != req.codes.ok: raise Exception(response.status_code)

        except Exception as e: return e
        else:

            for i, j in json.items(): 
                if "valid" in i :  json = j

        #   Clear some memory
        del word
        del parse
        del response

        return json

class Madlibs(): pass