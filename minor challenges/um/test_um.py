# Importing responsories

import pytest
from um import count


def test_assertion():

    #   Creating strings to test
    a = "Um, thanks for the album"
    b = "Um, thanks, um.."
    c = "um?.. Its not an Umbrella"
    
    #   Counting how many 'um'
    assert count(a) == 1
    assert count(b) == 2
    assert count(c) == 1

    return True


if __name__ == '__main__':
  test_assertion()
