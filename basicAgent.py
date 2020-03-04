from gameboard import Game

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
def numNeighbors(self, tile):
    x = tile.x
    y = tile.y
    count = 0
    print(x, y)
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


        break
        


        



        
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