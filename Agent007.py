from gameboard import Game
from random import randrange, seed
import numpy as np
from basicAgent import is_number, bombsAroundCell, safeAroundCell, revealNeighbors, flagNeighbors, numNeighbors


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

knowledgeBase = [] # Knowledgebase containing constraint equations
mineTiles = [] # List of tiles that are mines
safeTiles = [] #List of tiles that are safe

def determineCell(self):
        # Getting globals
        global mineTiles
        global knowledgeBase
        global safeTiles
        # Iterate through knowledge base
        for e in knowledgeBase.copy():

            # If an equation is empty, it is no longer needeed
            if len(e) == 0 or len(e[0]) == 0:
                knowledgeBase.pop(e)
               # print(knowledgeBase)
                continue

            # If the val is 0, then we know all vars in that equation are safe vars
            if e[1] == 0:
                knowledgeBase.remove(e)
                for safe in e[0]:
                    if self.grid_display[safe.x][safe.y] is '#' and safe not in safeTiles:
                        # Adding tile to safe tiles list
                        safeTiles.append(safe)
                continue

            # If the length of the equation is equal to the val of the equation equal, then we know all the vars in the constraint equation are mine tiles 
            if len(e[0]) == e[1]:
                knowledgeBase.remove(e)
                for mine in e[0]:
                    if not self.grid_display[mine.x][mine.y] is 'F' and mine not in mineTiles:
                        # Adding tile to mine tiles list
                        mineTiles.append(mine)

# Reduces number of equations 
def reduceEquations(self): 
        global knowledgeBase
        # Sort all equations in increasing order of their length
        knowledgeBase = sorted(knowledgeBase, key = lambda x: len(x[0]))

        # Iterate through each equation
        for e in knowledgeBase:
            # Iterate through each equation to compare
            for e_ in knowledgeBase:
                # Checking if equation is not the same
                if e == e_ or not e[0] or not e_[0] or not e[1] or not e_[1]:
                    continue

                # Checking if subset found
                if set(e[0]).issubset(set(e_[0])):
                    # Removing subset equation
                    e_[0] = list(set(e_[0]) - set(e[0]))
                    e_[1] -= e[1]
                    continue

                # Checking for superset
                if set(e_[0]).issubset(set(e[0])):
                    e[0] = list(set(e[0]) - set(e_[0]))
                    # Removing subset equation
                    #print(e[1])
                    e[1] -= e_[1]
                    

        # After removing subsets we must infer new safe tiles and mine tiles
        determineCell(self)       

# Function that removes a tile from the knowledgebase     
def removeTile(self, tile):
        global knowledgeBase
        # for eveery equation in knowledgebase
        for e in knowledgeBase:
                # Checking if tile is within current constraint equation
                if tile in e[0]:
                    # Removing variable corresponding to tile from the equation
                    e[0].remove(tile)

                    # If the tile is a mine, then substract from equation val
                    if tile.isMine and e[1]:
                        e[1] -= 1        

# Function that creates an equation given a tile
def createEquation(self,tile):
    row = tile.x
    column = tile.y

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            # Current cell, ignore
            if (i == 0 and j == 0):
                continue

            # Getting neighbors of cell
            if (row + i >= 0 and column + j >= 0 and row + i < self.gird_size and column + j < self.gird_size):

                # If the neighbor is already visited do not add to the constraint equation.
                if self.grid_display[row + i][column + j] != '#':
                    continue

                # If a neighbour is flagged then do not add it to the equation but subtract the constraint value of the current variable.
                if str(self.grid_display[row + i][column + j]) is 'F':
                    # Subtracting the tiles constraint value as neighboring mine is already flagged!
                    tile.constraint_value -= 1
                    continue
                
                # Getting neighboring tiles that are not visited or flagged
                neighbour = self.tile_grid[row + i][column + j]

                # Adding neghboring unvisiteed tiles to constraint equation
                tile.add_constraint_variable(tile = neighbour)

    # Referencing knowledgebase
    global knowledgeBase
    # Append the equation in the global equation list
    #print("here")
    knowledgeBase.append((tile.constraint_equation, tile.constraint_value))

# Function that updates the board based on simple cases
def updateBoard(self):
    for row in range(self.gird_size):
        for col in range(self.gird_size):
            if (self.grid_display == 0 or bombsAroundCell(self, row, col) == self.grid_display):
                self._uncoverCell(row, col) # Uncovering cell
            if (self.grid_display == numNeighbors(self, row, col) - safeAroundCell(self, row, col)):
                self.flagNeighbors(self, row, col) # Uncovering cell

# Checking if safe tiles and mine tile lists are empty or not               
def check():
    global mineTiles
    global safeTiles

    # Both lists are empty
    if (not mineTiles) and (not safeTiles):
        return False
    else:
    
        return True    # One or both of the lists have tiles              

# Function displays the constraint value equation nicely
def displayEquation():
    global knowledgeBase
    if (not knowledgeBase):
        print("global knowedege base is currently empty")
    
    for equation in knowledgeBase: # Iterating through every equation
        # Printing equation
        print(repr([(variable.x, variable.y) for variable in equation[0]]), " = ", equation[1])  

def countFlags(self):
    count = 0
    for i in range (self.gird_size):
        for j in range (self.gird_size):
            if (self.grid_display[i][j] is 'F'):
                count = count+1

    return count

# Reveals cells that we know are safe based on constraint values
def revealSafeCells(self):
    while(safeTiles):
            tile = self.safeTiles.pop(0)
            row = tile.x
            col = tile.y
            self._uncoverCell(row,col)

# Gets tiles of game and creates new equations at every state
def gameState (self):
    i = 0
    j = 0
    for i in range(self.gird_size):
        for j in range(self.gird_size):
            tile = self._uncoverCell(i,j)
            if (tile):
                createEquation(self, tile = tile)
                removeTile(self, tile = tile)

# Function that mimics improved agent
def improvedAgent(self):
    # Pick random tile
    # Get clue and clues around tile to build constarint variable and equation
    # Add to knowlege base the clue of tile and a lisr of the cluesof all neighbors
    # Based on constarint vairabe and smallest of all constraint equation pick next tile
    self.show()

    # Choosing random cell to begin
    temp = [randrange(self.gird_size), randrange(self.gird_size)]
    currentTile = self._uncoverCell(temp[0], temp[1])

    if currentTile:
        createEquation(self, tile = currentTile)
        removeTile(self, tile = currentTile)
    reduceEquations(self) # Reducing equations
    self.show()
    
    
    displayEquation()
    while (self.mine_count != countFlags(self)):
        if (gameState(self)):
            break
        updateBoard(self)
        
        
        if (check):
            temp = [randrange(self.gird_size), randrange(self.gird_size)]
            currentTile = self._uncoverCell(temp[0], temp[1])
            if currentTile:
                createEquation(self, tile = currentTile)
                removeTile(self, tile = currentTile)
        else:
            reduceEquations(self)
            if (check):
                temp = [randrange(self.gird_size), randrange(self.gird_size)]
                currentTile = self.uncoverCell(temp[0], temp[1])
                createEquation(self, tile = currentTile)
                removeTile(self, tile = currentTile)
    displayEquation()
    self.show()   
   
        
        
        
            
            
            
            
                  
grid_size = 8
num_mines = 3
game = Game(grid_size, num_mines)
size = game.gird_size
improvedAgent(game)
print()

