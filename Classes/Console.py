from Classes.Game import Game


class Console:
    def __init__(self, state):
        self.game = Game()
        if state == 'yes':
            self.game.load()
        else:
            self.game.create()

    def start(self):
        self.chess_setup()
        while True:
            if self.game.whomoves % 2 == 0:
                print ("White's turn")
            if self.game.whomoves % 2 == 1:
                print ("Black's turn")
            start = raw_input('Figure on which positions do you wanna move? If you want to save your game, type save.\n')
            if start == 'save':
                name = raw_input('Type name of file in which you wanna save the game.\n')
                name += '.txt'
                self.game.save(name)
                start = raw_input('Figure on which positions do you wanna move?\n')
            startx = self.positions(start)
            dest = raw_input('Where do you wanna move it?\n')
            destx = self.positions(dest)
            move = self.game.move(startx[0], startx[1], destx[0], destx[1])
            if move != 0:
                if move == 1:
                    print ("Whites are Winners")
                if move == 2:
                    print ("Blacks are Winners")
                return

    def chess_setup(self):
        for i in range(len(self.game.figures)):
            self.game.board[self.game.figures[i].a][self.game.figures[i].b] += 1

    def positions(self, position):
        return int(position.split()[0]), int(position.split()[1])
