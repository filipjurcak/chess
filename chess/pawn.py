from chess.figure import Figure


class Pawn(Figure):
    def __init__(self, x, y, color, image, board):
        super().__init__(x, y, color, image, board)

    def check(self, destx, desty, color, dx, dy):
        dy = self.y - desty
        if self.color == 'white' == color and 0 < dy <= 2 and 0 <= dx <= 1:
            if self.y == 6 and dy == 2 and dx == 0 and self.board[destx][desty + 1] == 0 and self.board[destx][desty] == 0:
                return True
            if dy == 1 and dx == 0 and self.board[destx][desty] == 0:
                return True
            if dy == 1 and dx == 1 and self.board[destx][desty] == 1:
                return True
            return False
        if self.color == 'black' == color and 0 < -dy <= 2 and 0 <= dx <= 1:
            if self.y == 1 and -dy == 2 and dx == 0 and self.board[destx][desty - 1] == 0 and self.board[destx][desty] == 0:
                return True
            if -dy == 1 and dx == 0 and self.board[destx][desty] == 0:
                return True
            if -dy == 1 and dx == 1 and self.board[destx][desty] == 1:
                return True
            return False
