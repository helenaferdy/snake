from turtle import Turtle
import random
import time

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
RAN_1 = -350
RAN_2 = 350

class Snake:
    def __init__(self):
        self.foodscore = 0
        self.spawn_snake()
        self.spawn_food()
        self.spawn_food_turtle()
        self.spawn_scoreboard()
        self.head = self.snakes[0]
        self.sleep = 0.10
        

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

    def extend_snake(self):
        es = Turtle()
        es.penup()
        es.shape("square")
        es.color("white")
        es.goto(self.prevx, self.prevy)
        self.snakes.append(es)


    def snake_run(self):
        self.prevx = 0
        self.prevy = 0
        for snake in self.snakes:
            if snake == self.head:
                self.prevx, self.prevy = snake.pos()
                snake.fd(20)
            else:
                x, y = self.prevx, self.prevy
                self.prevx, self.prevy = snake.pos()
                snake.goto(x, y)
        time.sleep(round(self.sleep, 3))
            

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

    def spawn_scoreboard(self):
        self.score = Turtle()
        self.score.penup()
        self.score.color("white")
        self.score.fillcolor("white")
        self.score.hideturtle()
        self.score.goto(0, 350)
        self.score.write(f"SCORE : {self.foodscore}", font=("Arial", 20, "normal"))
        

    def spawn_food(self):
        self.food = Turtle()
        self.food.penup()
        self.food.shape("circle")
        self.food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.food.color("pink")
        self.food.goto(random.randint(RAN_1, RAN_2), random.randint(RAN_1, RAN_2))


    def spawn_food_turtle(self):
        self.turtlefood = Turtle()
        self.turtlefood.shape("turtle")
        self.turtlefood.penup()
        self.turtlefood.color("cyan")
        self.turtlefood.goto(-900,-900)
    


    
