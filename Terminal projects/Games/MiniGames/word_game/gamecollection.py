#   Importing Responsories
import os
import sys
import random as r
import time
from dotenv import load_dotenv

from pylib.db import SQLite as SQL
from pylib.apis import NinjaAPI, GenerateNames
from pylib.dictionary import GameOver, ScrabbleGame


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

            return lvl

    def EightBall(self):

        ''' Classic Eightball Game

        '''
        #   Print an output
        print("Ask the Philiosopher a question")

        #   Prompting the user for a question
        prompt = str(input("Question :" ))

        try:
            if prompt.isdigit(): raise ValueError()

        except ValueError as e:
            del prompt
            sys.exit("Math, Albert Einstein once said \" If i had one hour to solve a challange, i would use the 55minutes to contemplate on it, then the remaining 5 minutes to solve it.\"")
        
        quiz = prompt

        prompt = prompt.split(" ")

        #   Initializing an array
        arr = ['what', 'how']

        #   Ensure that prompt is in arr
        if prompt[0].lower() in arr: 
            prompt = GameOver().PhilisophicalAnswer()

        else:
            prompt = GameOver().DumbFacts() 

        print(f"Answer for {quiz}\n{prompt}")

        #  Clear Memory
        del quiz, prompt, arr

        return

    def Scrabble(self):

        ''' Classic Scrabble game

        '''
        #   Initializing lists
        score = []
        winner = []
        sorted_score = []

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

        prompt = input("Rock, Scissor or Paper : ")

        try :

            if str(prompt).lower() not in [ "rock", "scissor", "paper"]: raise ValueError("Choose between Rock, Scissors or paper")

        except Exception as e : 
            sys.exit(e)
        def RockScissorPaper(arg = None):

            dictionary = {
                    'rock':'\U0001FAA8',     #  rock
                    'scissor':'\U00002702',     #  ✂️
                    'paper':'\U0001F4C4'}     #  📄

            if arg == None:

                arg = ['rock', 'scissor', 'paper']
                #   Randomize the dictionary
                r.shuffle(arg)

                return dictionary.get(arg[r.randrange(len(arg))])

            return dictionary.get(arg)
       
        prompt = RockScissorPaper(prompt)  

        #   Computer chooses between one of Rock, Scissors and paper
        x = RockScissorPaper()

        #  Ensure the user and computer is tie
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

    def JumbleGame(self):

        #   Configure the game
        lvl = 1
        lives = 3

        #   Initializing the classes

        #   Initializing a list
        categories = [i for i in SQL('JumbleGame.db').SelectRecord("categories")]

        while True:

            category = []
            print(f"Please select one of the categories below:\n")

            #   Ensure the list is not the last element
            for i, j in enumerate(categories):

                if categories[i] != categories[-1]:
                    print(str(j['categories']).title(), end=", ")

                else:
                    print(str(j['categories']).title())
                category.append(j['categories'])

            #   Prepare and retrieve the category
            prompt = input("category > ").lower()
            prompt = str(prompt)

            try :

                #   Ensure the category doesn't exists
                for i, j in enumerate(category):
                    if prompt not in category[i] and len(category) == i:
                        raise Exception()

            except Exception as e: 
                print(f"Category \"{prompt}\", does not exists\nTry again\n")  
                continue

            if prompt == categories[0]['categories']:
                answer = NinjaAPI().Choice()
            else :
                category = []
                for i, j in enumerate(categories):
                    if prompt == categories[i]['categories']:
                        print(f"Select a sub category from {categories[i]['categories']}:\n", end="")

                        for k in categories[i]:

                            #   Up for improving
                            if categories[i][k] != categories[i]['id'] and categories[i][k] != categories[i]['categories'] and categories[i][k] != None:
                                category.append(categories[i][k])

            for i in range(len(category)):

                if category[i] != category[-1]:
                    print(f"{category[i]}, ".title(), end= "")
                else: print(f"{category[i]}\n".title())

            for i,j in enumerate(categories):
                if categories[i]['categories'] == prompt:
                    prompt = input("Type in a sub category>")
                    category = [i for i in SQL('JumbleGame.db').SelectRecord(categories[i]['categories'], prompt)] 

            #   Initializing lists
            word = []
            
            answer = []
            for i, j in enumerate(category):
                for k in category[i]:

                    answer.append(category[i][prompt])

            #   Randomizing the answer
            answer = list(dict.fromkeys(answer))
            r.shuffle(answer)
            answer = answer[r.randrange(0, len(answer))]

            begin = time.time()
            #   Prompting the user for a word
            prompt = input(f"Guess the jumbled word (q to quit) \"{''.join(r.sample(answer, len(answer)))}\">")
    
            counter = round(begin - time.time(), 2)

            word.append(prompt)

            for i in range(len(word)):

                #   Initializing a string
                string = ""

                #   Ensure the element is not the last element
                if word[i] != word[-1]: string =f"{word[i]}, "
                else: string += word[i]

            try :

                 if lives == 0: raise Exception('End of your lives')
                 elif "q" in prompt: raise Exception("User Quit") 

            except Exception as e:
                print(f"[ ! ] {e}\n[ ! ] Game Summary\n[ ! ] Words tried             : ({string})\n[ ! ] Number of Words guessed : ({lvl})\n[ ! ] The correct answer      : {answer}\n")
                break

            if str(prompt) != str(answer):
                lives -= 1
            else:

                #   Increments
                lvl += 1
                lives += 1

                print(f"[ ! ] words tried : ( {string} )\n[ ! ] Counted {len(word)} attempts.\n[ ! ] Your lives increased to {lives}.\n[ ! ] You've answered {lvl} words.\n[ ! ]{counter}s was used on this question\norrectly.\n")

            #   Clear Memories
            del string, prompt, answer
            del lives, word, counter
        return 
