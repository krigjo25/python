#   Testing
#   Imporing responsories
import pytest

from twttr import shorten


#   Ensures the program works as expected
def test_assertion():

    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'

if __name__ == "__main__":
    test_assertion()
