white = 1
black =-1
tablesize = 8

class board():

    def __init__(self):
        self.cell = [[0 for i in range(tablesize)]for i in range(tablesize)]

        self.cell[3][3] = white
        self.cell[4][4] = white
        self.cell[3][4] = black
        self.cell[4][3] = black

#print(*board().cell, sep= "\n")

class putboard():

    def putreversi(self, x, y, player):

        if self.cell[y][x] is not 0:
            return False

        else:
            self.cell[y][x] = player
            return True
