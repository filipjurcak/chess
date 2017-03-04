from Classes.Figure import Figure


class King(Figure):
    def __init__(self, x, y, color, image, board):
        super().__init__(x, y, color, image, board)

    def check(self, destx, desty, color, dx, dy):
        if -1 <= dx <= 1 and -1 <= dy <= 1 and self.color == color:
            return True
        return False
