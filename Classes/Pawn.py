from Classes.Figure import Figure


class Pawn(Figure):
    def __init__(self, a, b, color, image, board):
        self.a = a
        self.b = b
        self.color = color
        self.image = image
        self.board = board

    def check(self, destx, desty, whomoves):
        if whomoves % 2 == 1:
            a = 'black'
        else:
            a = 'white'
        dx = abs(destx - self.a)
        dy = self.b - desty
        if self.color == 'white' == a and 0 < dy <= 2 and 0 <= dx <= 1:
            if self.b == 6 and dy == 2 and dx == 0 and self.board[destx][desty + 1] == 0 and self.board[destx][desty] == 0:
                return True
            if dy == 1 and dx == 0 and self.board[destx][desty] == 0:
                return True
            if dy == 1 and dx == 1 and self.board[destx][desty] == 1:
                return True
            return False
        if self.color == 'black' == a and 0 < -dy <= 2 and 0 <= dx <= 1:
            if self.b == 1 and -dy == 2 and dx == 0 and self.board[destx][desty - 1] == 0 and self.board[destx][desty] == 0:
                return True
            if -dy == 1 and dx == 0 and self.board[destx][desty] == 0:
                return True
            if -dy == 1 and dx == 1 and self.board[destx][desty] == 1:
                return True
            return False
