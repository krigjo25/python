#   Importing responsories
import sys
from pylib.command_line_tool import CommandlineInterface
from pylib.gamecollection import IntegerGames as ig

def main():

        #   Ensure the arguments is less than two
        try :
            if len(sys.argv) < 2: 
                raise Exception('Usage: python intgame.py -h to view the commands')
        except Exception as e: 
            sys.exit(e)

        cmd = CommandlineInterface()
            
        if cmd.CommandLineOptions().info: 
            return cmd.Porgaminfo()
        
        elif cmd.CommandLineOptions().tlp: 
            return ig().LittleProffessor()

        elif cmd.CommandLineOptions().gtn: 
            return ig().GuessTheNumber()

if __name__ == '__main__':
    main()