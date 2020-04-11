from gameboard import Game
from random import randrange, seed
import numpy as np
from basicAgent import is_number, bombsAroundCell, safeAroundCell, revealNeighbors, flagNeighbors, numNeighbors
from visual import *
from Agent007 import countFlags, displayEquation, check, updateBoard, createEquation, removeTile, reduceEquations, determineCell, revealNeighbors, revealSafeCells, gameState
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

knowledgeBase = []  # Knowledgebase containing constraint equations
mineTiles = []  # List of tiles that are mines
safeTiles = []  # List of tiles that are safe


def play():
    grid_size = 5
    num_mines = 5
    game = Game(grid_size, num_mines)
    size = game.gird_size
    game.mineindicator(size)
    riskyAgent(game)


def probability(self):
    min = 1
    minProbx = 0
    minProby = 0
    for x in range(self.tile_grid):
        for y in range(self.tile_grid):
            if (self.grid_display[x][y] < min):
                minProbx = x
                minProby = y
    return [minProbx, minProby]


def riskyAgent(self):
    # Pick random tile
    # Get clue and clues around tile to build constarint variable and equation
    # if inconclusive only then make a random move else look for the best viable option, make risky steps.
    # we also don't have a clue about the number of mines.

    self.show()

    # Choosing random cell to begin
    # first move...
    temp = [randrange(self.gird_size), randrange(self.gird_size)]
    currentTile = self._uncoverCell(temp[0], temp[1])

    temp = [randrange(self.gird_size), randrange(self.gird_size)]
    currentTile = self._uncoverCell(temp[0], temp[1])

    if currentTile:
        createEquation(self, tile=currentTile)
        removeTile(self, tile=currentTile)
    reduceEquations(self)  # Reducing equations
    self.show()

    displayEquation()
    while (self.mine_count != countFlags(self)):
        if (gameState(self)):
            break
        updateBoard(self)

        temp = [randrange(self.gird_size), randrange(self.gird_size)]
        currentTile = self._uncoverCell(temp[0], temp[1])
        if currentTile:
            createEquation(self, tile=currentTile)
            removeTile(self, tile=currentTile)

        reduceEquations(self)

    displayEquation()
    self.show()
    # # visual(self)

    # if currentTile:
    #     createEquation(self, tile=currentTile)
    #     removeTile(self, tile=currentTile)
    # reduceEquations(self)  # Reducing equations

    # displayEquation()
    # while (self.mine_count != countFlags(self)):
    #     if (gameState(self)):
    #         break
    #     updateBoard(self)
    # displayEquation()
    # self.show()


# grid_size = 10
# num_mines = 25
# game = Game(grid_size, num_mines)
# size = game.gird_size
# game.mineindicator(size)
# riskyAgent(game)
# print()
play()
