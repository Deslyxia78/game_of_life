import unittest
from game.game_of_life import GameOfLife

class TestGame(unittest.TestCase):
  def test_board_creation(self):
    coords = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
    gol = GameOfLife(coords, 0, True)
    grid = gol.game_of_life()
    self.assertEqual(grid.count_nonzero(), len(coords))

  def test_game_small_map_single_iteration(self):
    coords = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
    gol = GameOfLife(coords, 1, True)
    grid = gol.game_of_life()
    self.assertEqual(0, grid.count_nonzero())

  def test_game_large_map_single_iteration(self):
    coords = [(-2**64, 2**64),
              (2**64, 2**64),
              (-2**64, -2**64),
              (2**64, -2**64)]
    gol = GameOfLife(coords, 1, True)
    grid = gol.game_of_life()
    self.assertEqual(grid.count_nonzero(), 0)


if __name__ == '__main__':
  unittest.main()