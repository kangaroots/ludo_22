import unittest

from LudoGame import Player, LudoGame


class MyTestCase(unittest.TestCase):
    def test_case_0_from_readme(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 6), ('A', 4),
                 ('A', 6), ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4)]
        game = LudoGame()
        self.assertEqual(game.play_game(players, turns), ['28', '28', '21', 'H'])

    def test_case_1(self):
        players_1 = ['A', 'B', 'C', 'D']
        turns_1 = [('A', 6), ('A', 1), ('B', 6), ('B', 2), ('C', 6), ('C', 3), ('D', 6), ('D', 4)]
        game = LudoGame()
        self.assertEqual(game.play_game(players_1, turns_1), ['1', 'H', '16', 'H', '31', 'H', '46', 'H'])

    def test_case_2(self):
        players_2 = ['A', 'B']
        turns_2 = [('B', 6), ('B', 4), ('B', 5), ('B', 4), ('B', 4), ('B', 3), ('B', 4), ('B', 5), ('B', 4), ('B', 4),
                   ('B', 5), ('B', 4), ('B', 1), ('B', 4), ('B', 5), ('B', 5), ('B', 5)]
        game = LudoGame()
        self.assertEqual(game.play_game(players_2, turns_2), ['H', 'H', 'B6', 'H'])

    def test_case_3(self):
        players_3 = ['A', 'B']
        turns_3 = [('A', 6), ('A', 3), ('A', 6), ('A', 3), ('A', 6), ('A', 5), ('A', 4), ('A', 6), ('A', 4)]
        game = LudoGame()
        self.assertEqual(game.play_game(players_3, turns_3), ['28', '28', 'H', 'H'])

    def test_case_4(self):
        players_4 = ['A', 'C']
        turns_4 = [('A', 6), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 6), ('A', 4), ('A', 6), ('A', 4), ('A', 6),
                 ('A', 6), ('A', 6), ('A', 4), ('A',
                                                6), ('A', 6), ('C', 6), ('C', 4)]
        game = LudoGame()
        self.assertEqual(game.play_game(players_4, turns_4), ['33', 'H', '32', 'H'])

    def test_case_5(self):
        players_5 = ['A', 'B']
        turns_5 = [('A', 6), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 6), ('A', 4), ('A', 6), ('A', 4), ('A', 6),
                   ('A', 6), ('A', 4), ('A', 6), ('A',4), ('A', 6), ('A', 6), ('A', 4), ('A', 6), ('A', 6), ('A', 4),
                   ('A', 6), ('A', 6), ('A', 4), ('A', 6), ('A', 3), ('A', 6), ('B', 6), ('A', 6)]
        game = LudoGame()
        self.assertEqual(game.play_game(players_5, turns_5), ['E', 'E', 'R', 'H'])

    def test_case_6(self):
        players_6 = ['A', 'B']
        turns_6 = [('A', 6), ('A', 2), ('A', 2), ('A', 6), ('A', 4), ('A', 5), ('A', 4), ('A', 4), ('B', 6), ('B', 3),
                   ('A', 6), ('A', 3)]
        game = LudoGame()
        self.assertEqual(game.play_game(players_6, turns_6), ['3', 'H', '17', 'H'])

    def test_case_7(self):
        players_7 = ['A', 'B']
        turns_7 = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 4), ('A', 5), ('A', 5),
                   ('A', 3), ('A', 5), ('A', 3), ('A', 6)]
        game = LudoGame()
        self.assertEqual(game.play_game(players_7, turns_7), ['A1', 'R', 'H', 'H'])

    def test_case_8(self):
        players_8 = ['A', 'B']
        turns_8 = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('A', 4), ('A', 4), ('A', 5), ('A', 4), ('A', 5), ('A', 5),
                   ('A', 3), ('A', 5), ('A', 5), ('A', 6), ('A', 5), ('A', 5), ('A', 3), ('B', 6), ('B', 3), ('A', 4)]
        game = LudoGame()
        self.assertEqual(game.play_game(players_8, turns_8), ['E', '13', '17', 'H'])

    def test_case_9(self):
        players_9 = ['A', 'B']
        turns_9 = [('A', 6), ('A', 4), ('A', 4), ('A', 4), ('A', 6), ('A', 5), ('A', 3), ('B', 6), ('B', 2), ('A', 2),
                   ('A', 4)]
        game = LudoGame()
        self.assertEqual(game.play_game(players_9, turns_9), ['16', '10', 'H', 'H'])


if __name__ == '__main__':
    unittest.main()
