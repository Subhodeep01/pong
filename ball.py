from turtle import Turtle

MOVEMENT = -10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_direction = MOVEMENT
        self.y_direction = MOVEMENT
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.x_direction
        y = self.ycor() + self.y_direction
        self.goto(x, y)

    def bounce_y(self):
        self.y_direction = -self.y_direction

    def bounce_x(self):
        self.x_direction = -self.x_direction
        self.move_speed *= 0.9

    def refresh(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
