#   Importing Responsories
import os
import sys
import random as r
from dotenv import load_dotenv

from pylib.apis import NinjaAPI, GenerateNames
from pylib.databasePython import MariaDB
from pylib.dictionary import JumbleCategory, GameOver, ScrabbleGame


load_dotenv()


class WordGames():


    def __init__(self): pass

    #   Game Configurations
    def GameLevel(self, lvl):

        '''
            #   Choosing the difficulty level of the game
            #   The level has to be greater than 0
        '''

        while True:


            try :
                #   Ensure the input is an integer
                if not str(lvl).isdigit() or lvl == None: 
                    raise ValueError("The level has to be an integer !")

                #   Ensure the input is greater than zero
                if int(lvl) < 1: 
                    raise ValueError("Choose an integer which is greater than zero")

            except ValueError as e: 
                sys.exit(f"USEAGE: In the terminal type intgame.py -h for commands.\n{e},")


            return int(lvl)

    def JumbleGame(self):

        #   Initializing the classes

        jumble = JumbleCategory()

        #   Configure the jumble Settings
        word = []
        
        sub = ""
        lives = 3
        lvl = self.GameLevel(input('Choose a level:'))


        for i in [i for i in MariaDB(database= os.getenv("database")).SelectTable("categories", "categories")]: 
            sub += f"{i}, ".capitalize()



        while True:

            print(f"Please select one of the categories below:\n\n{sub}")
            
            #   Prepare and retrieve the category
            prompt = input("category:")
            prompt = str(prompt).lower()

            try :

                if len(prompt) < 2: 
                    raise ValueError("Category has to contain more than one character")

                if prompt not in [i for i in MariaDB(database= os.getenv("database")).SelectTable("categories", "categories")]: 
                    raise ValueError("Category does not exits")

            except ValueError as e: 
                print(e)

        

            if prompt in category[0]: 
                answer = NinjaAPI().Choice()
            else:

                try :

                    #   Fetch sub categories from database
                    category = MariaDB(database=os.getenv("database")).SelectRow("categories", prompt )

                except Exception as e: 

                    print(e)

                sub = ""

                #   Iterate through the categories and add category to variable
                for i in category[2:]:
                    sub += f"{i}, "

                print(f"Selected category {category[1]}\n{sub}")
                
                prompt = input("Type in a category:")

                #   Fetching the answer from the database
                answer = MariaDB(database=os.getenv("database")).SelectColumn(category[1], "roles", prompt, "characters")

                #   Randomizing the answer
                answer = answer[r.randrange(0, len(answer))]      
                

            #   Clear memories
            del category, sub
            del prompt

            #   Declear a string variable
            string = ""
        
            #   The confusing answer
            virvel = jumble.JumbleGenerator(answer)

            #   Prompting the user for a word
            prompt = input(f"Guess the jumbled word (q to quit): \"{virvel}\"")

            try :
                 if lives == 0: raise Exception()
                 elif "q" in prompt: raise Exception("User Quit") 

            except Exception as e:

                print(e)
                sys.exit(f"Game Summary\nWords tried : ({string})\n\nThe correct answer : {answer}")
                

            word.append(prompt)

            if prompt == answer:

                for i in word: 
                    string += f"{i} "

                print(f'words tried : ( {string} )\nCounted {len(word)} attempts.\n{GameOver().RandomCorrectAnswer()}')

            
           

            #   #   Clear some memories
            del word, string
            del virvel, prompt
            del answer, lives

    def EightBall(self):

        ''' Classic Eightball Game

        '''

        #   Initializing an array
        arr = ['what', 'how']

        #   Print an output
        print("Ask the Philiosopher a question")

        #   Prompting the user for a question
        prompt = str(input("Question :" ))
        quiz = prompt

        prompt = prompt.split(" ")

        
        #   Ensure that prompt is in arr
        if prompt[0].lower() in arr: 
            prompt = GameOver().PhilisophicalAnswer()

        else:
            prompt = GameOver().DumbFacts() 

        print(f"Answer for {quiz}\n{prompt}")

         #  Clear memories
        del quiz, prompt

        return

    def Scrabble(self):

        ''' Classic Scrabble game

        '''
        #   Initializing list / Dictionaries
        score = []
        winner = []
        sorted_score = []

        #   Prompts the words for both players
        print(f"Welcome to the Scrabble Game (terminal version) !\nAvailable dictionaries : :england:, :flag_us:")
        print(f"How to play : First you will be prompted for number of bots ask for your name\n then just type in a word to collect points.\nHowever if the word is false, no points is collected otherwise each letter has a point.\n")

        #   Initialize variables
        human = int(input("Number of players : "))
        bots = int(input("Number of bots to include in the game: "))
        
        

        #   Ensure total players has a greater value than 0
        if human > 0:

            for i in range(human):

                name = input(f"Player name : ")
                score.append({'name': {name}, 'word': input(f"{name}'s word : "), 'points': 0})
        
        #   Ensure total bots has a greater value than 0
        if bots > 0 :

            for i in range(bots):
                score.append({ 'name': f'( Bot ) {GenerateNames().GenerateRandomNames(1)}', 'word': NinjaAPI().Choice(),'points': 0})

        for i in score:

            #   Ensure the word is actually a word
            if NinjaAPI().Check(i['word']):
                i['points'] = ScrabbleGame().ComputeScore(i['word'])

            #   Sorting the Score
            sorted_score.append(i['points'])
            sorted_score = sorted(sorted_score)         

        for i in score:

            #   Appending winners to new dictionary
            if i['points'] == sorted_score[-1]:
                winner.append({
                                'name': i['name'],
                                'word': i['word'],
                                'points': i['points']
                })

        #   Clear Memories
        del human, bots, score
        del sorted_score


        if len(winner) > 1:
            print(f'There were a tie between {len(winner)} players.')
            for i in winner:
                print(f"{i['name']} with the word {i['word']}, tied the round with {i['points']} points")
            return

        else:
            for i in winner:
                return print(f"{i['name']} with the word {i['word']}, won the round with just {i['points']} points")

    def RockScissorPaper(self):

        '''
            #   Author : krigjo25
            #   Date   :  12.01-23

            #   Prompt the user for a string
            #   Combine the answers
            #   Send a philliosofically answer

        '''


        prompt = str(input("Rock, Scissors or Paper : ")).lower()

        try :

            #   Error messages
            if prompt not in [ "rock", "scissors", "paper"]: 
                raise ValueError("Choose between Rock, Scissors or paper")

        except Exception as e : 
            sys.exit(e)

        def RockScissorPaper(arg = ['Rock', 'Scissor', 'Paper']):

            dictionary = {
                    'rock':'\U0001FAA8',     #  rock
                    'scissor':'\U00002702',     #  ✂️
                    'paper':'\U0001F4C4'}     #  📄

            if arg == None:

                #   Randomize the dictionary
                r.shuffle(arg)

                return dictionary.get(arg[r.randrange(len(arg))])
            return dictionary.get(arg)
       
        prompt = RockScissorPaper(prompt)
            
        #   Computer chooses between one of Rock, Scissors and paper
        x = RockScissorPaper()

        #   Check for winner and print out output
        if prompt == x: sys.exit(GameOver().RandomTowaTieAnswer())
        else:

            #   If the user win
            if prompt == '\U0001F4C4' and x =='\U0001FAA8': print(f" {GameOver().Player(prompt,x)}")
            if prompt == '\U0001FAA8' and x =='\U00002702': print(f" {GameOver().Player(prompt,x)}")
            if prompt == '\U00002702' and x =='\U0001F4C4': print(f" {GameOver().Player(prompt,x)}")

                #   if the bot wins
            if x == '\U0001F4C4' and prompt =='\U0001FAA8': print(f"{GameOver().Computer(x)}")
            if x == '\U0001FAA8' and prompt =='\U00002702': print(f"{GameOver().Computer(x)}")
            if x == '\U00002702' and prompt =='\U0001F4C4': print(f"{GameOver().Computer(x)}")

            #   Clear Memories
            del x, prompt
                
        return

