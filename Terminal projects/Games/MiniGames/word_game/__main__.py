
import sys
from pylib.command_line_tool import CommandlineInterface
from gamecollection import WordGames

def main(): 
        
    """
        Command-line tool to interact with the games
    """

    try :
        if len(sys.argv) < 2: raise Exception("Usage : python wordgames.py -h or --help to view the command list")

    except Exception as e:
        sys.exit(e)
        
    if CommandlineInterface().CommandLineOptions().rsp: 
        return WordGames().RockScissorPaper()

    elif CommandlineInterface().CommandLineOptions().scrabble: 
        return WordGames().Scrabble()
        
    elif CommandlineInterface().CommandLineOptions().eight: 
        return WordGames().EightBall()
        
    elif CommandlineInterface().CommandLineOptions().jumble: 
        return WordGames().JumbleGame()

        #   Game Guides
    elif CommandlineInterface().CommandLineOptions().credits: 
        return CommandlineInterface().ProgramCredits()
            
    elif CommandlineInterface().CommandLineOptions().info: 
        return CommandlineInterface().Porgaminfo()
    elif CommandlineInterface().CommandLineOptions().faq_rps:
        return CommandlineInterface().faqrps()
    elif CommandlineInterface().CommandLineOptions().faq_eightball:
        return CommandlineInterface().faqeightball()
    elif CommandlineInterface().CommandLineOptions().faq_jumble:
        return CommandlineInterface().faqjumble()
    elif CommandlineInterface().CommandLineOptions().faq_scrabble:
        return CommandlineInterface().faqscrabble()

if __name__ == "__main__":
    main()