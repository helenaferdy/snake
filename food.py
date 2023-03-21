from turtle import Turtle
import random
import logging, sys

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("pink")
        self.goto(-222,100)

        self.logz = Loggings()

    def spawn_food(self, x, y):
        self.logz.info(f"food spawned at {x},{y}")
        self.goto(x,y)

class FoodTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.fillcolor("cyan")
        self.goto(-900, -900)
        self.t_food_counter = 30

        self.logz = Loggings()

    def spawn_food(self, x, y):
        self.t_food_counter = random.randint(6,16)
        self.goto(x,y)
        self.logz.info(f"turtle food spawned at {x},{y}")

    def food_counter(self):
        self.t_food_counter -= 0.15
        if self.t_food_counter <= 0:
            self.goto(-900, -900)
        self.clear()
        self.write(round(self.t_food_counter, 1), font=("Arial", 15, "normal"))

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.fillcolor("white")
        self.hideturtle()
        self.goto(320, 370)
        self.write(f"SCORE : 0", font=("Arial", 20, "normal"))
    
    def update_score(self, score):
        self.score = score
        self.clear()
        self.write(f"SCORE : {self.score}", font=("Arial", 20, "normal"))

    
class Loggings():
    def __init__(self):
        LOG_LOCATION = "logs/snake.log"
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(message)s', 
            handlers=[
                logging.FileHandler(LOG_LOCATION),
                logging.StreamHandler(sys.stdout)
                ])
        
    def info(self, message):
        self.message = message
        logging.info(f"{self.message}")
