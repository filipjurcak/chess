from chess.figure import Figure


class Knight(Figure):
    def __init__(self, x, y, color, image, board):
        super().__init__(x, y, color, image, board)

    def check(self, destx, desty, color, dx, dy):
        if self.color == color and ((dx == 2 and dy == 1) or (dx == 1 and dy == 2)):
            return True
        return False
