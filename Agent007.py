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


def Agent007(self, grid_size, num_mines):
    mine_hit = False
    game_won = False
    game_stuck = False
    non_mine_var = list()
    mine_var = list()
    # temp = [randrange(self.gird_size), randrange(self.gird_size)]
    a = randrange(grid_size)
    b = randrange(grid_size)
    temp = (a, b)
    print(a, b)
    print(temp[0])
    print(temp[1])
    self.uncoverCell(temp[0], temp[1])
    if (self.grid_display[temp[0]][temp[1]] == "*"):
        mine_hit = True
        print('MINE HIT')
    else:
        print('NOT A MINE')

    flagCount = 0
    while ((mine_hit is False) and (self.mine_count != flagCount)):
        print("flagcount", flagCount)
        self.show()
        print()
        mine_hit = True

        for x in range(grid_size):

            for y in range(grid_size):
                print(self.grid_display[x][y])
                self.show()
                print()
                # Current cell is already revealed
                if (is_number(self.grid_display[x][y])):
                    # Case 1
                    # print("here")
                    continue
                # Curret cell is already flagged
                elif (str(self.grid_display[x][y]) is 'F'):
                    # Case 2
                    flagCount = flagCount + 1
                    # print("f inc", flagCount)
                    continue
                # Just revealed current cell and its a mine :(
                elif (str(self.grid_display[x][y]) is '*'):
                    # print("Hit a Mine! You Lose!")
                    mine_hit = True
                    # print("here")
                    break
                # else:
                #     self.uncoverCell(x, y)
                #     clue = self.grid[x][y]
                #     if (self.grid_display[x][y] == "*"):
                #         lose = True
                #         break
                #     if (clue == 0):
                #         # All safe around cell
                #         revealNeighbors(self, x, y)
                #     elif (clue == 8):
                #         # All mines around me
                #         flagNeighbors(self, x, y)
                #     else:
                #         # Corner/edge cases
                #         if (clue == bombsAroundCell(self, x, y)):
                #             revealNeighbors(self, x, y)
                #         elif (clue == safeAroundCell(self, x, y)):
                #             flagNeighbors(self, x, y)

            if (mine_hit is True):
                break
    self.show()


grid_size = 4
num_mines = 1
game = Game(grid_size, num_mines)
size = game.gird_size
Agent007(game, grid_size, num_mines)
print()
# def _create_constraint_equation(self, variable):
#     row = variable.row
#     print(row)
#     column = variable.column
#     print(column)

#     for i in [-1, 0, 1]:
#         for j in [-1, 0, 1]:
#             if (i == 0 and j == 0):
#                 continue

#             if (row + i >= 0 and column + j >= 0 and row + i < self.grid.length and column + j < self.grid.length):

#                 # If a neighbour is already clicked, then do not add it to the constraint equation.
#                 if self.grid.opened[row + i, column + j]:
#                     continue

#                 # If a neighbour is already flagged, then do not add it to the equation but subtract the constraint value
#                 # of the current variable.
#                 if self.grid.flags[row + i, column + j]:
#                     variable.constraint_value -= 1
#                     continue

#                 neighbour = self.grid.variable_mine_ground_copy[row + i, column + j]
#                 variable.add_constraint_variable(variable=neighbour)

#     # Append the equation in the global equation list
#     self.all_constraint_equations.append(
#         [variable.constraint_equation, variable.constraint_value])

# def _visualise_equations(self):
#     for equation in self.all_constraint_equations:
#         print(repr([(variable.row, variable.column)
#                     for variable in equation[0]]), " = ", equation[1])

# def _remove_duplicates(self, array):

#     # Create an empty list to store unique elements
#     uniqueList = []

#     # Iterate over the original list and for each element
#     # add it to uniqueList, if its not already there.
#     for element in array:
#         if element not in uniqueList:
#             uniqueList.append(element)

#     # Return the list of unique elements
#     return uniqueList

# def _resolve_subsets(self):

