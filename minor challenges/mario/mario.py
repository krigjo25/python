"""
    Title : Mario more
    Description :   A program that prompts user for blocks
                    Create blocks based on user input

    Base by : CS50, Problem set 02
    Developed by : @krigjo25
    Date Started : 26.11-23
    Date Submited : Sunday, November 26, 2023 13:00 PM CET
    Date re-Submited : Sunday, November 26, 2023 13:43 PM CET

"""
from cs50 import get_int


#   Python version
def main():
    while True:
        n = get_int("Blocks : ")
        if n > 0 and n < 9:
            return simulate_blocks(n)

def simulate_blocks(n):

    #   Counting rows
    for i in range(n):
        # Space
        for j in range(n, i + 1, -1):
            print(" ", end="")

        #   Counting Hashes on the left side
        for j in range(i + 1):
            print("#", end="")

        print()

    #   Decrease by one
    n -= 1

    return


if __name__ == "__main__":
    main()
