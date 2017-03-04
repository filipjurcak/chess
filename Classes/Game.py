from Dictionaries.List_images import List_images
from Classes.Bishop import Bishop
from Classes.Knight import Knight
from Classes.Rook import Rook
from Classes.Queen import Queen
from Classes.Pawn import Pawn
from Classes.King import King
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
                      str(self.figures[i].a) + " " + str(self.figures[i].b) + '\n')
        doc.write(str(self.whomoves))
        doc.close()

    def load(self):
        name = raw_input('Type name of file where you have your saved game: \n')
        name += '.txt'
        doc = open(name, 'rw+')
        for i in range(int(doc.readline())):
            figure = doc.readline()
            parameters = self.parametres(figure)
            module = import_module('Classes.' + str(parameters[0]))
            class_ = getattr(module, parameters[0])
            self.figures.append(class_(parameters[2], parameters[3], parameters[1],
                              self.Images[str(parameters[1]) + str(parameters[0])]['Image'], self.board))
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
        for i in range(len(self.figures)):
            if self.figures[i].a == startx and self.figures[i].b == starty:
                a = self.figures[i].movement(destx, desty, self.figures, self.whomoves)
                if a == 0:
                    self.whomoves += 1
                return a

    def checkuj(self, startx, starty, destx, desty):
        for i in range(len(self.figures)):
            if self.figures[i].a == startx and self.figures[i].b == starty:
                return self.figures[i].checkni(destx, desty, self.whomoves)

    def parametres(self, parameters):
        return str(parameters.split()[0]), str(parameters.split()[1]), int(parameters.split()[2]), int(parameters.split()[3])
