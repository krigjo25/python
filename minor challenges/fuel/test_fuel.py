#   Importing responsories
import pytest
from fuel import convert, gauge


def test_Convert():

    #   Ensuring it works as expected
    assert convert("1/100") == "E"
    assert convert("50/100") == "50%"
    assert convert("99/100") == "F"


#   Ensuring dividing with zero raises an exception
def test_raiseZeroDivisionError():
    with pytest.raises(ZeroDivisionError) as e:

        assert convert("1/0") == e
        assert convert("32/0") == e


#   Ensuring the program raises an Value Error when the last number is less than the first
def test_raiseValueError():

    with pytest.raises(ValueError) as e:

        assert convert("a/b") == e

    with pytest.raises(Exception) as e:

        assert convert("2/1") == e
        assert convert("200/1") == e
