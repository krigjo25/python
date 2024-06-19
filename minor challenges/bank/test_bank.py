#   Import responsories
import pytest
from bank import value


def test_func():

    assert value('hello') == "$0"
    assert value('hey') == "$20"
    assert value('else') == "$100"


if __name__ == "__main__":
    test_func()
