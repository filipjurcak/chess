from Classes.Figure import Figure


class Knight(Figure):
    def __init__(self, a, b, color, image, board):
        self.a = a
        self.b = b
        self.color = color
        self.image = image
        self.board = board

    def check(self, destx, desty, whomoves):
        dx = abs(self.a - destx)
        dy = abs(self.b - desty)
        if whomoves % 2 == 1:
            a = 'black'
        else:
            a = 'white'
        if self.color == a and ((dx == 2 and dy == 1) or (dx == 1 and dy == 2)):
            return True
        return False