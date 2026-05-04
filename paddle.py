from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


    def up(self):
        ney_y = self.ycor() + 50
        self.goto(self.xcor(), ney_y)


    def down(self):
        ney_y = self.ycor() - 50
        self.goto(self.xcor(), ney_y)