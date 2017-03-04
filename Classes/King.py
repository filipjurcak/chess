from Classes.Figure import Figure


class King(Figure):
    def __init__(self, a, b, color, image, board):
        self.a = a
        self.b = b
        self.color = color
        self.image = image
        self.board = board

    def check(self, destx, desty, whomoves):
        if whomoves % 2 == 1:
            a = 'black'
        else:
            a = 'white'
        if -1 <= (self.a - destx) <= 1 and -1 <= (self.b - desty) <= 1 and self.color == a:
            return True
        return False