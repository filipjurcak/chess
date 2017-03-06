from chess.figure import Figure


class Bishop(Figure):
    def check(self, destx, desty, color, dx, dy):
        if self.checkWayBishop(destx, desty) and self.color == color:
            return True
        return False

    def checkWayBishop(self, destx, desty):
        dx = destx - self.x
        dy = desty - self.y
        if abs(dx) != abs(dy):
            return False
        for i in range(abs(dx) - 1):
            diffx = int(dx / abs(dx) * (i + 1))
            diffy = int(dy / abs(dy) * (i + 1))
            if self.board[self.x + diffx][self.y + diffy] == 1:
                return False
        return True
