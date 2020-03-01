from gameboard import Game

numberMines = 0

def run():
    gameboard = initialize()
    size = gameboard.gird_size
    #Setting up number of mines adjacent to cells
    gameboard.mineindicator(size,size)
    i=0
    while (not(gameboard.gameState(size,numberMines) )):
        print()
        print()
        print ('Current Board')
        gameboard.show()
        gameboard.gameOptions()
        gameboard.show()


def initialize():
    gird_size = 0
    mine_count = 0
    while(True):
        try:
            gird_size = int(input('size: '))
            break
        except:
            print('wrong input type')
    while(True):
        try:
            mine_count = int(input('mines: '))
            if mine_count <= gird_size * gird_size:
                numberMines = mine_count
                break
            print(
                f'mines should be less than number of cells ({gird_size*gird_size})')
        except:
            print('wrong input type')
    return Game(gird_size, mine_count)


if __name__ == '__main__':
    run()