#     # Sort all equations in increasing order of their length
#     self.all_constraint_equations = sorted(
#         self.all_constraint_equations, key=lambda x: len(x[0]))

#     # Start resolving subsets
#     for equation in self.all_constraint_equations:
#         for equation_ in self.all_constraint_equations:

#             if equation == equation_ or not equation[0] or not equation_[0] or not equation[1] or not equation_[1]:
#                 continue

#             # Check if the equation is a subset of the other equations
#             if set(equation[0]).issubset(set(equation_[0])):
#                 equation_[0] = list(set(equation_[0]) - set(equation[0]))
#                 equation_[1] -= equation[1]
#                 continue

#             # Check if the equation is a superset of the other equations
#             if set(equation_[0]).issubset(set(equation[0])):
#                 equation[0] = list(set(equation[0]) - set(equation_[0]))
#                 equation[1] -= equation_[1]

# After resolving subsets, check if now we can get mine and non-mine variables
# from the equations.
# self._check_equations_for_mine_and_non_mine_variables()

# def _backtrack(self):
#     return

# def _check_equations_for_mine_and_non_mine_variables(self):

#     for equation in self.all_constraint_equations.copy():

#         # If the equation becomes empty i.e. all its variables are removed
#         if len(equation) == 0 or len(equation[0]) == 0:
#             self.all_constraint_equations.remove(equation)
#             continue

#         # If value is 0, all variables in that equation are non-mine variables.
#         if equation[1] == 0:
#             self.all_constraint_equations.remove(equation)
#             for non_mine_variable in equation[0]:
#                 if not self.grid.opened[non_mine_variable.row, non_mine_variable.column] and \
#                         non_mine_variable not in self.non_mine_variables:
#                     self.non_mine_variables.append(non_mine_variable)
#             continue

#         # If value is equal to the length of the equation, then all the variables
#         # in the equation are min variables for sure.
#         if len(equation[0]) == equation[1]:
#             self.all_constraint_equations.remove(equation)
#             for mine_variable in equation[0]:
#                 if not self.grid.flags[mine_variable.row, mine_variable.column] and mine_variable not in self.mine_variables:
#                     self.mine_variables.append(mine_variable)

# def _remove_variable_from_other_equations(self, variable, is_mine_variable=False):
#     for equation in self.all_constraint_equations:
#         if variable in equation[0]:
#             equation[0].remove(variable)

#             if is_mine_variable and equation[1]:
#                 equation[1] -= 1

# def _add_mine_flag(self, cell):
#     self.grid.add_mine_flag(cell.row, cell.column)
#     self._remove_variable_from_other_equations(
#         variable=cell, is_mine_variable=True)

# def _open_mine_cell(self, cell):
#     self.grid.open_mine_cell(cell.row, cell.column)
#     self._remove_variable_from_other_equations(
#         variable=cell, is_mine_variable=True)

# def _open_square(self, cell):
#     self.grid.open_square(cell.row, cell.column)

#     # If game is over, it means we clicked on a mine. If we dont want to end the game on mine hit
#     # then reset the mine_hit variable, open the mine and continue with the game.
#     if self.grid.mine_hit and not self.end_game_on_mine_hit:
#         self._open_mine_cell(cell=cell)
#         return

#     self._create_constraint_equation(variable=cell)
#     self._remove_variable_from_other_equations(variable=cell)

# def _check_solvable_csp(self):
#     return (not self.non_mine_variables and not self.mine_variables)

# def _click_random_square_with_heuristic(self):

#     unopened_cells = dict()
#     open_cell_coords = list(zip(*np.where(self.grid.opened)))

#     for row, column in open_cell_coords:
#         open_cell = self.grid.variable_mine_ground_copy[row, column]

#         # Get number of open mines
#         number_of_cell_mines_found = open_cell.get_flagged_mines(
#             grid=self.grid)

#         # Calculate risk for the open cell
#         risk = open_cell.value - number_of_cell_mines_found

