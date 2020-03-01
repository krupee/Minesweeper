from random import randrange, seed

Empty = 0
Bomb = 1
Hide = '#'


class Game:
    def __init__(self, gird_size, mine_count):

        self.gird_size = gird_size
        self.mine_count = mine_count

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
            self.grid_display[row][col] = 'M'

    def show(self):
        for i in range(self.gird_size):
            for j in range(self.gird_size):
                if j == 0:
                    print(i, end=' ')
                print(self.grid_display[i][j], end=' ')
            print()
        print('  ', end='')
        for i in range(self.gird_size):
            print(i, end=' ')
        print()
