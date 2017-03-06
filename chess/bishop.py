from chess.figure import Figure


class Bishop(Figure):
    def check(self, destx, desty, dx, dy):
        if self.check_way_bishop(destx, desty):
            return True
        return False

    def check_way_bishop(self, destx, desty):
        dx = destx - self.x
        dy = desty - self.y
        if abs(dx) != abs(dy) or (self.x == destx and self.y == desty):
            return False
        for i in range(abs(dx) - 1):
            diffx = int(dx / abs(dx) * (i + 1))
            diffy = int(dy / abs(dy) * (i + 1))
            if self.board[self.x + diffx][self.y + diffy] == 1:
                return False
        return True
