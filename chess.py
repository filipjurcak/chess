from Classes.Visualizer import Visualizer
from Classes.Console import Console


def main():
    square = 720
    a = ""
    while a != "console" or a != "visualizer" or a != "ice cream":
        a = input("What do you want?\n")
        if a == "console" or a == "visualizer" or a == "ice cream":
            break
    if a == "ice cream":
        print("Buy yourself\n")
        return
    if a == "console" or a == "visualizer":
        c = input("Do you wanna load saved game?\n")
        if a == "console":
            b = Console(c)
        if a == "visualizer":
            b = Visualizer(square, c)
    b.start()
if __name__ == '__main__':
    main()
