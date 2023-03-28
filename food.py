from turtle import Turtle
import random

TURTLE_GREEN = "#006400"
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color(TURTLE_GREEN)
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.penup()
        self.speed("fastest")
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)