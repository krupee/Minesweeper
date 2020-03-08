from gameboard import Game
from random import randrange, seed
import numpy as np
from basicAgent import is_number, bombsAroundCell, safeAroundCell, revealNeighbors, flagNeighbors

knowledgeBase = []
mineTiles = []
safeTiles = []


def _create_constraint_equation_for_variable(self,tile):
    row = tile.x
    print(row)
    column = tile.y
    print(column)

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (i == 0 and j == 0):
                continue

            if (row + i >= 0 and column + j >= 0 and row + i < self.gird_size and column + j < self.grid_size):

                # If the neighbor is already visited do not add to the constraint equation.
                if self.grid_display[row + i, column + j] != '#':
                    continue

                # If a neighbour is flagged, then do not add it to the equation but subtract the constraint value of the current variable.
                if str(self.grid_display[row + i, column + j]) is 'F':
                    tile.constraint_value -= 1
                    continue

                neighbour = self.tile_grid[row + i, column + j]
                tile.add_constraint_variable(tile = neighbour)

    # Append the equation in the global equation list
    knowledgeBase.append((tile.constraint_equation, tile.constraint_value))
       
grid_size = 4
num_mines = 1
game = Game(grid_size, num_mines)
size = game.gird_size
#Agent007(game, grid_size, num_mines)
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
# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

# global knowledegeBase = list()
# global mineTiles = list()
# global safeTiles = list()



# class Tile:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.flag = 0  # 0 = unknown, 1 = safe, 2 = mine
#         self.constraint_value = 0
#         self.constraint_equation = list()
#         self.isMine = False
#         self.numNeighbors = 0
#         self.numAdjacentMines = 0
#         self.numAdjacentSafe = 0
#         self.numAdjacentHidden = 0
        
          
            
# def improvedAgent(self):
    
#     # Pick random tile
#     # Get clue and clues around tile to build constarint variable and equation
#     # Add to knowlege base the clue of tile and a lisr of the cluesof all neighbors
#     # Based on constarint vairabe and smallest of all constraint equation pick next tile
    
#     # Choosing random cell
#     temp = [randrange(self.gird_size), randrange(self.gird_size)]
#     self._uncoverCell(temp[0], temp[1])
    
    
        
       
        
        

        
        
        
        
        
# game = Game(4, 1)
# size = game.gird_size
# game.mineindicator(size)
# improvedAgent(game)