from chess.figure import Figure


class King(Figure):
    def check(self, destx, desty, dx, dy):
        if dx <= 1 and dy <= 1:
            return True
        return False
