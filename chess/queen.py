from chess.bishop import Bishop
from chess.rook import Rook


class Queen(Rook, Bishop):
    def check(self, destx, desty, color, dx, dy):
        if self.color == color and (self.checkWayBishop(destx, desty) or self.checkWayRook(destx, desty)):
            return True
        return False
