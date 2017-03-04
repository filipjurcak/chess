from Classes.Bishop import Bishop
from Classes.Rook import Rook


class Queen(Rook, Bishop):
    def __init__(self, x, y, color, image, board):
        super().__init__(x, y, color, image, board)

    def check(self, destx, desty, color, dx, dy):
        if dx <= 7 and dy <= 7 and self.color == color and ((self.checkWayBishop(destx, desty) and (dx == dy)) or (
                    self.checkWayRook(destx, desty) and ((dx <= 7 and dy == 0) or (dy <= 7 and dx == 0)))):
            return True
        return False
