import time
from turtle import Screen

from snake import Snake
from food import Food


def main():
    screen = Screen()
    screen.setup(height=600, width=600)
    screen.bgcolor("black")

    screen.listen()
    screen.tracer(n=0)

    snake = Snake()
    food = Food()
    food.refresh()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while True:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()

    screen.exitonclick()


if __name__ == "__main__":
    main()
