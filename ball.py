from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.setpos(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move = -self.y_move

    def bounce_x(self):
        self.x_move = -self.x_move


    def reset(self):
        self.setpos(0, 0)
        self.x_move = -self.x_move