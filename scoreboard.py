from turtle import Turtle

FONT = ("Courier", 8, "normal")
ALIGN = "center"


class ScoreBoard(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.scr = 0
        self.hideturtle()
        self.penup()
        self.goto(pos)
        self.pencolor("white")
        self.write(arg=f"Player Score: {self.scr}", align=ALIGN, font=FONT)

    def update(self):
        self.scr += 1
        self.clear()
        self.write(arg=f"Player Score: {self.scr}", align=ALIGN, font=FONT)
