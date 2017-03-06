from chess.visualizer import Visualizer
from chess.console import Console


def main():
    square = 720
    name = ''
    while name != "console" and name != "visualizer" and name != "ice cream":
        name = input("What do you want?\n")
    if name == "ice cream":
        return print("Buy yourself\n")
    if name == "console" or name == "visualizer":
        state = input("Do you wanna load saved game?\n")
        if name == "console":
            game = Console(state)
        if name == "visualizer":
            game = Visualizer(square, state)
    game.start()
if __name__ == '__main__':
    main()
