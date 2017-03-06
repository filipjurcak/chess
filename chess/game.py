from chess.bishop import Bishop
from chess.knight import Knight
from chess.rook import Rook
from chess.queen import Queen
from chess.pawn import Pawn
from chess.king import King
from importlib import import_module
from .list_images import images as figures_images


class Game:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.whomoves = 0
        self.figures = []
        self.Images = figures_images

    def save(self, name):
        doc = open(name, 'w+')
        doc.write(str(len(self.figures)) + '\n')
        for figure in self.figures:
            doc.write(str(figure.__class__.__name__) + ' ' + str(figure.color) + ' ' + str(figure.x) + ' ' +
                      str(figure.y) + '\n')
        doc.write(str(self.whomoves))
        doc.close()

    def load(self):
        name = input('Type name of file where you have your saved game: \n')
        name += '.txt'
        doc = open(name, 'r+')
        for _ in range(int(doc.readline())):
            figure = doc.readline()
            parameters = self.parametres(figure)
            classfigure = chr(ord(parameters[0][0]) + 32) + parameters[0][1:]
            module = import_module('chess.' + classfigure)
            class_ = getattr(module, parameters[0])
            self.figures.append(class_(parameters[2], parameters[3], parameters[1],
                                       self.Images[str(parameters[1]) + parameters[0]]['Image'], self.board))
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
                        self.figures.append(Rook(j, i, color, figures_images[color + 'Rook']['Image'], self.board))
                    if j == 1 or j == 6:
                        self.figures.append(Knight(j, i, color, figures_images[color + 'Knight']['Image'], self.board))
                    if j == 2 or j == 5:
                        self.figures.append(Bishop(j, i, color, figures_images[color + 'Bishop']['Image'], self.board))
                    if j == 3:
                        self.figures.append(King(j, i, color, figures_images[color + 'King']['Image'], self.board))
                    if j == 4:
                        self.figures.append(Queen(j, i, color, figures_images[color + 'Queen']['Image'], self.board))
                if i == 1 or i == 6:
                    self.figures.append(Pawn(j, i, color, figures_images[color + 'Pawn']['Image'], self.board))

    def move(self, startx, starty, destx, desty):
        figure = [val for val in self.figures if (val.x == startx and val.y == starty)]
        res = figure[0].movement(destx, desty, self.figures, abs(startx - destx), abs(starty - desty))
        if res == 0:
            self.whomoves += 1
        return res

    def control(self, startx, starty, destx, desty):
        figure = [val for val in self.figures if (val.x == startx and val.y == starty)]
        return figure[0].check(destx, desty, self.get_color(), abs(startx - destx), abs(starty - desty))

    def parametres(self, parameters):
        return str(parameters.split()[0]), str(parameters.split()[1]), int(parameters.split()[2]), int(
            parameters.split()[3])

    def get_color(self):
        if self.whomoves % 2 == 1:
            return 'black'
        else:
            return 'white'
