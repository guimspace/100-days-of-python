from random import randrange
from turtle import Screen


class TurtleRace:

    def __init__(self):
        self.cars = []

        self.screen = Screen()
        self.screen.colormode(255)

    def add_car(self, car):
        self.cars.append(car)

    def start(self):
        margin = 50

        w = margin + 600 + margin
        h = margin + margin * len(self.cars)
        self.screen.setup(width=w, height=h)

        w_offset = - w / 2
        h_offset = h / 2

        for car in self.cars:
            car.goto(w_offset + margin, h_offset - margin - margin * car.pos)

        winners = []
        while len(winners) == 0:
            for car in self.cars:
                car.car.forward(randrange(20))
                if car.car.xcor() >= 300 - margin:
                    winners.append(str(car.pos))

        print(f'The winners are: {", ".join(winners)}')


        self.screen.exitonclick()
