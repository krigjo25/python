"""
    Title : Readability
    Description :   Readability based on Coleman-Liau formula

    Base by : krigjo25, CS50 Problem set 02
    Developed by : @krigjo25
    Date Started : 26.11-23
    Date Submited : Sunday, November 26, 2023 16:00 PM CET
    Date re-Submited : Sunday, November 26, 2023 17:39 PM CET

"""

# Importing Responsories
from cs50 import get_string


def main():
    return ColemanLiauFormula(get_string("Calculate Sentence: "))


def LetterCount(text):
    count = 0
    for i in text:
        if str(i).isalpha():
            count += 1

    # Clean up unused variables
    del text

    return count


def WordCount(text):
    count = 0

    # reference Python Docs str module
    # https://docs.python.org/3/library/stdtypes.html?highlight=str%20split#str.split

    for i in str(text).split():
        count += 1

    #   Clean up unsused variables
    del text

    return count


def SentenceCount(text):
    count = 0
    sep = [".", "!", "?"]

    for i in str(text):
        if i in sep:
            count += 1

    #   Clean up unsused variables
    del sep, text

    return count


def ColemanLiauFormula(text):
    l = LetterCount(text)
    w = WordCount(text)
    s = SentenceCount(text)

    #   Calculates The Readability
    l = (l / w) * 100
    s = (s / w) * 100
    cli = round((0.0588 * l) - (0.296 * s) - 15.8)

    if cli < 1:
        print("Before Grade 1")
    elif cli > 15:
        print("Grade 16+")
    else:
        print(f"Grade {cli}")

    #   Clean up unused variables
    del l, w, s, cli
    return


if __name__ == "__main__":
    main()
