#   Importing Responsories
import os
import sys
import time

import numpy as np
import random as r


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
        arr = np.array(['what', 'how'])

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
        score = np.array([])
        winner = np.array([])
        sorted_score = np.array([])

        print(f"Welcome to the Scrabble Game (terminal version) !\nAvailable dictionaries : :england:, :flag_us:")
        print(f"How to play : First you will be prompted for number of bots ask for your name\n then just type in a word to collect points.\nHowever if the word is false, no points is collected otherwise each letter has a point.\n")

        #   Initialize variables
        human = int(input("Number of players : "))
        bots = int(input("Number of bots to include in the game: "))

        #   Ensure total players has a greater value than 0

        if human > 0:
            for i in range(human):

                name = input(f"Player name : ")
                score = np.append(score,{'name': name, 'word': input(f"{name}'s word : "), 'points': 0})
        
        #   Ensure total bots has a greater value than 0
        if bots > 0 :
            for i in range(bots):
                score = np.append(score, { 'name': f'( Bot ) {GenerateNames().GenerateRandomNames(1)}', 'word': NinjaAPI().Choice(),'points': 0})

        for i in score:

            #   Ensure the word is actually a word
            if bool(NinjaAPI().Check(i['word'])):
                i['points'] = ScrabbleGame().ComputeScore(i['word'])

            #   Sorting the Score
            sorted_score = np.append(sorted_score, i['points'])
            sorted_score = np.sort(sorted_score, kind = 'mergesort')         

        #   Binary Search?
        for i in score:

            #   Appending winners to new dictionary
            if i['points'] == sorted_score[-1]:
                winner = np.append(winner,{
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

        BEGIN = time.time()

        #   Configure the game
        lvl = 1
        lives = 3

        #   Initializing a DataFrame
        categories = SQL('JumbleGame.db').SelectRecord("categories").drop("id", axis='columns')
        categories.infer_objects(copy=False)

        while True:

            try :

                 if lives == 0: raise Exception('End of your lives')

            except Exception as e:
                print(f"[ ! ] {e}\n[ ! ] Game Summary\n")
                break

            print(f"Please select one of the categories below:\n")

            for index, row in categories.iterrows():

                #   Ensure that the category is the same
                if categories['categories'].iloc[index] == categories['categories'].iloc[-1]:
                        print(f"{row['categories']}")

                else:
                    print(f"{row['categories']}, ", end= "")

            #   Prompt the user for an input
            prompt = input("category > ")
            prompt = str(prompt).title()

            for index, row in categories.iterrows():

                #   Ensure that the prompted message is equal to categories
                if categories['categories'].iloc[0] == prompt:
                    answer = NinjaAPI().Choice()

                else:
                    
                    try :

                        #   Ensure that the prompted category exists
                        if prompt.title() not in categories.values:

                            raise Exception('Category does not exists')

                    except Exception as e : 
                        print(e)
                        continue

                    #   Sub-categories
                    for index, row in categories.iterrows():

                        #   Ensure the row is equal to the prompted message
                        if prompt == row['categories']:

                            print(f'Type in a sub-category from {prompt} below:')
                            for i, j in enumerate(row):
                                if j != None:
                                    
                                    if row.iloc[i] != row.iloc[-1]:
                                        print(f"{j}, ", end="")

                                    else:
                                        print(f"{j} ")

                            #   Fetch answer
                            prompt = input('\nSub-Category >')

                            answer = SQL("JumbleGame.db").SelectRecord(f"{row['categories']}".lower(), f"{prompt}".title())
                            answer = answer.sample()
                            answer = answer.to_numpy()
                            print(answer[0][0])

            begin = time.time()
            print("secs ", round(time.time()-BEGIN, 2))
            #   Prompting the user for a word
            prompt = input(f"Guess the jumbled word (q to quit) \"{''.join(r.sample(answer[0][0], len(answer[0][0])))}\">")
    
            counter = round(begin - time.time(), 2)

            if str(prompt) != str(answer[0][0]):
                lives -= 1
                arg = f"[ ! ] The correct answer      : {answer}\n[ ! ] Your lives decreased as you missed on this one."

            else:

                #   Increments
                lvl += 1
                lives += 1

                arg = f"[ ! ] Your lives increased to {lives}.\n[ ! ] You've answered {lvl} words.\n[ ! ]{counter}s was used on this question\norrectly.\n"

            print(arg)
            #   Clear Memories
        del prompt, answer, lives
        del counter

        return 
