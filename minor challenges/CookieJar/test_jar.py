#   Importing responsories
import pytest
from jar import Jar


def test_Constructor():


      #   Constructor test

  jar = Jar()

  # Testing the capacity
  jar.capacity = 1
  assert jar.capacity == 1


  jar.capacity = 12

  assert jar.capacity == 12

  jar.size = ''
  assert jar.size == 'zero cookies'

  return

def test_Deposit():

  jar = Jar()

  # Deposits one cookie
  jar.deposit(2)
  assert str(jar) == '🍪🍪'

  jar.deposit(10)
  assert str(jar) == '🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪'

  return

def test_withdraw():
  pass


def test_ValueError():

  jar = Jar()

  #   Testing ValueError for the Constructor

  with pytest.raises(ValueError):

    jar.capacity = 0
    assert jar.capacity == 0

    jar.capacity = -1
    assert jar.capacity == -1

  with pytest.raises(ValueError):

    jar.deposit(1)
    jar.deposit(13)

  with pytest.raises(ValueError):


    jar.withdraw(1)
    jar.withdraw(13)

  return