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

    def spawn_food(self):
        self.food = Turtle()
        self.food.shape("square")
        self.food.color("red")
        self.food.penup()
        self.food.goto(random.randint(RAN_1, RAN_2), random.randint(RAN_1, RAN_2))

    def snake_run(self):
        self.prevx = 0
        self.prevy = 0
        if self.head.distance(self.food) < 20:
            self.food.reset()
            self.score.reset()
            self.foodscore +=1
            self.spawn_food()
            self.spawn_scoreboard()
            self.extend_snake()
            if self.sleep > 0.04:
                self.sleep -= 0.005
            elif self.sleep > 0.02:
                self.sleep -= 0.0025
            else:
                self.sleep -= 0.00125

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




    


    
