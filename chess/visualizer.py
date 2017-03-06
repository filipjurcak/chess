from tkinter import *
from PIL import Image, ImageTk
from chess.game import Game


class Visualizer:
    def __init__(self, square, state):
        self.game = Game()
        if state == 'yes' or state == 'Yes':
            self.game.load()
        else:
            self.game.create()
        self.main = Tk()
        self.w = Canvas(self.main, width=square, height=square + square / 8)
        self.w.pack()
        self.w.bind('<Button-3>', self.firstclick)
        self.w.bind('<Button-1>', self.secondClick)
        self.square = square
        self.small_square = square / 8
        self.weak_reference = []
        self.quit = False

    def create_chess(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    m = "saddle brown"
                else:
                    m = "wheat"
                self.w.create_rectangle(i * self.small_square, j * self.small_square, (i + 1) * self.small_square,
                                        (j + 1) * self.small_square, fill=m)
        self.w.create_rectangle(0, self.square, self.square / 2, self.square + self.square / 8, fill='orange2')
        self.w.create_text(self.square / 4, self.square + self.square / 16, fill='white', font=('Purisa', 50),
                           text="Save")
        self.w.create_rectangle(self.square / 2, self.square, self.square, self.square + self.square / 8, fill='gray1')
        self.w.create_text(self.square - self.square / 4, self.square + self.square / 16, fill='white',
                           font=('Purisa', 50), text="Quit")

    def chess_setup(self):
        for figure in self.game.figures:
            figure.image = figure.image.resize((int(self.small_square), int(self.small_square)), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(figure.image)
            self.weak_reference.append(photo)
            self.w.create_image((figure.x * self.small_square) + self.small_square / 2,
                                (figure.y * self.small_square) + self.small_square / 2, image=photo)
            self.game.board[figure.x][figure.y] = 1

    def visualize_valid_moves(self, startx, starty, color):
        for i in range(8):
            for j in range(8):
                if self.game.control(startx, starty, i, j):
                    if self.game.board[i][j] == 1:
                        for figure in self.game.figures:
                            if figure.x == i and figure.y == j:
                                if figure.color == color:
                                    if (i + j) % 2 == 0:
                                        m = "saddle brown"
                                    else:
                                        m = "wheat"
                                else:
                                    m = "red"
                                break
                    else:
                        m = "green yellow"
                else:
                    if (i + j) % 2 == 0:
                        m = "saddle brown"
                    else:
                        m = "wheat"
                self.w.create_rectangle(i * self.small_square, j * self.small_square, (i + 1) * self.small_square,
                                        (j + 1) * self.small_square, fill=m)
        self.chess_setup()

    def firstclick(self, event):
        if self.quit:
            quit()
        self.startx = int(event.x / self.small_square)
        self.starty = int(event.y / self.small_square)
        if self.starty == 8:
            if 0 <= self.startx <= 3:
                self.save()
            else:
                quit()
        chosen_figure = [val for val in self.game.figures if (self.startx == val.x and self.starty == val.y)]
        self.visualize_valid_moves(self.startx, self.starty, chosen_figure[0].color)

    def secondClick(self, event):
        if self.quit:
            quit()
        self.destx = int(event.x / self.small_square)
        self.desty = int(event.y / self.small_square)
        if self.desty == 8:
            if 0 <= self.destx <= 3:
                self.save()
            else:
                quit()
        else:
            move = self.game.move(self.startx, self.starty, self.destx, self.desty)
            if move != 0:
                if move == 1 or move == 2:
                    if move == 1:
                        m = 'white'
                    else:
                        m = 'black'
                    self.w.create_text(self.square / 2, self.square / 2, fill=m, font=('Purisa', 100), text="Winner")
                    self.quit = True
                return
        self.redraw()

    def delete_stoogles(self):
        for figure in self.game.figures:
            self.w.delete("all")
            self.game.board[figure.x][figure.y] = 0
            self.weak_reference = []

    def redraw(self):
        self.delete_stoogles()
        self.create_chess()
        self.chess_setup()

    def start(self):
        self.redraw()
        self.main.mainloop()

    def save(self):
        name = input("Type name of file in which you wanna save the game:\n")
        name += '.txt'
        self.game.save(name)
