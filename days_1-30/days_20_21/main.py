import time
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard

BOARD_LENGTH = 600


def main():
    board_edge = BOARD_LENGTH / 2 - 20

    screen = Screen()
    screen.setup(height=600, width=600)
    screen.bgcolor("black")

    screen.listen()
    screen.tracer(n=0)

    snake = Snake()

    food = Food()
    food.refresh()

    scoreboard = Scoreboard()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_on = True
    while scoreboard.has_lifes():
        if game_on:
            screen.update()
            time.sleep(0.1)
            snake.move()
        else:
            snake.die()
            snake = Snake()
            food.refresh()
            scoreboard.reset()
            screen.onkey(snake.up, "Up")
            screen.onkey(snake.down, "Down")
            screen.onkey(snake.left, "Left")
            screen.onkey(snake.right, "Right")
            game_on = True

        head_xcor = snake.head.xcor()
        head_ycor = snake.head.ycor()

        if head_xcor > board_edge or head_xcor < -board_edge:
            game_on = False
            continue
        elif head_ycor > board_edge or head_ycor < -board_edge:
            game_on = False
            continue

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.grow()
            scoreboard.increment_score()

        for seg in snake.segments[1:]:
            if snake.head.distance(seg["seg"]) < 10:
                game_on = False

    scoreboard.game_over()
    screen.exitonclick()


if __name__ == "__main__":
    main()
