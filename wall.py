from turtle import Turtle

class Wall:
    def __init__(self, x, y):
        self = Turtle()
        self.x = x
        self.y = y
        self.shape("square")
        self.color("black")
        self.penup()
        self.shapesize(1,400)
        self.goto(self.x, self.y)