
import sys

from gamecollection import WordGames
from pylib.dictionary import FrequentlyAskedQuestions
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

        #   Intigrated programs
        elif CommandlineInterface().CommandLineOptions().credits: 
            return CommandlineInterface().ProgramCredits()
                
        elif CommandlineInterface().CommandLineOptions().info: 
            return CommandlineInterface().Porgaminfo()

        elif CommandlineInterface().CommandLineOptions().games:
            return FrequentlyAskedQuestions.WordGames(CommandlineInterface().CommandLineOptions().games)
        
        elif CommandlineInterface().CommandLineOptions().eightball:
            return FrequentlyAskedQuestions.WordGames(CommandlineInterface().CommandLineOptions().eightball)
        
        elif CommandlineInterface().CommandLineOptions().rsp:
            return FrequentlyAskedQuestions.WordGames(CommandlineInterface().CommandLineOptions().rsp)
        elif CommandlineInterface().CommandLineOptions().scrabble:
            return FrequentlyAskedQuestions.WordGames(CommandlineInterface().CommandLineOptions().scrabble)
        
        else : raise Exception()

    except Exception as e:
        sys.exit("Usage : python wordgames.py -h or --help to view the command list")


if __name__ == "__main__":
    main()