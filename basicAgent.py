from gameboard import Game


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.flag = 0  # 0 = unknown, 1 = safe, 2 = mine
        self.numAdjacentMines = 0
        self.numAdjacentSafe = 0
        self.numAdjacentHidden = 0


def basicAgent(self):
    self.show()
    # Pick first square to start
    self.uncoverCell(0, 0)
    print(self.mineindicator(0))
    self.show()
    for x in range(self.gird_size):
        for y in range(self.gird_size):
            curr = Tile(x, y)
            self.cells.append(curr)

    # for curr in self.cells:
        #print(curr.x, curr.y, curr.flag)


game = Game(8, 8)
basicAgent(game)
