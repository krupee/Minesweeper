'''
from tkinter import *
from gameboard import Game

def displayGame(self):

    my_window = Tk()

    for x in range(self.gird_size):
        for y in range(self.gird_size):
            if (x == 3):
                label = Label(my_window, width = "5", height = "5", bg = "red")
                label.grid(row = x, column = y)


    my_window.mainloop()

game = Game(4, 1)
size = game.gird_size
game.mineindicator(size)
displayGame(game)
'''

# This code was inspired by online resources


from tkinter import *  # assume Python 3
from gameboard import Game


class Level:
    def __init__(self, name, height, width):
        self.name = name
        self.height = height
        self.width = width
        self.tiles = makeTiles(height, width)

    class Tile:
        def __init__(self, x, y, image):
            self.x = x
            self.y = y
            self.image = None


def makeTiles(height, width):
    tiles = [[Level.Tile(x, y, None) for x in range(width)] for y in range(height)]
    return tiles


root = Tk()

zero = PhotoImage(file='images/0.PNG')
one = PhotoImage(file='images/1.PNG')
two = PhotoImage(file='images/2.PNG')
three = PhotoImage(file='images/3.PNG')
four = PhotoImage(file='images/4.PNG')
five = PhotoImage(file='images/5.PNG')
six = PhotoImage(file='images/6.PNG')
seven = PhotoImage(file='images/7.PNG')
eight = PhotoImage(file='images/8.PNG')
bomb = PhotoImage(file='images/bomb.PNG')
click = PhotoImage(file='images/click.PNG')
flag = PhotoImage(file='images/flag.PNG')


game = Game(10, 1)
size = game.gird_size
game.mineindicator(size)

test1 = Level("mine", 10, 10)
for x in range(10):
    for y in range(10):
        curr = game.grid_display[x][y]
        if curr == "#":
            test1.tiles[x][y].image = zero
        elif curr == "*":
            test1.tiles[x][y].image = zero
        else:
            test1.tiles[x][y].image = zero

colorMatrix = [[0 for x in range(10)] for y in range(10)]
for x in range(10):
    for y in range(10):
        colorMatrix[x][y] = test1.tiles[x][y].image

#print(colorMatrix)

width, height = 400, 400


root.title("colorMatrix")

frame = Frame()
#frame.pack()

canvas = Canvas(frame, width=width, height=height)
rows, cols = len(colorMatrix), len(colorMatrix[0])



'''
rect_width, rect_height = width // rows, height // cols
for y, row in enumerate(colorMatrix):
    for x, color in enumerate(row):
        x0, y0 = x * rect_width, y * rect_height
        x1, y1 = x0 + rect_width-1, y0 + rect_height-1
        #button.grid(row = )
'''
for x in range(10):
    for y in range(10):
        button = Button(root, image = colorMatrix[x][y])
        button.grid(row = x, column = y)
#canvas.pack()

root.mainloop()