import pytest
import mock
from pylib.gamecollection import WordGames
from pylib.dictionary import GameOver

class TestCaseConfig():

    go = GameOver
    wg = WordGames()

class GameTest(TestCaseConfig):

    def test_Eightball(self):
        ''' As the answers is random, it may be impossible to test functionallity for random strings'''
        #   Calculate the chance of getting the same answer again

        #   Test inputs
        #   Analyzes the chance to get duplicate results
        assert self.go.PhilisophicalAnswer()
        assert self.go.DumbFacts()
 
        assert self.wg.EightBall() 


    def test_exceptions(self):
        pass

    def test_Scrabble(self):
        pass

    def test_exception(self): pass

    def test_RSP(self): pass

    def test_exceptions(self):pass
    
    def test_jumbleGame(self):pass

    def test_jumbleexceptions(self):pass