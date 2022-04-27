from turtle_race import TurtleRace
from not_car import NotCar


def main():
    race = TurtleRace()

    car = NotCar(1, (255, 0, 0))
    race.add_car(car)

    for p in range(2, 7):
        car = NotCar(p)
        race.add_car(car)

    race.start()


if __name__ == "__main__":
    main()
