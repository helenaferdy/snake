from turtle import Turtle


class Snake:
    def __init__(self):
        self.spawn_snake()

    def spawn_snake(self):
        self.x = 0
        self.snakes = []
        for i in range(3):
            s = Turtle()
            s.penup()
            s.shape("square")
            s.color("white")
            s.goto(self.x,0)

            self.x -= 20

            self.snakes.append(s)

    def snake_run(self):
        i = 0
        for snake in self.snakes:
            if i == 0:
                prevx, prevy = snake.pos()
                snake.fd(20)
            else:
                x, y = prevx, prevy
                prevx, prevy = snake.pos()
                snake.goto(x, y)
            i +=1

    def move_up(self):
        self.snakes[0].setheading(90)

    def move_left(self):
        self.snakes[0].setheading(180)

    def move_down(self):
        self.snakes[0].setheading(270)

    def move_right(self):
        self.snakes[0].setheading(0)