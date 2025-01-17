from window import Window
from cell import Cell
def main():
    window = Window(800, 600)
    c1 = Cell(window)
    c1.right_wall = False
    c1.draw(50, 50, 100, 100)

    c2 = Cell(window)
    c2.left_wall = False
    c2.bottom_wall = False
    c2.draw(100, 50, 150, 100)

    c1.draw_move(c2)

    c3 = Cell(window)
    c3.top_wall = False
    c3.right_wall = False
    c3.draw(100, 100, 150, 150)

    c2.draw_move(c3)

    c4 = Cell(window)
    c4.left_wall = False
    c4.draw(150, 100, 200, 150)

    c3.draw_move(c4, True)
    window.wait_for_close()


if __name__ == '__main__':
    main()   