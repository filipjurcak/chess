from chess.figure import Figure


class King(Figure):
    def check(self, destx, desty, dx, dy):
        return dx <= 1 and dy <= 1
