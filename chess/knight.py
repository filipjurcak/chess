from chess.figure import Figure


class Knight(Figure):
    def check(self, destx, desty, dx, dy):
        if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
            return True
        return False
