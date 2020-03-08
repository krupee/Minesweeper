from gameboard import Game
from random import randrange, seed
import numpy as np
from basicAgent import is_number, bombsAroundCell, safeAroundCell, revealNeighbors, flagNeighbors, numNeighbors

knowledgeBase = []
mineTiles = []
safeTiles = []

def _check_equations_for_mine_and_non_mine_variables(self):
        global mineTiles
        global knowledgeBase
        global safeTiles
        for equation in knowledgeBase.copy():

            # If the equation becomes empty i.e. all its variables are removed
            if len(equation) == 0 or len(equation[0]) == 0:
                knowledgeBase.remove(equation)
                continue

            # If value is 0, all variables in that equation are non-mine variables.
            if equation[1] == 0:
                knowledgeBase.remove(equation)
                for non_mine_variable in equation[0]:
                    if self.grid_display[non_mine_variable.x][non_mine_variable.y] is '#' and non_mine_variable not in safeTiles:
                        safeTiles.append(non_mine_variable)
                continue

            # If value is equal to the length of the equation, then all the variables
            # in the equation are min variables for sure.
            if len(equation[0]) == equation[1]:
                knowledgeBase.remove(equation)
                for mine_variable in equation[0]:
                    if not self.grid_display[mine_variable.x][mine_variable.y] is 'F' and mine_variable not in mineTiles:
                        mineTiles.append(mine_variable)

def _resolve_subsets(self):
        global knowledgeBase
        # Sort all equations in increasing order of their length
        knowledgeBase = sorted(knowledgeBase, key = lambda x: len(x[0]))

        # Start resolving subsets
        for equation in knowledgeBase:
            for equation_ in knowledgeBase:

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
        _check_equations_for_mine_and_non_mine_variables(self)       
        
        
def _remove_variable_from_other_equations(self, tile, is_mine_variable = False):
        global knowledgeBase
        for equation in knowledgeBase:
                if tile in equation[0]:
                    equation[0].remove(tile)

                    if is_mine_variable and equation[1]:
                        equation[1] -= 1        

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

    global knowledgeBase
    # Append the equation in the global equation list
    knowledgeBase.append((tile.constraint_equation, tile.constraint_value))

def updateBoard(self):
    for row in range(self.gird_size):
        for col in range(self.gird_size):
            if (self.grid_display == 0 or bombsAroundCell(self, row, col) == self.grid_display):
                self.uncoverCell(row, col)
            if (self.grid_display == numNeighbors(self, row, col) - safeAroundCell(self, row, col)):
                self.flagNeighbors(self, row, col)
                
                    
          
def improvedAgent(self):
    
    # Pick random tile
    # Get clue and clues around tile to build constarint variable and equation
    # Add to knowlege base the clue of tile and a lisr of the cluesof all neighbors
    # Based on constarint vairabe and smallest of all constraint equation pick next tile
    
    # Choosing random cell
    temp = [randrange(self.gird_size), randrange(self.gird_size)]
    currentTile = self.uncoverCell(temp[0], temp[1])
    if currentTile:
        _create_constraint_equation_for_variable(self, tile = currentTile)
        _remove_variable_from_other_equations(self, tile = currentTile)
   
    while (True):
        updateBoard(self)
        _resolve_subsets(self)
        temp = [randrange(self.gird_size), randrange(self.gird_size)]
        currentTile = self.uncoverCell(temp[0], temp[1])
        if currentTile:
            _create_constraint_equation_for_variable(self, tile = currentTile)
            _remove_variable_from_other_equations(self, tile = currentTile)
        print(safeTiles)
       
        
        
        
            
            
            
            
                  
grid_size = 4
num_mines = 1
game = Game(grid_size, num_mines)
size = game.gird_size
improvedAgent(game)
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