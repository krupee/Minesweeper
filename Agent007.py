from gameboard import Game
from random import randrange, seed
import numpy as np


def is_number(a):
    # will be True also for 'NaN'
    try:
        number = float(a)
        return True
    except ValueError:
        return False


def make_None_matrix(m):
    dim = len(m[0])
    for i in range(dim):
        for j in range(dim):
            m[i, j] = None
    return m


def get_Information_Board(m):
    dim = len(m[0])
    m1 = np.zeros_like(m)
    for i in range(dim):
        for j in range(dim):
            m1[i, j] = get_info_at(m, i, j)
    return m1


def get_info_at(m, i, j):
    neigh_sum = 0
    dim = len(m[0])
    for l in [-1, 0, 1]:
        for k in [-1, 0, 1]:
            if is_valid(i+l, j+k, dim):
                neigh_sum += m[i+l, j+k]
    return neigh_sum


def is_valid(i, j, dim):
    if i < 0 or j < 0:
        return False
    if i > dim-1 or j > dim - 1:
        return False
    return True


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.flag = 0  # 0 = unknown, 1 = safe, 2 = mine
        self.numNeighbors = 0
        self.numAdjacentMines = 0
        self.numAdjacentSafe = 0
        self.numAdjacentHidden = 0

        self.dim = dim
        self.degree = np.zeros([dim, dim])
        self.probability = np.zeros([dim, dim]) + 1.0
        # 0 if only zero is possible , 1 if only one value is possible. 2 if both are possible
        self.possible_values = make_None_matrix(np.zeros([dim, dim]))
        self.known_board = make_None_matrix(np.zeros([dim, dim]))
        # all explored nodes are 1 remaining zeros
        self.explored_board = np.zeros([dim, dim])
        self.current_state = np.zeros([dim, dim])
        self.constraint_list = []
        self.safe_cells = []
        self.mines = []
        self.isVariable = np.zeros([dim, dim])


def calculateAdj(self, tile):
    x = tile.x
    y = tile.y
    safe = 0
    hidden = 0
    mines = 0
    clue = self.grid[x][y]

    for r in range(-1, 2):
        for c in range(-1, 2):
            if (r == 0 and c == 0):
                continue
            row = r + x
            column = c + y
            if (row < self.gird_size and row >= 0 and column < self.gird_size and column >= 0):
                if (self.grid_display[row][column] == "#"):
                    hidden = hidden + 1
                elif (self.grid_display[row][column] == "F"):
                    mines = mines + 1
                else:
                    safe = safe + 1

# Uncovers all neighbors of a given cell


def revealNeighbors(self, row, col):
    for r in range(-1, 2):
        for c in range(-1, 2):
            if (r == 0 and c == 0):  # Current cell
                continue
            if (row + r >= 0 and col + c >= 0 and row + r < self.gird_size and col + c < self.gird_size and (self.grid_display[row+r][col+c] == '#' and not self.grid_display[row+r][col+c] == 'F')):
                self.uncoverCell(row+r, col+c)


# Flags all neighbors of a given cell
def flagNeighbors(self, row, col):
    for r in range(-1, 2):
        for c in range(-1, 2):
            if (r == 0 and c == 0):  # Current cell
                continue
            if (row + r >= 0 and col + c >= 0 and row + r < self.gird_size and col + c < self.gird_size and (self.grid_display[row+r][col+c] == '#' and not self.grid_display[row+r][col+c] == 'F')):
                self.grid_display[row+r][col+c] = 'F'

# Counts number of flagged mines around current cell


def bombsAroundCell(self, row, col):
    count = 0
    for r in range(-1, 2):
        for c in range(-1, 2):
            if (r == 0 and c == 0):  # Current cell
                continue
            if (row + r >= 0 and col + c >= 0 and row + r < self.gird_size and col + c < self.gird_size and self.grid_display[row+r][col+c] == 'F'):
                count = count + 1
    return count


def safeAroundCell(self, row, col):
    count = 0
    for r in range(-1, 2):
        for c in range(-1, 2):
            if (r == 0 and c == 0):  # Current cell
                continue
            if (row + r >= 0 and col + c >= 0 and row + r < self.gird_size and col + c < self.gird_size and self.grid_display[row+r][col+c] == '#'):
                count = count + 1
    return count


def numNeighbors(self, x, y):
    count = 0
    for r in range(-1, 2):
        for c in range(-1, 2):
            if (r == 0 and c == 0):
                continue
            row = r + x
            column = c + y
            if (row < self.gird_size and row >= 0 and column < self.gird_size and column >= 0):
                count = count + 1
    return count


def play(self):
    game = Game(4, 2)
    old_grid = None
    current_grid = self.grid_display
    while not np.array_equal(current_grid, old_grid):
        old_grid = current_grid
        current_grid = Agent007(game)


'''
self.mineindicator(self.gird_size)
self.show()
print()
self.showGrid()
print()
self.showVisited()
print()

x = 0
y = 0

while (True):



self.grid_display[x][y] = self.grid[x][y]
self.visited[x][y] = True
tile = Tile(x, y)
self.numAdjacentSafe = calculateAdj(self, tile)
self.show()
print(numNeighbors(self, tile))
'''


'''
for x in range(self.gird_size):
print()
stri = []
for y in range(self.gird_size):
curr = Tile(x, y)
stri.append(self.grid[x][y])

print(stri)
#self.cells.append(curr)
'''

# for curr in self.cells:
#print(curr.x, curr.y, curr.flag)


game = Game(4, 1)
size = game.gird_size
game.mineindicator(size)
basicAgent(game)

'''

0 2 # #
1 2 # #
# # # #
# # # #


- Pick (random)
- Populate Tile with Hidden, Safe, Mine values
- Check if any revealed tiles neighbors == clue OR if clue == 0, then make everything safe/mine
- Pick (random)




When clue == # hidden neighbors


'''
