from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.high_score = 0
        self.lifes = 5

        with open("snake.data") as save:
            self.high_score = int(save.read())

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)

        self.refresh_board()

    def has_lifes(self):
        return self.lifes > 0

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake.data", "w") as save:
                save.write(str(self.high_score))

        self.score = 0
        self.lifes -= 1
        self.refresh_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center")

    def refresh_board(self):
        self.clear()
        self.write(f"Lifes: {self.lifes}\tScore: {self.score}\tHigh score: {self.high_score}", align="center")

    def increment_score(self):
        self.score += 1
        self.refresh_board()
