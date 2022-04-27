import random
from scipy.stats import poisson

import consts
from car import Car
from road_map import RoadMap


class Traffic:
    def __init__(self):
        lamb = int(round(consts.NUM_TILES / 3, 0))
        dist = poisson.rvs(mu=lamb, size=consts.NUM_LANES - 2)

        self.map = RoadMap()
        self.max_rate = consts.NUM_TILES

        self.lanes = []
        for i in range(consts.NUM_LANES - 2):
            self.lanes.append({
                "rate": poisson.cdf(k=dist[i], mu=lamb),
                "speed": random.randrange(2, 4),
                "cars": [],
                "space": 0,
                "interval": 0
            })

            lane = self.lanes[i]
            lane["space"] = int(round(32 / lane["speed"] / 0.1, 0))

            heading = 180 * random.randrange(2)
            for j in range(dist[i]):
                y_init = self.map.get_center(i + 1)
                car = Car(heading, y_init)
                car.refresh()
                lane["cars"].append(car)

        self.spawn()

    def has_hit(self, carl):
        if carl.num_lane == 0 or carl.num_lane == consts.NUM_LANES - 1:
            return False

        lane = self.lanes[carl.num_lane - 1]
        for car in lane["cars"]:
            if carl.distance(car) < 15:
                return True

        return False

    def refresh(self):
        for lane in self.lanes:
            for car in lane["cars"]:
                car.refresh()

    def move(self):
        for lane in self.lanes:
            for car in lane["cars"]:
                if not car.isvisible():
                    continue

                car.forward(lane["speed"])
                if car.xcor() > consts.X_EDGE or car.xcor() < -consts.X_EDGE:
                    car.refresh()

    def spawn(self):
        for lane in self.lanes:
            if lane["interval"] > 0:
                lane["interval"] -= 1
                continue

            if random.random() > lane["rate"]:
                continue

            for car in lane["cars"]:
                if not car.isvisible():
                    lane["interval"] = lane["space"]
                    car.showturtle()
                    break
