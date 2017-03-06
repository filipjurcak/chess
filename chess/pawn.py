from chess.figure import Figure


class Pawn(Figure):
    def check(self, destx, desty, color, dx, dy):
        if ((self.color == 'black' == color and self.y < desty) or (self.color == 'white' == color and self.y > desty)) \
                and 0 < dy <= 2 and 0 <= dx <= 1:
            if dy == 2 and dx == 0:
                if self.y == 6 and self.board[destx][desty + 1] == 0 and self.board[destx][
                        desty] == 0 and self.color == 'white':
                    return True
                if self.y == 1 and self.board[destx][desty - 1] == 0 and self.board[destx][
                        desty] == 0 and self.color == 'black':
                    return True
            if dy == 1 and dx == 0 and self.board[destx][desty] == 0:
                return True
            if dy == 1 and dx == 1 and self.board[destx][desty] == 1:
                return True
        return False
