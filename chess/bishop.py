from chess.figure import Figure


class Bishop(Figure):
    def check(self, destx, desty, dx, dy):
        return self.check_way_bishop(destx, desty)

    def check_way_bishop(self, destx, desty):
        dx = destx - self.x
        dy = desty - self.y
        if abs(dx) != abs(dy) or (self.x == destx and self.y == desty):
            return False
        for i in range(1, abs(dx)):
            diffx = int(dx / abs(dx) * i)
            diffy = int(dy / abs(dy) * i)
            if self.board[self.x + diffx][self.y + diffy] == 1:
                return False
        return True
