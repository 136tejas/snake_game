from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def incease_score(self):
        self.score += 5
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGN, font=FONT)
