import numpy as np

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

print(*board().cell, sep= "\n")

class putboard():

    def putreversi(self, x, y, player):

        if self.cell[y][x] is not 0:
            return False

        else:
            self.cell[y][x] = player
            return True

    def flipp (self , x, y, player):
        precell = [(yy,xx) for y in tablesize for x in tablesize]
        if yy == 0 and xx == 0:
            continue

        #print(xx,yy)

        availlable = []
        distance = 0

       while(True):
           distance += 1
           disy = y +(yy * distance)
           disx = x +(xx * distance)

           if 0 <= disy <= tablesize  and  0<= disx <= tablesize:
               correct = self.cell[disy][disx]
            if correct == 0:
                break

            if correct == player:
                if availlable != []:
                    

            #    fllip.append(availlable)
