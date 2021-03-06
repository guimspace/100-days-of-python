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

                result = False
                for id in self._vault:
                    try:
                        self.decrypt_item(self._vault[id], id)
                    except ValueError:
                        result = True

                if result:
                    raise ValueError

        except FileNotFoundError:
            with open(self._filepath, "w", encoding="utf-8") as vault:
                json.dump(self._vault, vault, indent=4)

    def add_item(self, item):
        id = uuid.uuid4()
        s_id = str(id)

        with open(self._filepath, "r+", encoding="utf-8") as vaultfile:
            vault = json.load(vaultfile)
            enc_item = self.encrypt_item(id, item)
            vault.update({s_id: enc_item})
            vaultfile.seek(0)
            json.dump(vault, vaultfile, indent=4)
            vaultfile.truncate()

        self._vault.update({s_id: item})

    def encrypt_item(self, id, item):
        enc_item = {}
        for key in item:
            enc_item[key] = BadCrypto.encrypt(self._password, item[key], id.bytes)
        return enc_item

    def decrypt_item(self, item, id):
        salt = uuid.UUID(id).bytes
        for key in item:
            item[key] = BadCrypto.decrypt(self._password, item[key], salt)

    def get_item(self, name):
        for key in self._vault:
            if name == self._vault[key]["name"]:
                return self._vault[key]
        return None
