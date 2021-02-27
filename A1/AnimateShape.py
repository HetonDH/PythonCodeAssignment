# Chenyue Hu u1275460
# Assignment 1 Animate shape

from graphics import *

def eyes(x, y, win):
    c1 = Circle(Point(x, y), 20)
    c1.setFill("white")
    c1.draw(win)

def draw_a_line(x,y,win):
    aline = Line(Point(x,y), Point(x + 20, y))
    aline.draw(win)

def shape_body(x, y, win):
    body1 = Oval(Point(x, y), Point(x+200,y+150))
    body1.setFill("pink")
    body1.draw(win)

def tail(x,y,win):
    aRectangle = Rectangle(Point(x, y), Point(x+100, y+30))
    aRectangle.setFill("purple")
    aRectangle.draw(win)

def draw_my_shape(x,y,win):
    shape_body(x,y,win)
    draw_a_line(x+10,y+100,win)
    eyes(x+50, y+50, win)
    tail(x+170,y+100,win)
    tail(x+170,y+50,win)



def main():
    win = GraphWin('Drawing', 700, 500, autoflush=False)
    win.setBackground('blue')

    while True:
        win.clear_win()
        point = win.getMousePosition()
        x = point.getX()
        y = point.getY()
        draw_my_shape(x, y, win)
        win.update()

if __name__ == "__main__":
    main()