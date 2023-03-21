from snake import Snake
from turtle import Screen
import random

RAN_1 = -350
RAN_2 = 350
VERY_RANDOM_NUMBER = 10

screen = Screen()
screen.bgcolor("gray")
screen.tracer(0)
screen.listen()
snekz = Snake()

game_is_on = True
while game_is_on:
    snekz.snake_run()

    if snekz.head.distance(snekz.food) < 20:
        snekz.score.clear()
        snekz.foodscore +=1
        snekz.food.goto(random.randint(RAN_1, RAN_2), random.randint(RAN_1, RAN_2))
        snekz.score.write(f"SCORE : {snekz.foodscore}", font=("Arial", 20, "normal"))
        snekz.extend_snake()
        if snekz.sleep > 0.04:
            snekz.sleep -= 0.005
        elif snekz.sleep > 0.02:
            snekz.sleep -= 0.0025
        else:
            snekz.sleep -= 0.00125

        if snekz.foodscore == 4:
            VERY_RANDOM_NUMBER = 7
        if snekz.foodscore == 8:
            VERY_RANDOM_NUMBER = 5
        if snekz.foodscore == 15:
            VERY_RANDOM_NUMBER = 3

        randxz = random.randint(1, VERY_RANDOM_NUMBER)
        print(f"randxz : {randxz}, veryrandom : {VERY_RANDOM_NUMBER}")
        if  randxz == VERY_RANDOM_NUMBER:
            snekz.turtlefood.goto(random.randint(RAN_1, RAN_2), random.randint(RAN_1, RAN_2))


    if snekz.head.distance(snekz.turtlefood) < 20:
        snekz.score.clear()
        snekz.turtlefood.goto(-900,-900)
        snekz.foodscore +=1
        snekz.score.write(f"SCORE : {snekz.foodscore}", font=("Arial", 20, "normal"))
        snekz.sleep += 0.020

    

    screen.onkey(snekz.move_up, "w")
    screen.onkey(snekz.move_left, "a")
    screen.onkey(snekz.move_down, "s")
    screen.onkey(snekz.move_right, "d")

    screen.update()



screen.exitonclick()
