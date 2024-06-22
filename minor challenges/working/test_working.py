#   Importing libraries
import pytest
from working import convert


def test_Working():

  assert TestConvert()

def TestConvert():

  #   Coverting AM to PM

  assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
  assert convert('9 PM to 9 AM') == '21:00 to 09:00'

  #   Coverting 12 to 0 viceversa
  assert convert('12 AM to 12 PM') == '00:00 to 12:00'

  return True

def test_exception():
  # Testing exception errors
  with pytest.raises(ValueError) as e:

    assert convert('9AM to 5PM') == e.value

  with pytest.raises(ValueError):

    assert convert('9 AM - 5 PM') == e.value

  with pytest.raises(ValueError):

    assert convert('09:00 to 05:00') == e.value

    with pytest.raises(ValueError):
      assert convert('13 AM to 26 PM') == e.value

if __name__ == '__main__':
  test_Working()
