from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.setpos(position)


    def go_up(self):
        self.setpos(self.xcor(), self.ycor() + 20)


    def go_down(self):
        self.setpos(self.xcor(), self.ycor() - 20)
