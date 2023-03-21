from snake import Snake
from turtle import Screen
import random
import logging, sys

RAN_1 = -350
RAN_2 = 350
T_FOOD_COUNTER = 20
t_food_counter = T_FOOD_COUNTER

LOG_LOCATION = "logs/debug.log"
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

game_is_on = True
while game_is_on:
    snekz.snake_run()
    t_food_counter -= 0.15

    snekz.turtlefood.clear()
    snekz.turtlefood.write(round(t_food_counter, 1), font=("Arial", 15, "normal"))

    if snekz.sleep > 0.10:
        snekz.sleep = 0.10

    if snekz.head.distance(snekz.food) < 20:
        snekz.speed_up()
        snekz.score.clear()
        snekz.foodscore +=1
        snekz.score.write(f"SCORE : {snekz.foodscore}", font=("Arial", 20, "normal"))
        logging.info(f"snake eats food at {snekz.head.pos()}")

        food_randomx = random.randint(RAN_1, RAN_2)
        food_randomy = random.randint(RAN_1, RAN_2)
        snekz.food.goto(food_randomx, food_randomy)
        logging.info(f"food spawned at {food_randomx},{food_randomy}")

        snekz.extend_snake()
        logging.info(f"snake speed {round(snekz.sleep, 3)}")

        randxz = random.randint(1, snekz.very_random_number)
        logging.info(f"randompoint ({randxz} : {snekz.very_random_number})")
        if  randxz == snekz.very_random_number:
            food_randomx = random.randint(RAN_1, RAN_2)
            food_randomy = random.randint(RAN_1, RAN_2)
            snekz.turtlefood.goto(food_randomx, food_randomy)
            t_food_counter = T_FOOD_COUNTER
            logging.info(f"food turtle spawned at {food_randomx},{food_randomy}")


    if snekz.head.distance(snekz.turtlefood) < 20:
        logging.info(f"snake eats food turtle at {snekz.head.pos()}")
        snekz.slow_down()
        
        snekz.score.clear()
        snekz.foodscore +=1
        snekz.turtlefood.goto(-900,-900)
        snekz.score.write(f"SCORE : {snekz.foodscore}", font=("Arial", 20, "normal"))
        logging.info(f"snake speed {round(snekz.sleep, 3)}")

    
    screen.onkey(snekz.move_up, "w")
    screen.onkey(snekz.move_left, "a")
    screen.onkey(snekz.move_down, "s")
    screen.onkey(snekz.move_right, "d")
    screen.update()

screen.exitonclick()
