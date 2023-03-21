from snake import Snake
from food import Food, FoodTurtle
from turtle import Screen
import random
import logging, sys

RAN_1 = -350
RAN_2 = 350

LOG_LOCATION = "logs/snake.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s', 
    handlers=[
        logging.FileHandler(LOG_LOCATION),
        logging.StreamHandler(sys.stdout)
        ])

screen = Screen()
screen.bgcolor("gray")
screen.tracer(0)
screen.listen()

snekz = Snake()
fudz = Food()
fudz_turtle = FoodTurtle()

game_is_on = True
while game_is_on:
    snekz.snake_run()
    fudz_turtle.food_counter()

    if snekz.head.distance(fudz) < 20:
        snekz.speed_up()
        snekz.extend_snake()

        food_randomx = random.randint(RAN_1, RAN_2)
        food_randomy = random.randint(RAN_1, RAN_2)
        fudz.spawn_food(food_randomx, food_randomy)

        randxz = random.randint(1, snekz.very_random_number)
        logging.info(f"randompoint ({randxz} : {snekz.very_random_number})")
        if randxz == snekz.very_random_number:
            food_randomx = random.randint(RAN_1, RAN_2)
            food_randomy = random.randint(RAN_1, RAN_2)

            fudz_turtle.spawn_food(food_randomx, food_randomy)

    if snekz.head.distance(fudz_turtle) < 20:
        snekz.slow_down()
        fudz_turtle.spawn_food(-900,-900)
        
    
    screen.onkey(snekz.move_up, "w")
    screen.onkey(snekz.move_left, "a")
    screen.onkey(snekz.move_down, "s")
    screen.onkey(snekz.move_right, "d")
    screen.update()

screen.exitonclick()
