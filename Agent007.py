from gameboard import Game
from random import randrange, seed
import numpy as np
from basicAgent import is_number, bombsAroundCell, safeAroundCell, revealNeighbors, flagNeighbors


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
    x = a
    y = b

    while ((mine_hit is False) and (self.mine_count != flagCount)):
        print("flagcount", flagCount)
        self.show()
        print()
        for x in range(grid_size):
            for y in range(grid_size):
                # Current cell is already revealed
                if(x == 0 and y == 0):
                    continue

                if (is_number(self.grid_display[x][y])):
                    # Case 1
                    # print("here")
                    continue
                # Curret cell is already flagged
                elif (str(self.grid_display[x][y]) is 'F'):
                    # Case 2
                    flagCount = flagCount + 1
                    #print("f inc", flagCount)
                    continue
                # Just reevealed current cell and its a mine :(
                elif (str(self.grid_display[x][y]) is '*'):
                    #print("Hit a Mine! You Lose!")
                    mine_hit = True
                    # print("here")
                    break
                else:

                    _uncover_neighbors(self, a, b)
                    # mine_hit = True


def _uncover_neighbors(self, row, col):
    for r in range(-1, 2):
        for c in range(-1, 2):
            if(r == 0 and c == 0):  # current cell
                continue
            if (row + r >= 0 and col + c >= 0 and row + r < self.gird_size and
                    col + c < self.gird_size and (self.grid_display[row+r][col+c] == '#' and not self.grid_display[row+r][col+c] == 'F')):
                self.uncoverCell(row+r, col+c)
                self.show()
                _uncover_neighbors(self, row+r, col+c)


def _create_constraint_equation(self, var):
    row = var.row
    print(row)
    column = var.column
    print(column)

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (i == 0 and j == 0):
                continue

            if (row + i >= 0 and column + j >= 0 and row + i < self.gird_size and column + j < self.grid_size):

                # If the neighbor is already visited do not add to the constraint equation.
                if self.grid_display[row + i, column + j]:
                    continue

                # If a neighbour is flagged, then do not add it to the equation but subtract the constraint value of the current variable.
                if str(self.grid_display[row + i, column + j]) is 'F':
                    var.constraint_value -= 1
                    continue

                neighbour = self.grid.variable_mine_ground_copy[row + i, column + j]
                var.add_constraint_variable(variable=neighbour)

    # Append the equation in the global equation list
    self.all_constraint_equations.append(
        [var.constraint_equation, var.constraint_value])


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


grid_size = 4
num_mines = 1
game = Game(grid_size, num_mines)
size = game.gird_size
Agent007(game, grid_size, num_mines)
print()

'''
Every square is a variable with two possible values: safe or mined.
Every safe square yields a ‘sum constraint’ over its 8 neighbors. For example, a square labeled 3 yields a constraint stating the square be surrounded by 3 mines.

'''


'''
Ok so, Start with a random cell from the grid
Check Neighbors Nearby if there is a mine
Create constraint equation 

00 01 02 03 04
10 11 12 13 14
20 21 22 23 24
30 31 32 33 34

Random Cell = 01
Check if 00, 02, 10, 11, 12 is a mine?
add cells to knowledge base and mark them as safe
Open all the safe cells
If any of the cell is a mine, Flag that cell
add constraints to each of those cell, if the neigbors are all safe open all of the cells
proceed further by check neighbors of the variables with constraints 
'''
