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

knowledgeBase = []  # Knowledgebase containing constraint equations
mineTiles = []  # List of tiles that are mines
safeTiles = []  # List of tiles that are safe


def riskyAgent(self):
    # Pick random tile
    # Get clue and clues around tile to build constarint variable and equation
    # if inconclusive only then make a random move.
    self.show()

    # Choosing random cell to begin
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
    visual(self)


grid_size = 10
num_mines = 25
game = Game(grid_size, num_mines)
size = game.gird_size
game.mineindicator(size)
riskyAgent(game)
print()
