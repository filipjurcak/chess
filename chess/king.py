from chess.figure import Figure


class King(Figure):
    def check(self, destx, desty, color, dx, dy):
        if dx <= 1 and dy <= 1 and self.color == color:
            return True
        return False
