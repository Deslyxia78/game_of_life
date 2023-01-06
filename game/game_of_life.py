import sys
from scipy.sparse import dok_matrix

class GameOfLife:

  def __init__(self, coords, iterations = 10, test = False):

    self.isTest = test
    self.iterations = iterations

    # Get min/max x and y
    x_coords, y_coords = zip(*coords)
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)

    # Compute number of rows and columns
    self.rows = max_x - min_x + 1
    self.cols = max_y - min_y + 1

    # Create initial grid all zeros
    self.grid = dok_matrix((self.rows, self.cols), dtype=int)

    # Set the cells at given coordinates to `Alive`
    for x, y in coords:
      self.grid[x - min_x, y - min_y] = 1

  def print_grid(self):
    # Get grid dimensions
    rows, cols = self.grid.shape

    # Initialize the string representation of the grid
    grid_str = ''

    # Iterate over rows of the grid
    for row in range(rows):
      # Iterate columns
      for col in range(cols):
        # Append '*' if cell is a 1, or '.' if it is zero
        grid_str += '*' if self.grid[row, col] == 1 else '.'
      # Append a newline character at the end of each row
      grid_str += '\n'

    # Return the string representation of the grid
    return grid_str

  def traverse(self, row, col, grid):

    to_check = dok_matrix((self.rows, self.cols), dtype=int)
    # Get neighbor count from 8 surrounding neighbors
    # while protecting against OOB errors
    neighbors = 0
    for dx in [-1, 0, 1]:
      for dy in [-1, 0, 1]:
        if dx == 0 and dy == 0:
          continue
        if 0 <= row + dx < self.rows and 0 <= col + dy < self.cols:
          neighbors += grid[row + dx, col + dy]
          if grid[row + dx, col + dy] == 0:
            to_check[dx, dy] = 0

    return neighbors, to_check

  def game_of_life(self):

    for i in range(self.iterations):
      # Copy grid to calculate next generation
      next_gen = self.grid.copy()
      dead_check = dok_matrix((self.rows, self.cols), dtype=int)

      # Iterate the grid keys looking to kill alive cells
      for row, col in self.grid.keys():
        neighbors, to_check = self.traverse(row, col, self.grid)

        if self.grid[row, col] == 1 and (neighbors < 2 or neighbors > 3):
          next_gen[row, col] = 0

        # Iterate to_check and add new keys to dead_check
        for tc_row, tc_col in to_check.keys():
          dead_check[tc_row, tc_col] = 0

      # Iterate the dead_check keys looking to create alive cells
      for row, col in dead_check.keys():
        neighbors, _ = self.traverse(row, col, dead_check)

        if neighbors == 3:
          next_gen[row, col] = 1

      # Update grid for new iteration
      self.grid = next_gen
    if not self.isTest:
      print(self.print_grid())
    return self.grid

def main():
  # Read coord list from STDIN
  coord_list = [tuple(map(int, line.strip().strip('()').split(','))) for line in sys.stdin]

  # Create an instance of the GameOfLife class
  game = GameOfLife(coord_list)

  # Run the game of life
  game.game_of_life()

if __name__ == '__main__':
  main()