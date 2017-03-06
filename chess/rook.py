from chess.figure import Figure


class Rook(Figure):
    def check(self, destx, desty, dx, dy):
        return self.check_way_rook(destx, desty)

    def check_way_rook(self, destx, desty):
        dx = destx - self.x
        dy = desty - self.y
        if dx != 0 and dy != 0 or (self.x == destx and self.y == desty):
            return False
        for i in range(1, max(abs(dy), abs(dx))):
            if dx == 0:
                diffy = int(dy / abs(dy) * i)
                if self.board[self.x][self.y + diffy] == 1:
                    return False
            if dy == 0:
                diffx = int(dx / abs(dx) * i)
                if self.board[self.x + diffx][self.y] == 1:
                    return False
        return True
