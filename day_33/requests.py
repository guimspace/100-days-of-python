import requests
from datetime import datetime


def main():
    parameters = {
        "lat": 51.5285582,
        "lng": -0.2416815,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json",
                            params=parameters)
    response.raise_for_status()
    print(response.status_code)

    data = response.json()
    now = datetime.now()
    print(now, data)


if __name__ == "__main__":
    main()
