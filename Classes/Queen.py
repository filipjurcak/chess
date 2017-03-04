from Classes.Bishop import Bishop
from Classes.Rook import Rook


class Queen(Rook, Bishop):
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
        if dx <= 7 and dy <= 7 and self.CheckWayBishop(self.a, self.b, destx, desty) and \
                self.CheckWayRook(self.a, self.b, destx, desty) and self.color == a and \
                ((dx <= 7 and dy == 0) or (dy <= 7 and dx == 0) or (dx == dy)):
            return True
        return False
