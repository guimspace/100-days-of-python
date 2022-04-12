from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)

        self.score = 0
        self.refresh_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center")

    def refresh_board(self):
        self.write(f"Score: {self.score}", align="center")

    def increment_score(self):
        self.score += 1
        self.clear()
        self.refresh_board()
