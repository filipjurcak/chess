from Classes.Figure import Figure


class Rook(Figure):
    def __init__(self, x, y, color, image, board):
        super().__init__(x, y, color, image, board)

    def check(self, destx, desty, color, dx, dy):
        if dx <= 7 and dy <= 7 and self.color == color and ((dx <= 7 and dy == 0) or (dy <= 7 and dx == 0)) and \
                self.checkWayRook(destx, desty):
            return True
        return False

    def checkWayRook(self, destx, desty):
        dx = destx - self.x
        dy = desty - self.y
        if dx != 0 and dy != 0:
            return False
        for i in range(max(abs(dy), abs(dx)) - 1):
            if (dx == 0 and self.board[self.x][self.y + int(dy / abs(dy) * (i + 1))] == 1) or \
                    (dy == 0 and self.board[self.x + int(dx / abs(dx) * (i + 1))][self.y] == 1):
                return False
        return True
