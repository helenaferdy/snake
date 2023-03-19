from turtle import Turtle
import random

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

RAN_1 = -380
RAN_2 = 380

class Snake:
    def __init__(self):
        self.spawn_snake()
        self.spawn_food()
        self.head = self.snakes[0]

    def spawn_snake(self):
        self.x = 0
        self.snakes = []
        for _ in range(3):
            s = Turtle()
            s.penup()
            s.shape("square")
            s.color("white")
            s.goto(self.x,0)

            self.x -= 20
            self.snakes.append(s)

    def spawn_food(self):
        self.food = Turtle()
        self.food.shape("square")
        self.food.color("red")
        self.food.penup()
        self.food.goto(random.randint(RAN_1, RAN_2), random.randint(RAN_1, RAN_2))

    def snake_run(self):
        if self.head.distance(self.food) < 20:
            self.food.reset()
            self.spawn_food()
        for snake in self.snakes:
            if snake == self.head:
                prevx, prevy = snake.pos()
                snake.fd(20)
            else:
                x, y = prevx, prevy
                prevx, prevy = snake.pos()
                snake.goto(x, y)
            

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




    


    
