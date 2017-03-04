from Classes.Figure import Figure


class Bishop(Figure):
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
        if dx <= 7 and dy <= 7 and self.CheckWayBishop(self.a, self.b, destx, desty) and self.color == a and dx == dy:
            return True
        return False

    def CheckWayBishop(self, startx, starty, destx, desty):
        if startx > destx and starty > desty:
            i = startx - 1
            j = starty - 1
            while i > destx and j > desty:
                if self.board[i][j] == 1:
                    return False
                else:
                    i -= 1
                    j -= 1
        if startx > destx and desty > starty:
            i = startx - 1
            j = starty + 1
            while i > destx and j < desty:
                if self.board[i][j] == 1:
                    return False
                else:
                    i -= 1
                    j += 1
        if destx > startx and starty > desty:
            i = startx + 1
            j = starty - 1
            while i < destx and j > desty:
                if self.board[i][j] == 1:
                    return False
                else:
                    i += 1
                    j -= 1
        if destx > startx and desty > starty:
            i = startx + 1
            j = starty + 1
            while i < destx and j < desty:
                if self.board[i][j] == 1:
                    return False
                else:
                    i += 1
                    j += 1
        return True
