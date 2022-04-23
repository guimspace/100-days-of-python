import csv


class BadVault:
    def __init__(self, filepath):
        self._filepath = filepath

        try:
            with open(filepath, "a", encoding="utf-8") as csvfile:
                print(f"BadVault: {filepath} ok")

        except Exception:
            print("BadVault: bad file")
            raise

    def append_item(self, item):
        with open(self._filepath, "a", encoding="utf-8") as csvfile:
            csv.DictWriter(csvfile,
                           fieldnames=("name", "username", "password")
                           ).writerow(item)
