from chess.bishop import Bishop
from chess.rook import Rook


class Queen(Rook, Bishop):
    def check(self, destx, desty, dx, dy):
        return self.check_way_bishop(destx, desty) or self.check_way_rook(destx, desty)
