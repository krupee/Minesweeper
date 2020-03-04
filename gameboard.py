from random import randrange, seed




Empty = 0
Bomb = -1
Hide = '#'

# Formatting for reference: .grid holds Empty:0 , Mine:-1 and .grid_display holds Empty:number, Mine:M , Flag: F
# .grid_display[][] is what the gameplayer sees
# .grid[][] is "hidden board"
class Game:
    def __init__(self, gird_size, mine_count):

        self.gird_size = gird_size
        self.mine_count = mine_count
        self.visited = self.createVisited()
        rows = [0]*mine_count
        cols = [0]*mine_count

        # initialize grid with 0
        self.grid = [[Empty]*gird_size for i in range(gird_size)]

        self.grid_display = [
            [Hide]*gird_size for i in range(gird_size)]  # diplay grid

        mine_cordinates = set()

        temp = (0, 0)

        count_flag = 0

        while count_flag < mine_count:
            temp = (randrange(gird_size), randrange(gird_size))

            if temp not in mine_cordinates:
                mine_cordinates.add(temp)
                # print(mine_cordinates)
                count_flag += 1

        for row, col in mine_cordinates:
            self.grid[row][col] = Bomb
            # Removing for gameplay purpose
            #self.grid_display[row][col] = 'M'

    def createVisited(self):
        arr = []        
        for x in range(self.gird_size):
            new = []
            for y in range(self.gird_size):
                new.append(False)
            arr.append(new)
        return arr

    def show(self):
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.grid_display]))

    def showGrid(self):
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.grid]))

    def showVisited(self):
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.visited]))
    
#   Reveals a cell and checks whether it is a mine or not
    def uncoverCell(self,row,col):
        if (self.grid_display[row][col] == 'F'): #Unflagging cell
            self.grid_display[row][col] = '#'
    
        elif (self.grid[row][col] != -1):        #Location picked  is not a mine
            
            self.grid_display[row][col] = self.grid[row][col]
        
        elif (self.grid[row][col] == -1):        #Location picked is a mine
            ## Mine exploded
            self.grid_display[row][col] = '*'
            ## NEED TO FIGURE OUT WHAT TO DO IN THIS CASE
            return

#   Calculates number of adjacent mines for every cell in minefield
    def mineindicator (self,size):
        row = size
        col = size
        for r in range (0,row):
            for c in range (0,col):
                minecount = 0           #SET/RESET MINECOUNT BACK TO 0
                if c > 0:
                    if (self.grid[r][c-1] == -1):       #Check Left
                        minecount = minecount + 1
                    if r > 0:
                        if (self.grid[r-1][c-1] == -1): #Check Top left
                            minecount = minecount + 1
                if r > 0:                           
                    if (self.grid[r-1][c] == -1):        #Check Up
                        minecount = minecount + 1
                    if c < col-1:                                   #(col-1 b/c it does 0-4 if col is 5.
                        if (self.grid[r-1][c+1] == -1): #Check Top Right
                            minecount = minecount + 1
                if c < col-1:
                    if (self.grid[r][c+1] == -1):        #Check Right
                        minecount = minecount + 1
                    if r < row-1:
                        if (self.grid[r+1][c+1] == -1):  #Check Bottom Right
                            minecount = minecount + 1
                if r < row-1:
                    if (self.grid[r+1][c] == -1):        #Check Down
                        minecount = minecount + 1
                    if c > 0:
                        if (self.grid[r+1][c-1] == -1):  #Check Bottom Left
                            minecount = minecount + 1
                if self.grid[r][c] != -1:        #If it isnt a bomb,determine mines around
                    self.grid[r][c] = minecount
        return

#   Chooses whether you want to reveal or flag a cell
    def gameOptions(self):
        decision = input('Would you like to flag or reveal a cell? (F-Flag,R-Reveal): ')
        if (decision == 'F'):
            location = input('Enter row and column (ex. 2,3): ')
            row,col = location.split(",")
            self.grid_display[int(row)][int(col)] = 'F'
        elif (decision =='R'):
            location = input('Enter row and column (ex. 2,3): ')
            row,col = location.split(",")
            row=int(row)
            col=int(col)
            self.uncoverCell(int(row),int(col))   
        return
    
    def gameState(self,size,mine_count):
        gameEnd = False
        num_Uncovered = 0
        for i in range (size):
          for u in range(size):
            if self.grid_display[i][u] != '#' and self.grid_display[i][u] != 'F' and self.grid_display[i][u] !='*':
                num_Uncovered = num_Uncovered + 1
            if self.grid_display[i][u] == '*':  #If bomb is revealed
                print ('GAME OVER')
                gameEnd = True
                return gameEnd
    
        #If the number of empty spots without mines is equal to the number of spots uncovered then game is won
        if ((size * size) - (mine_count)) == num_Uncovered:
            gameEnd = True
            print ('CONGRATS GAME WON!')
        

        return gameEnd
    
    