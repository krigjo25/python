#   Importing Python responsories
import os
import sys
import csv


def main():
    """
    #   Author :    krigjo25
    #   Date :      30.08-22

    #   Expects the user to provide two command-line arguments
    #   If the user does not provide exactly two command-line arguments
    #   if the first cannot be read, the program should exit via sys.exit with an error message.

    """

    #   Ensuring the arguments
    if len(sys.argv) != 3:
        sys.exit("Usage : python scourgify.py  [infile] [filepath]")

    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    else:
        return CSVWriter()


def CSVWriter():
    """
    #   Author :    krigjo25
    #   Date :      06.09-22

    #   Description :
            Cleans a csv file, by sortinging it firstname, lastname and removing strings

    """

    #   Initializing a list
    student = []

    #   Open the csv file & write to a new CSV file
    with open(f"{sys.argv[1]}") as f, open(f"{sys.argv[2]}", "w") as w:
        try:

            #   Iterating through the CSV file & sorting the name by first-/lastname
            for i in csv.DictReader(f):

                #   Handling the strings
                j, k = i["name"].split(",")
                j, k = j.lstrip(), k.lstrip()

                #   Appending to list
                student.append({"first": k, "last": j, "house": i["house"]})

            #   Writing to another file
            columns =

            #   Create a header
            cw = csv.DictWriter(w, fieldnames=["first", "last", "house"])
            cw.writeheader()

            #   Write the rows
            cw.writerows(student)

            #   Close the file
            f.close()
            w.close()

        #   Except an exception if occures
        except FileNotFoundError as e:
            sys.exit("CSV is corrupted")


if __name__ == '__main__':
    main()
