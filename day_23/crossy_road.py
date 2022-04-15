import time

from road import Road
from carl import Carl
from traffic import Traffic


def main():
    road = Road()
    carl = Carl()
    traffic = Traffic()

    road.bind_keys(carl)

    while not traffic.has_hit(carl):
        road.screen.update()
        time.sleep(0.0167)

        if carl.has_arrived():
            road.screen.update()
            time.sleep(0.4)
            carl.refresh()
            traffic.refresh()

        traffic.spawn()
        traffic.move()

    road.exitonclick()


if __name__ == "__main__":
    main()
