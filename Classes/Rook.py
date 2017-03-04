from Classes.Figure import Figure


class Rook(Figure):
    def __init__(self, a, b, color, image, board):
        self.a = a
        self.b = b
        self.color = color
        self.image = image
        self.board = board

    def check(self, destx, desty, whomoves):
        dx = abs(self.a - destx)
        dy = abs(self.b - desty)
        if whomoves % 2 == 1:
            a = 'black'
        else:
            a = 'white'
        if dx <= 7 and dy <= 7 and self.CheckWayRook(self.a, self.b, destx, desty) and self.color == a:
            if (dx <= 7 and dy == 0) or (dy <= 7 and dx == 0):
                return True
        return False

    def CheckWayRook(self, startx, starty, destx, desty):
        if destx - startx == 0:
            if desty - starty > 0:
                i = starty + 1
                while i < desty:
                    if self.board[destx][i] == 1:
                        return False
                    else:
                        i += 1
            else:
                i = starty - 1
                while i > desty:
                    if self.board[destx][i] == 1:
                        return False
                    else:
                        i -= 1
        if desty - starty == 0:
            if destx - startx > 0:
                i = startx + 1
                while i < destx:
                    if self.board[i][desty] == 1:
                        return False
                    else:
                        i += 1
            else:
                i = startx - 1
                while i > destx:
                    if self.board[i][desty] == 1:
                        return False
                    else:
                        i -= 1
        return True
