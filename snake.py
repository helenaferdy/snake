from turtle import Turtle
from food import ScoreBoard, Loggings
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
        self.very_random_number = 8
        self.sleep = 0.10

        self.spawn_snake()
        self.head = self.snakes[0]
        self.scorz = ScoreBoard()
        self.logz = Loggings()
    
    def snake_run(self):
        time.sleep(round(self.sleep, 3))
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
        
        # for s in self.snakes[1:]:
        #     if s.distance(self.head) < 20:
        #         self.end_game()

    def snake_teleport(self):
        self.prevx, self.prevy = self.head.pos()
        self.prevx = self.prevx * -1
        self.logz.info(f"snake teleports from {self.head.pos()} to {self.prevx, self.prevy}")
        self.head.goto(self.prevx, self.prevy)

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

    def speed_up(self):
        self.logz.info(f"snake eats food at {self.head.pos()}")
        if self.sleep > 0.04:
            self.sleep -= 0.005
        elif self.sleep > 0.02:
            self.sleep -= 0.0025
        else:
            self.sleep -= 0.00125
        self.refresh()

    def slow_down(self):
        self.logz.info(f"snake eats turtle food at {self.head.pos()}")
        self.sleep += 0.020
        self.refresh()

        if self.sleep > 0.10:
            self.sleep = 0.10

    def refresh(self):
        self.logz.info(f"snake speed {round(self.sleep, 3)}")
        self.foodscore +=1
        self.scorz.update_score(self.foodscore)

        if self.foodscore == 4:
            self.very_random_number -= 2
        if self.foodscore == 8:
            self.very_random_number -= 2
        if self.foodscore == 15:
            self.very_random_number -= 1

    def end_game(self):
        eg = ScoreBoard()
        eg.goto(0, 0)
        eg.color("pink")
        eg.write(f"GAME OVER", font=("Arial", 40, "bold"), align="center")
        self.logz.info(f"game over at {self.head.pos()} with score {self.foodscore}")

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


        



    
