from Classes.Figure import Figure


class Bishop(Figure):
    def __init__(self, x, y, color, image, board):
        super().__init__(x, y, color, image, board)

    def check(self, destx, desty, color, dx, dy):
        if dx <= 7 and dy <= 7 and self.checkWayBishop(destx, desty) and self.color == color and dx == dy:
            return True
        return False

    def checkWayBishop(self, destx, desty):
        dx = destx - self.x
        dy = desty - self.y
        if abs(dx) != abs(dy):
            return False
        for i in range(abs(dx) - 1):
            if self.board[self.x + int(dx/abs(dx)*(i + 1))][self.y + int(dy/abs(dy)*(i + 1))] == 1:
                return False
        return True