#         # Get all the neighbours which are still yet to be opened
#         unopened_cell_neighbours = open_cell.get_unopened_neighbours(
#             grid=self.grid)

#         # Assign the same risk value to each of the neighbours
#         for cell_neighbour in unopened_cell_neighbours:

#             if cell_neighbour not in unopened_cells:
#                 unopened_cells[cell_neighbour] = 0

#             unopened_cells[cell_neighbour] += risk

#     if not unopened_cells:
#         self.game_stuck = True
#         return

#     # Choose the unopened cell with the minimum risk.
#     random_cell = min(unopened_cells, key=unopened_cells.get)
#     self._click_square(random_cell)

# def _click_random_square(self):
#     unopened_cells_coords = list(zip(*np.where(~self.grid.clicked)))

#     if not unopened_cells_coords:
#         return

#     random_cells = [self.grid.variable_mine_ground_copy[row, col]
#                     for (row, col) in unopened_cells_coords]
#     random_cell = np.random.choice(random_cells)
#     self._click_square(random_cell)

# def _click_all_non_mine_cells(self):
#     while(self.non_mine_variables):
#         non_mine_variable = self.non_mine_variables.pop(0)
#         self._click_square(non_mine_variable)

# def _flag_all_mine_cells(self):
#     while(self.mine_variables):
#         mine_variable = self.mine_variables.pop(0)
#         self._add_mine_flag(mine_variable)

# def _basic_solver(self):

#     # Open up all non-mine cells
#     self._click_all_non_mine_cells()

#     # First remove any duplicate equations we may have
#     # added in the knowledge base.
#     self.all_constraint_equations = self._remove_duplicates(
#         self.all_constraint_equations)

#     # Add flags to all mine cells
#     self._flag_all_mine_cells()

#     # Find more non-mine and mine variables
#     self._check_equations_for_mine_and_non_mine_variables()

# def get_gameplay_metrics(self):
#     metrics = dict()
#     metrics["number_of_mines_hit"] = self.grid.number_of_mines_hit / \
#         self.grid.number_of_mines
#     metrics["number_of_mines_flagged_correctly"] = len(list(zip(
#         *np.where(self.grid.mines & self.grid.flags.astype(bool) & ~self.grid.mine_revealed))))
#     metrics["number_of_cells_flagged_incorrectly"] = len(
#         list(zip(*np.where(~self.grid.mines & self.grid.flags.astype(bool)))))
#     metrics["final_score"] = metrics["number_of_mines_flagged_correctly"] / \
#         self.grid.number_of_mines
#     return metrics

# def play(self):

#     self.non_mine_variables.append(
#         self.grid.variable_mine_ground_copy[0, 0])
#     while(True):

#         # Always see if we can solve the minesweeper using a basic solver
#         self._basic_solver()

#         # Condition to end the game
#         all_flags_equal_to_mines = list(
#             zip(*np.where(self.grid.mines))) == list(zip(*np.where(self.grid.flags)))
#         all_clicked = np.all(self.grid.clicked)

#         # If we are stuck at a game position, where no new moves can be made
#         # then we just click randomly.
#         if self.game_stuck:
#             self.game_stuck = False
#             self._click_random_square()

#         # If we hit a mine, then we lost the game
#         if self.grid.mine_hit:
#             self.game_won = False
#             return

#         # If not the above two cases, then check if we clicked on all cells.
#         if all_clicked:

#             # If all the mines are properly flagged, then we won
#             if all_flags_equal_to_mines:
#                 self.game_won = True
#             else:
#                 self.game_won = False
#             return

#         # Update all equations in our knowledge base which are subsets of each other
#         # whenever we run out of non-mines and mines
#         if self._check_solvable_csp():
#             self._resolve_subsets()

#             # If everything fails, then click randomly
#             if self._check_solvable_csp():
#                 self._click_random_square_with_heuristic()


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
# self.cells.append(curr)
'''

# for curr in self.cells:
# print(curr.x, curr.y, curr.flag)


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
