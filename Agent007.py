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


class CSPAgent():

    def __init__(self, env=None, end_game_on_mine_hit=True):
        self.env = env
        self.end_game_on_mine_hit = end_game_on_mine_hit
        self.all_constraint_equations = list()
        self.non_mine_variables = list()
        self.mine_variables = list()
        self.game_stuck = False
        self.game_won = False

    def _create_constraint_equation_for_variable(self, variable):
        row = variable.row
        column = variable.column
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (i == 0 and j == 0):
                    continue

                if (row + i >= 0 and column + j >= 0 and row + i < self.env.n and column + j < self.env.n):

                    # If a neighbour is already clicked, then do not add it to the constraint equation.
                    if self.env.opened[row + i, column + j]:
                        continue

                    # If a neighbour is already flagged, then do not add it to the equation but subtract the constraint value
                    # of the current variable.
                    if self.env.flags[row + i, column + j]:
                        variable.constraint_value -= 1
                        continue

                    neighbour = self.env.variable_mine_ground_copy[row + i, column + j]
                    variable.add_constraint_variable(variable=neighbour)

        # Append the equation in the global equation list
        self.all_constraint_equations.append(
            [variable.constraint_equation, variable.constraint_value])

    def _visualise_equations(self):
        for equation in self.all_constraint_equations:
            print(repr([(variable.row, variable.column)
                        for variable in equation[0]]), " = ", equation[1])

    def _remove_duplicates(self, array):

        # Create an empty list to store unique elements
        uniqueList = []

        # Iterate over the original list and for each element
        # add it to uniqueList, if its not already there.
        for element in array:
            if element not in uniqueList:
                uniqueList.append(element)

        # Return the list of unique elements
        return uniqueList

    def _resolve_subsets(self):

        # Sort all equations in increasing order of their length
        self.all_constraint_equations = sorted(
            self.all_constraint_equations, key=lambda x: len(x[0]))

        # Start resolving subsets
        for equation in self.all_constraint_equations:
            for equation_ in self.all_constraint_equations:

                if equation == equation_ or not equation[0] or not equation_[0] or not equation[1] or not equation_[1]:
                    continue

                # Check if the equation is a subset of the other equations
                if set(equation[0]).issubset(set(equation_[0])):
                    equation_[0] = list(set(equation_[0]) - set(equation[0]))
                    equation_[1] -= equation[1]
                    continue

                # Check if the equation is a superset of the other equations
                if set(equation_[0]).issubset(set(equation[0])):
                    equation[0] = list(set(equation[0]) - set(equation_[0]))
                    equation[1] -= equation_[1]

        # After resolving subsets, check if now we can get mine and non-mine variables
        # from the equations.
        self._check_equations_for_mine_and_non_mine_variables()

    def _backtrack(self):
        return

    def _check_equations_for_mine_and_non_mine_variables(self):

        for equation in self.all_constraint_equations.copy():

            # If the equation becomes empty i.e. all its variables are removed
            if len(equation) == 0 or len(equation[0]) == 0:
                self.all_constraint_equations.remove(equation)
                continue

            # If value is 0, all variables in that equation are non-mine variables.
            if equation[1] == 0:
                self.all_constraint_equations.remove(equation)
                for non_mine_variable in equation[0]:
                    if not self.env.opened[non_mine_variable.row, non_mine_variable.column] and \
                            non_mine_variable not in self.non_mine_variables:
                        self.non_mine_variables.append(non_mine_variable)
                continue

            # If value is equal to the length of the equation, then all the variables
            # in the equation are min variables for sure.
            if len(equation[0]) == equation[1]:
                self.all_constraint_equations.remove(equation)
                for mine_variable in equation[0]:
                    if not self.env.flags[mine_variable.row, mine_variable.column] and mine_variable not in self.mine_variables:
                        self.mine_variables.append(mine_variable)

    def _remove_variable_from_other_equations(self, variable, is_mine_variable=False):
        for equation in self.all_constraint_equations:
            if variable in equation[0]:
                equation[0].remove(variable)

                if is_mine_variable and equation[1]:
                    equation[1] -= 1

    def _add_mine_flag(self, cell):
        self.env.add_mine_flag(cell.row, cell.column)
        self._remove_variable_from_other_equations(
            variable=cell, is_mine_variable=True)

    def _open_mine_cell(self, cell):
        self.env.open_mine_cell(cell.row, cell.column)
        self._remove_variable_from_other_equations(
            variable=cell, is_mine_variable=True)

    def _click_square(self, cell):
        self.env.click_square(cell.row, cell.column)

        # If game is over, it means we clicked on a mine. If we dont want to end the game on mine hit
        # then reset the mine_hit variable, open the mine and continue with the game.
        if self.env.mine_hit and not self.end_game_on_mine_hit:
            self._open_mine_cell(cell=cell)
            return

        self._create_constraint_equation_for_variable(variable=cell)
        self._remove_variable_from_other_equations(variable=cell)

    def _check_solvable_csp(self):
        return (not self.non_mine_variables and not self.mine_variables)

    def _click_random_square_with_heuristic(self):

        unopened_cells = dict()
        open_cell_coords = list(zip(*np.where(self.env.opened)))

        for row, column in open_cell_coords:
            open_cell = self.env.variable_mine_ground_copy[row, column]

            # Get number of open mines
            number_of_cell_mines_found = open_cell.get_flagged_mines(
                env=self.env)

            # Calculate risk for the open cell
            risk = open_cell.value - number_of_cell_mines_found

            # Get all the neighbours which are still yet to be opened
            unopened_cell_neighbours = open_cell.get_unopened_neighbours(
                env=self.env)

            # Assign the same risk value to each of the neighbours
            for cell_neighbour in unopened_cell_neighbours:

                if cell_neighbour not in unopened_cells:
                    unopened_cells[cell_neighbour] = 0

                unopened_cells[cell_neighbour] += risk

        if not unopened_cells:
            self.game_stuck = True
            return

        # Choose the unopened cell with the minimum risk.
        random_cell = min(unopened_cells, key=unopened_cells.get)
        self._click_square(random_cell)

    def _click_random_square(self):
        unopened_cells_coords = list(zip(*np.where(~self.env.clicked)))

        if not unopened_cells_coords:
            return

        random_cells = [self.env.variable_mine_ground_copy[row, col]
                        for (row, col) in unopened_cells_coords]
        random_cell = np.random.choice(random_cells)
        self._click_square(random_cell)

    def _click_all_non_mine_cells(self):
        while(self.non_mine_variables):
            non_mine_variable = self.non_mine_variables.pop(0)
            self._click_square(non_mine_variable)

    def _flag_all_mine_cells(self):
        while(self.mine_variables):
            mine_variable = self.mine_variables.pop(0)
            self._add_mine_flag(mine_variable)

    def _basic_solver(self):

        # Open up all non-mine cells
        self._click_all_non_mine_cells()

        # First remove any duplicate equations we may have
        # added in the knowledge base.
        self.all_constraint_equations = self._remove_duplicates(
            self.all_constraint_equations)

        # Add flags to all mine cells
        self._flag_all_mine_cells()

        # Find more non-mine and mine variables
        self._check_equations_for_mine_and_non_mine_variables()

    def get_gameplay_metrics(self):
        metrics = dict()
        metrics["number_of_mines_hit"] = self.env.number_of_mines_hit / \
            self.env.number_of_mines
        metrics["number_of_mines_flagged_correctly"] = len(list(zip(
            *np.where(self.env.mines & self.env.flags.astype(bool) & ~self.env.mine_revealed))))
        metrics["number_of_cells_flagged_incorrectly"] = len(
            list(zip(*np.where(~self.env.mines & self.env.flags.astype(bool)))))
        metrics["final_score"] = metrics["number_of_mines_flagged_correctly"] / \
            self.env.number_of_mines
        return metrics

    def play(self):

        self.non_mine_variables.append(
            self.env.variable_mine_ground_copy[0, 0])
        while(True):

            # Always see if we can solve the minesweeper using a basic solver
            self._basic_solver()

            # Condition to end the game
            all_flags_equal_to_mines = list(
                zip(*np.where(self.env.mines))) == list(zip(*np.where(self.env.flags)))
            all_clicked = np.all(self.env.clicked)

            # If we are stuck at a game position, where no new moves can be made
            # then we just click randomly.
            if self.game_stuck:
                self.game_stuck = False
                self._click_random_square()

            # If we hit a mine, then we lost the game
            if self.env.mine_hit:
                self.game_won = False
                return

            # If not the above two cases, then check if we clicked on all cells.
            if all_clicked:

                # If all the mines are properly flagged, then we won
                if all_flags_equal_to_mines:
                    self.game_won = True
                else:
                    self.game_won = False
                return

            # Update all equations in our knowledge base which are subsets of each other
            # whenever we run out of non-mines and mines
            if self._check_solvable_csp():
                self._resolve_subsets()

                # If everything fails, then click randomly
                if self._check_solvable_csp():
                    self._click_random_square_with_heuristic()


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
