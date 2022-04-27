from turtle import Turtle

TABLE_DIMENSIONS = (153, 274)
TABLE_ZOOM = 4


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, TABLE_ZOOM * TABLE_DIMENSIONS[0] / 2 - 20)

        self.score = [0, 0]
        self.refresh_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center")

    def refresh_board(self):
        self.write(f"{self.score[0]}\t{self.score[1]}", align="center")

    def increment_score(self, player):
        self.score[player] += 1
        self.clear()
        self.refresh_board()

    def is_game_on(self):
        return self.score[0] < 5 and self.score[1] < 5
