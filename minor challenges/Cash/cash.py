"""
    Title :
            Cash

    Description :
                  A program that converts dollars to cents
                  Calculates Quarters,Dimes, Nickels,Pennies.
                  Calculates how many coins to retrieve from that dollar

    Base by : CS50, Problem set 01
    Solution by : @krigjo25
    Date Started : Sunday, November 26, 2023 08:00 AM CET
    Date Submited : Sunday, November 26, 2023 10:28 AM CET
    Date re-Submited : N/A

"""

import cs50


def Dollars():
    while True:
        d = input('$:')
        if d > 0:
            return d * 100


def main():
    #   prompt the customer
    cents = int(Dollars())

    # Calculate number of coins
    q = CalculateQuarters(cents)
    cents -= q * 25

    d = CalculateDimes(cents)
    cents -= d * 10

    n = CalculateNickels(cents)
    cents -= n * 5

    p = CalculatePennies(cents)
    cents -= p
    cents = q + d + n + p

    print(f"{int(cents)}")

    return


def CalculateQuarters(c):
    """
    1 Quarter = 25 cents
    """
    # Initialize variables
    q = 0

    while c > 24:
        q += 1
        c -= 25

    return q


def CalculateDimes(c):
    """
    1 Dime = 10 cents
    """
    # Initialize variables
    d = 0

    while c > 9:
        d += 1
        c -= 10

    return d


def CalculateNickels(c):
    """
    1 Nickels = 5 cents
    """
    # Initialize variables
    n = 0

    while c > 4:
        n += 1
        c -= 5

    return n


def CalculatePennies(c):
    """
    1 Pennie = 1 cent
    """

    # Initialize variables
    n = 0

    while c > 0:
        n += 1
        c -= 1

    return n


if __name__ == "__main__":
    main()
