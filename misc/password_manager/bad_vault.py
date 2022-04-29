import json
import uuid


class BadVault:
    def __init__(self, filepath):
        self._filepath = filepath
        self._vault = {}

        try:
            with open(filepath, "r", encoding="utf-8") as vault:
                self._vault = json.load(vault)
        except FileNotFoundError:
            with open(filepath, "w", encoding="utf-8") as vault:
                json.dump(self._vault, vault, indent=4)

        print("BadVault: ok")

    def add_item(self, item):
        item_uuid = str(uuid.uuid4())
        self._vault.update({item_uuid: item})

        with open(self._filepath, "w", encoding="utf-8") as vault:
            json.dump(self._vault, vault, indent=4)
            print("BadVault: item added")

    def get_item(self, name):
        for key in self._vault:
            if name == self._vault[key]["name"]:
                return self._vault[key]
        return None
