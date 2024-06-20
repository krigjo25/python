#   Importing responsories
import pytest
from plates import PlateValidation

def test_assertion_fails():

    #   Ensures that the program outputs the correct information
    assert PlateValidation('A') == False
    assert PlateValidation("AA()") == False
    assert PlateValidation('012345') == False
    assert PlateValidation('AA12AA') == False
    assert PlateValidation("@.AA12") == False
    assert PlateValidation("AA}]12") == False
    assert PlateValidation("AA12/-") == False
    assert PlateValidation('AAAAAAA') == False
    assert PlateValidation('1234567') == False
    assert PlateValidation('krigjo25') == False


def test_assertion_success():
    assert PlateValidation('CS50') == True
    assert PlateValidation('krigjo') == True
    assert PlateValidation('kak3') == True

