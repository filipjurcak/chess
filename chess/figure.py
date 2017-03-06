from importlib import import_module
from chess.list_images import List_images


class Figure:
    def __init__(self, x, y, color, image, board):
        self.x = x
        self.y = y
        self.color = color
        self.image = image
        self.board = board

    def movement(self, destx, desty, figures, dx, dy):
        if self.check(destx, desty, self.color, dx, dy):
            return self.move(destx, desty, figures, dx, dy)

    def move(self, destx, desty, figures, dx, dy):
        instance = ''
        for figure in figures:
            if figure.x == destx and figure.y == desty and figure.color != self.color:
                instance = figure.__class__.__name__
        if self.__class__.__name__ == 'Pawn' and instance != 'King' and dy == 1 and (
                    (self.y == 1 and self.color == 'white') or (self.y == 6 and self.color == 'black')) and (
                dx == 0 and self.board[destx][desty] == 0) or (dx == 1 and self.board[destx][desty] == 1):
            var = input("Choose which figure do you want: \n")
            self.switch(var, figures, destx, desty)
        elif self.board[destx][desty] == 1:
            for i in range(len(figures)):
                if figures[i].x == destx and figures[i].y == desty and figures[i].color != self.color:
                    if figures[i].__class__.__name__ == "King":
                        if self.color == 'white':
                            return 1
                        else:
                            return 2
                    del figures[i]
                    break
        self.board[self.x][self.y] = 0
        self.board[destx][desty] = 1
        self.x = destx
        self.y = desty
        return 0

    def switch(self, var, figures, destx, desty):
        # images = Game().Images
        images = List_images().Images
        while var != "Rook" and var != "Queen" and var != "Knight" and var != "Bishop":
            var = input("Choose which figure do you want: \n")
        figures[:] = [value for value in figures if (value.x != destx or value.y != desty)]
        figures[:] = [value for value in figures if (value.x != self.x or value.y != self.y)]
        classfigure = var
        var = chr(ord(var[0]) + 32) + var[1:]
        module = import_module('chess.' + str(var))
        class_ = getattr(module, classfigure)
        figures.append(class_(destx, desty, self.color, images[self.color + str(classfigure)]['Image'], self.board))
