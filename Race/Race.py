from Dice import *
from graphics import *
from random import randint

class Horse:

    X_pos = 50

    def __init__(self, speed_number, Y_pos, image, Window):
        self.dice = Dice(speed_number)
        self.Y_pos = Y_pos
        self.image = image
        self.Window = Window

    def move(self):
        self.X_pos = self.dice.roll() + self.X_pos

    def draw(self):
        self.image.draw_at_pos(self.Window, self.X_pos, self.Y_pos)

    def crossed_finish_line(self, X_pos_finish):
        if self.X_pos >= X_pos_finish:
            return True
        else:
            return False


def main():
    Window = GraphWin(title="Horse Race", width=700, height=350, autoflush=False)
    Window.setBackground("white")

    image1 = Image(Point(0, 0), "Knight.gif")
    image2 = Image(Point(0, 0), "Wizard.gif")

    random_speed = randint(1, 5)

    horse1 = Horse(random_speed, 100, image1, Window)
    horse2 = Horse(random_speed, 250, image2, Window)

    horse1.draw()
    horse2.draw()

    destination = Line(Point(630, 0), Point(630, 350))
    destination.setFill("red")
    destination.draw(Window)

    Window.getMouse()

    while not horse1.crossed_finish_line(666) and not horse2.crossed_finish_line(666):

        Window.clear_win()

        horse1.move()
        horse2.move()

        horse1.draw()
        horse2.draw()
        destination.draw(Window)

        Window.update()

    if horse1.crossed_finish_line(666) and horse2.crossed_finish_line(666):
        print("Tie")

    if horse1.crossed_finish_line(666):
        print("Horse 1 is winner!")

    else:
        horse2.crossed_finish_line(666)
        print("Horse 2 is winner!")

if __name__ == "__main__":
    main()






