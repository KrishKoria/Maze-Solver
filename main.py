from window import Window
from cell import Cell
def main():
    window = Window(800, 600)
    c = Cell(window)
    c.left_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(window)
    c.right_wall = False
    c.draw(125, 125, 200, 200)

    c = Cell(window)
    c.bottom_wall = False
    c.draw(225, 225, 250, 250)

    c = Cell(window)
    c.top_wall = False
    c.draw(300, 300, 500, 500)

    window.wait_for_close()


if __name__ == '__main__':
    main()   