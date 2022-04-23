import json
import uuid

from askpw import AskPw
from badcrypto import BadCrypto


class BadVault:
    def __init__(self, filepath):
        self._filepath = filepath
        self._vault = {}
        self._password = ""

    def open_vault(self):
        self._password = AskPw.ask("Open Vault")
        if self._password is None or len(self._password) == 0:
            raise ValueError("Invalid password.")

        try:
            with open(self._filepath, "r", encoding="utf-8") as vault:
                self._vault = json.load(vault)
        except FileNotFoundError:
            with open(self._filepath, "w", encoding="utf-8") as vault:
                json.dump(self._vault, vault, indent=4)

    def add_item(self, item):
        item_uuid = str(uuid.uuid4())
        enc_item = self.encrypt_item(item)
        self._vault.update({item_uuid: enc_item})

        with open(self._filepath, "w", encoding="utf-8") as vault:
            json.dump(self._vault, vault, indent=4)
            print("BadVault: item added")

    def encrypt_item(self, item):
        for key in item:
            item[key] = BadCrypto.encrypt(self._password, item[key])
        return item

    def get_item(self, name):
        for key in self._vault:
            if name == self._vault[key]["name"]:
                return self._vault[key]
        return None
