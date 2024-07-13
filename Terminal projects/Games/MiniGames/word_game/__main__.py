
import sys

from gamecollection import WordGames
from pylib.dictionary import FrequentlyAskedQuestion
from pylib.command_line_tool import CommandlineInterface


def main(): 
        
    """
        Command-line tool to interact with the games
    """

    try :
        if len(sys.argv) < 2: raise Exception()
        #   Games

        if CommandlineInterface().CommandLineOptions().rspGame:
            return WordGames().RockScissorPaper()

        elif CommandlineInterface().CommandLineOptions().scrabbleGame: 
            return WordGames().Scrabble()
            
        elif CommandlineInterface().CommandLineOptions().eightballGame: 
            return WordGames().EightBall()
            
        elif CommandlineInterface().CommandLineOptions().jumbleGame: 
            return WordGames().JumbleGame()

        #   Faq
        elif CommandlineInterface().CommandLineOptions().credits: 
            return CommandlineInterface().ProgramCredits()
                
        elif CommandlineInterface().CommandLineOptions().info: 
            return CommandlineInterface().Porgaminfo()

        elif CommandlineInterface().CommandLineOptions().games:
            print(CommandlineInterface().CommandLineOptions().games)
            return FrequentlyAskedQuestion.WordGames(FrequentlyAskedQuestion().WordGames(str(CommandlineInterface().CommandLineOptions().games)))

        else : raise Exception()

    except Exception as e:
        sys.exit(f"USEAGE : python wordgames.py -h or --help to view the command list\n{e}")


if __name__ == "__main__":
    main()