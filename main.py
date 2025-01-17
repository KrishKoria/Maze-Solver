from window import Window
from point import Point, Line
def main():
    window = Window(800, 600)
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    line = Line(p1, p2)
    window.draw_line(line, 'red')

    window.wait_for_close()


if __name__ == '__main__':
    main()   