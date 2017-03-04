from chess.list_images import List_images
from chess.bishop import Bishop
from chess.knight import Knight
from chess.rook import Rook
from chess.queen import Queen
from chess.pawn import Pawn
from chess.king import King
from importlib import import_module


class Game:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.whomoves = 0
        self.figures = []
        self.Images = List_images().Images

    def save(self, name):
        doc = open(name, 'w+')
        doc.write(str(len(self.figures)) + '\n')
        for i in range(len(self.figures)):
            doc.write(str(self.figures[i].__class__.__name__) + " " + str(self.figures[i].color) + " " +
                      str(self.figures[i].x) + " " + str(self.figures[i].y) + '\n')
        doc.write(str(self.whomoves))
        doc.close()

    def load(self):
        name = input('Type name of file where you have your saved game: \n')
        name += '.txt'
        doc = open(name, 'r+')
        for i in range(int(doc.readline())):
            figure = doc.readline()
            parameters = self.parametres(figure)
            d = chr(ord(parameters[0][0]) - 32) + parameters[0][1:]
            module = import_module('chess.' + parameters[0])
            class_ = getattr(module, d)
            self.figures.append(class_(parameters[2], parameters[3], parameters[1],
                                       self.Images[str(parameters[1]) + d]['Image'], self.board))
        self.whomoves = int(doc.readline())

    def create(self):
        for i in range(8):
            for j in range(8):
                if i == 0 or i == 1:
                    color = 'black'
                if i == 6 or i == 7:
                    color = 'white'
                if i == 0 or i == 7:
                    if j == 0 or j == 7:
                        self.figures.append(Rook(j, i, color, self.Images[color + 'Rook']['Image'], self.board))
                    if j == 1 or j == 6:
                        self.figures.append(Knight(j, i, color, self.Images[color + 'Knight']['Image'], self.board))
                    if j == 2 or j == 5:
                        self.figures.append(Bishop(j, i, color, self.Images[color + 'Bishop']['Image'], self.board))
                    if j == 3:
                        self.figures.append(King(j, i, color, self.Images[color + 'King']['Image'], self.board))
                    if j == 4:
                        self.figures.append(Queen(j, i, color, self.Images[color + 'Queen']['Image'], self.board))
                if i == 1 or i == 6:
                    self.figures.append(Pawn(j, i, color, self.Images[color + 'Pawn']['Image'], self.board))

    def move(self, startx, starty, destx, desty):
        color = self.get_color()
        for i in range(len(self.figures)):
            if self.figures[i].x == startx and self.figures[i].y == starty:
                res = self.figures[i].movement(destx, desty, self.figures, color, abs(startx-destx), abs(starty - desty))
                if res == 0:
                    self.whomoves += 1
                return res

    def control(self, startx, starty, destx, desty):
        color = self.get_color()
        for i in range(len(self.figures)):
            if self.figures[i].x == startx and self.figures[i].y == starty:
                return self.figures[i].test(destx, desty, color, abs(startx - destx), abs(starty - desty))

    def parametres(self, parameters):
        return str(parameters.split()[0]), str(parameters.split()[1]), int(parameters.split()[2]), int(
            parameters.split()[3])

    def get_color(self):
        if self.whomoves % 2 == 1:
            return 'black'
        else:
            return 'white'
