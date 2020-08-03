from graphics import *

win_width = 600
win_height = 500

def main():
    global win
    win = GraphWin("Picture", win_width, win_height)
    draw_house(win_width//3, win_height*2//3, 150, 200)
    cursor_point = win.getMouse()
    win.close()

def draw_house(x0, y0, width, height):
    """
    :param x0: центральная нижняя точка дома
    :param y0: центральная нижняя точка дома
    :param width: ширина
    :param height: высота
    :return:
    """
    foundation_height = int(height * 0.1)
    walls_height = int(0.5 * height)
    walls_width = int(0.9 * width)
    roof_height = height - walls_height
    window_height = walls_height // 3
    window_width = walls_width // 3

    draw_foundation(x0,y0, width, foundation_height)
    draw_walls(x0, y0 - foundation_height, width, walls_height)
    draw_window(x0, y0 - foundation_height - walls_height, window_height, window_width)
    draw_roof(x0, y0-walls_height, width, roof_height)

def draw_foundation(x0, y0, width, height):
    foundation = Rectangle(Point(x0 - width//2, y0 - height), Point(x0 + width//2, y0))
    foundation.setWidth(3)
    foundation.setFill("Brown")
    foundation.draw(win)

def draw_walls(x0, y0, width, height):
    pass

def draw_window(x0, y0, width, height):
    pass

def draw_roof(x0, y0, width, height):
    pass

main()

