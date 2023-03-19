from snake import Snake
import time
from turtle import Screen

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
snekz = Snake()

game_is_on = True
while game_is_on:
    snekz.snake_run()

    screen.onkey(snekz.move_up, "w")
    screen.onkey(snekz.move_left, "a")
    screen.onkey(snekz.move_down, "s")
    screen.onkey(snekz.move_right, "d")

    time.sleep(0.1)
    screen.update()









screen.exitonclick()
