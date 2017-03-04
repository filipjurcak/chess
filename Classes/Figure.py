from importlib import import_module
from Dictionaries.List_images import List_images


class Figure:
    def checkni(self, destx, desty, whomoves):
        return self.check(destx, desty, whomoves)

    def movement(self, destx, desty, figures, whomoves):
        if self.check(destx, desty, whomoves):
            return self.move(destx, desty, figures)

    def move(self, destx, desty, figures):
        dx = abs(destx - self.a)
        dy = abs(desty - self.b)
        if self.__class__.__name__ == 'Pawn' and ((self.b == 1 and self.color == 'white') or (self.b == 6 and self.color == 'black')):
            if (dy == 1 and dx == 0 and self.board[destx][desty] == 0) or (dy == 1 and dx == 1 and self.board[destx][desty] == 1):
                var = input("Choose which figure do you want: \n")
                self.switch(var, figures, destx, desty)
                self.board[self.a][self.b] = 0
                self.board[destx][desty] = 1
                return 0
        if self.board[destx][desty] == 1:
            for j in range(len(figures)):
                if figures[j].a == destx and figures[j].b == desty:
                    if figures[j].color == self.color:
                        return
                    if figures[j].__class__.__name__ == "King":
                        if self.color == 'white':
                            return 1
                        if self.color == 'black':
                            return 2
                    del figures[j]
                    break
        self.board[self.a][self.b] = 0
        self.board[destx][desty] = 1
        self.a = destx
        self.b = desty
        return 0

    def switch(self, input, figures, destx, desty):
        self.Images = List_images().Images
        while input != "Rook" and input != "Queen" and input != "Knight" and input != "Bishop":
            input = input("Choose which figure do you want: \n")
        color = self.color
        board = self.board
        for i in range(len(figures)):
            if figures[i].a == destx and figures[i].b == desty:
                del figures[i]
                break
        for i in range(len(figures)):
            if figures[i].a == self.a and figures[i].b == self.b:
                del figures[i]
                break
        module = import_module('Classes.' + str(input))
        class_ = getattr(module, input)
        figures.append(class_(destx, desty, color, self.Images[color + str(input)]['Image'], board))
