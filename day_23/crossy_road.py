import time

from road import Road
from carl import Carl


def main():
    road = Road()
    carl = Carl()

    road.bind_keys(carl)

    while True:
        road.screen.update()
        time.sleep(0.1)

        if carl.has_arrived():
            road.screen.update()
            time.sleep(0.4)
            carl.refresh()

    road.exitonclick()


if __name__ == "__main__":
    main()
