#   Importing Python responsories
import sys
import csv

#   Tabulate responsory
from tabulate import tabulate

def main():

    """
        #   Author      :   @krigjo25
        #   Date        :   30.08-22
        #   Description :   Implements a command-line program to
                read a csv file
    """

    try:

        #   Ensures the user to use two argument which one of them is a csv
        if len(sys.argv) !=2: raise Exception('Usage python pizza.py [infile path] [outfilepath]')
        elif '.csv' not in sys.argv[1]: raise Exception('Please make sure the file is a CSV')

    except Exception as e:
        sys.exit(e)

    return CSVReader()

def CSVReader():
    try:
        #   Open and print the file
        with open(f'{sys.argv[1]}', 'r') as f:

            #   append the csv file into a list called table
            table = [i for i in csv.DictReader(f)]

            #   print the tabulated table
            return print(tabulate(table, headers = "keys", tablefmt = 'grid'))

    except FileNotFoundError as e:
        sys.exit(e)
if __name__ == '__main__':
    main()
