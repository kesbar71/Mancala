# unit tests for Mancala game

import unittest
from Mancala import Mancala

class TestMancala(unittest.TestCase):
    def setUp(self):
        self.game = Mancala()

    def test_initial_state(self):
        self.assertEqual(self.game.board, [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0])

    def test_move(self):
        self.game.move(0)
        self.assertEqual(self.game.board, [0, 5, 5, 5, 5, 4, 1, 4, 4, 4, 4, 4, 4, 0])

    def test_move2(self):
        self.game.move(0)
        self.game.move(1)
        self.assertEqual(self.game.board, [0, 0, 6, 6, 6, 5, 1, 5, 5, 5, 5, 4, 4, 0])

    def test_move3(self):
        self.game.move(0)
        self.game.move(1)
        self.game.move(2)
        self.assertEqual(self.game.board, [0, 0, 0, 7, 7, 6, 2, 5, 5, 5, 5, 4, 4, 0])

    def test_move4(self):
        self.game.move(0)
        self.game.move(1)
        self.game.move(2)
        self.game.move(3)
        self.assertEqual(self.game.board, [0, 0, 0, 0, 8, 7, 2, 6, 6, 5, 5, 4, 4, 0])

    def test_move5(self):
        self.game.move(0)
        self.game.move(1)
        self.game.move(2)
        self.game.move(3)
        self.game.move(4)
        self.assertEqual(self.game.board, [0, 0, 0, 0, 0, 8, 3, 7, 7, 6, 5, 4, 4, 0])

    def test_move6(self):
        self.game.move(0)
        self.game.move(1)
        self.game.move(2)
        self.game.move(3)
        self.game.move(4)
        self.game.move

    def test_move7(self):
        self.game.move(0)
        self.game.move(1)
        self.game.move(2)
        self.game.move(3)
        self.game.move(4)
        self.game.move(5)
        self.assertEqual(self.game.board, [0, 0, 0, 0, 0, 0, 4, 8, 8, 7, 6, 5, 0, 1])

    def test_move8(self):
        self.game.move(0)
        self.game.move(1)
        self.game.move(2)
        self.game.move(3)
        self.game.move(4)
        self.game.move(5)
        self.game.move(7)
        self.assertEqual(self.game.board, [0, 0, 0, 0, 0, 0, 4, 0, 9, 8, 7, 6, 5, 1])

if __name__ == '__main__':
    unittest.main()

    