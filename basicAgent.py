from gameboard import Game
from random import randrange, seed
class Tile:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.flag = 0 # 0 = unknown, 1 = safe, 2 = mine
        self.numNeighbors = 0
        self.numAdjacentMines = 0
        self.numAdjacentSafe = 0
        self.numAdjacentHidden = 0

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
    
    tile.ad

 


## Uncovers all neighbors of a given cell
def revealNeighbors(self,row,col):
  for r in range(-1, 2):
		for c in range(-1, 2):
      if (r == 0 and c == 0): #Current cell
				continue
      if (row + r >= 0 and col + c >= 0 and row + r < self.gird_size and col + j < self.gird_size and (self.grid_display[row+r][col+c] == '#' and not self.grid_display[row+r][col+c] == 'F' )):
      	self.uncoverCell(row+r,col+c) 

        
        
## Flags all neighbors of a given cell
def flagNeighbors(self,row,col):
  for r in range(-1, 2):
  	for c in range(-1, 2):
      if (r == 0 and c == 0): #Current cell
        continue
      if (row + r >= 0 and col + c >= 0 and row + r < self.gird_size and col + j < self.gird_size and (self.grid_display[row+r][col+c] == '#' and not self.grid_display[row+r][col+c] == 'F' )):
				self.grid_display[row+r][col+c] = 'F'        
 
## Counts number of flagged mines around current cell 
def bombsAroundCell(self, row, col):
  count = 0
  for r in range(-1, 2):
  	for c in range(-1, 2):
      if (r == 0 and c == 0): #Current cell
        continue
      if (row + r >= 0 and col + c >= 0 and row + r < self.gird_size and col + j < self.gird_size and self.grid_display[row+r][col+c] == 'F' )):
				count = count + 1  
  return count

def safeAroundCell(self, row, col):
  count = 0
  for r in range(-1, 2):
  	for c in range(-1, 2):
      if (r == 0 and c == 0): #Current cell
        continue
      if (row + r >= 0 and col + c >= 0 and row + r < self.gird_size and col + j < self.gird_size and self.grid_display[row+r][col+c] == '#' )):
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



def basicAgent(self):
  	lose = False
    temp = (randrange(gird_size), randrange(gird_size))
    self.uncoverCell(temp[0], temp[1])
  	while ((lose == False) or (self.mine_count == flagCount)):
			flagCount = 0
      for x in range(self.gird_size):
        for y in range(self.gird_size):
          if (self.grid_display[x][y] != "#"): #Current cell is already revealed
            # Case 1
            continue
          elif (self.grid_display[x][y] == "F"): #Curret cell is already flagged
            # Case 2
            flagCount = flagCount + 1
            continue
          elif (self.grid_display[x][y] == "M"): #Just reevealed current cell and its a mine :(
            #print("Hit a Mine! You Lose!")
            lose = True
          else:
            clue = self.grid[x][y]
            if (clue == 0):
              # All safe around cell
              self.revealNeighbors(x, y)
            elif (clue == 8):
              # All mines around me
              self.flagNeighbors(x, y)
            else:
              # Corner/edge cases
              if (clue == self.bombsAroundMe(x, y)):
                self.revealNeighbors(x, y)
              elif (clue == self.safeAroundMe(x, y)):
                self.flagNeighbors(x, y)
      
      if (lose == True):
        print("Mine hit")
      else:
        print("You won!")
          
          
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

            



    
    #for curr in self.cells:
        #print(curr.x, curr.y, curr.flag)






game = Game(8, 8)
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


https://github.com/vedantc6/CS520-AI/blob/master/MineSweeper/agents/base_agent.py
 
'''




