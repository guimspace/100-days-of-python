import csv


class BadDb:
    def __init__(self, filepath):
        self._filepath = filepath

        try:
            with open(filepath, "a", encoding="utf-8") as csvfile:
                print(f"BadDb: {filepath} ok")

        except Exception:
            print("BadDb: bad file")
            raise

    def append_item(self, item):
        with open(self._filepath, "a", encoding="utf-8") as csvfile:
            csv.DictWriter(csvfile,
                           fieldnames=("name", "username", "password")
                           ).writerow(item)
