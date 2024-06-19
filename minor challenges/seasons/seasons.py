#   Importing Responsories
import sys, inflect, datetime

def main():
    '''
        #   Title       :
                Date to text

        #   Description :
              print out given date into words

        #   Usage
             python dates.py When prompted use (YYYY-MM-DD)'''

    return print(Date_to_min(input('Date of birth :')))




def Date_to_min(arg):

    #   Initializing variables
    today = datetime.date.today()
    arg = [i for i in str(arg).split('-')]

    try :
        if len(arg) != 3 or len(arg[0]) != 4 or int(arg[1]) > 12:
            raise Exception('Invalid date format, use YYYY-MM-DD')

    except Exception as e:
        sys.exit(e)

    #   Calculating the difference between the dates
    arg = datetime.date(int(arg[0]), int(arg[1]), int(arg[2]))
    arg = today - arg

    #   Calculating the minutes since inputted date
    arg = f'{1440 * arg.days}'
    arg = f'{inflect.engine().number_to_words(arg, andword='').capitalize()} minutes'

    #   Clear memories
    del today

    return arg

if __name__ == "__main__":
    main()
