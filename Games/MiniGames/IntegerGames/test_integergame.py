#   Importing Responsories
import pytest

#   Importing local libraries
from games import WordGames

class TestWordGames:

    wg = WordGames

    def test_EightBall(self):

        w = WordGames()
        assert w.EightBall('what') == 'what'
        assert w.EightBall('how') == 'what'
        assert w.EightBall('why') == 'what'

        return
    
    def test_EightBall(self):

        w = WordGames()
        assert w.RockScissorPaper('\U0001F4C4') == 'what'
        assert w.RockScissorPaper('\U0001FAA8') == 'what'
        assert w.RockScissorPaper('\U00002702') == 'what'

        return
