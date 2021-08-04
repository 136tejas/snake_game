from turtle import Turtle
import random

color = ["red", "blue", "green", "yellow", "purple"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.60, stretch_len=0.60)
        self.color(random.choice(color))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        ran_x = random.randint(-280, 280)
        ran_y = random.randint(-280, 280)
        self.goto(ran_x, ran_y)
