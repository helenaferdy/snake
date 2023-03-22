from snake import Snake
from food import Food, FoodTurtle, Loggings, ScoreBoard
from wall import Wall
from turtle import Screen
import random

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
RAN_1 = -320
RAN_2 = 320
RAINBOW = ["green", "brown", "white", "yellow", "pink", "cyan"]

screen = Screen()
screen.bgcolor("gray")
screen.tracer(0)
screen.listen()

snekz = Snake()
fudz = Food()
fudz_turtle = FoodTurtle()
logz = Loggings()
top_wallz = Wall(0, 360)
bot_wallz = Wall(0, -390)

game_is_on = True
while game_is_on:
    snekz.snake_run()
    fudz_turtle.food_counter()
    fudz_turtle.fillcolor(random.choice(RAINBOW))

    for s in snekz.snakes[1:]:
        if s.distance(snekz.head) < 5:
            screen.bgcolor("black")
            game_is_on = False
            snekz.end_game()

    if snekz.head.distance(fudz) < 20:
        snekz.speed_up()
        snekz.extend_snake()
        fudz.spawn_food(random.randint(RAN_1, RAN_2), random.randint(RAN_1, RAN_2))

        randxz = random.randint(1, snekz.very_random_number)
        logz.info(f"randompoint ({randxz} : {snekz.very_random_number})")
        if randxz == snekz.very_random_number:
            fudz_turtle.spawn_food(random.randint(RAN_1, RAN_2), random.randint(RAN_1, RAN_2))

    if snekz.head.distance(fudz_turtle) < 20:
        snekz.slow_down()
        fudz_turtle.spawn_food(-900,-900)
        
    if snekz.head.ycor() > 335 or snekz.head.ycor() < -375:
        screen.bgcolor("black")
        game_is_on = False
        snekz.end_game()

    if snekz.head.xcor() > 480 and snekz.head.heading() == RIGHT or snekz.head.xcor() < -480 and snekz.head.heading() == LEFT:
        snekz.snake_teleport()
    
    screen.onkey(snekz.move_up, "w")
    screen.onkey(snekz.move_left, "a")
    screen.onkey(snekz.move_down, "s")
    screen.onkey(snekz.move_right, "d")
    screen.update()

screen.exitonclick()
