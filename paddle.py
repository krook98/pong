from turtle import Turtle
LEFT = (-350, 0)
RIGHT = (350, 0)


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.xcor()
        self.ycor()
        if side == 'left':
            self.goto(LEFT)
        else:
            self.goto(RIGHT)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



