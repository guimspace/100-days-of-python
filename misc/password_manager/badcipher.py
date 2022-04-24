from cryptography.exceptions import AlreadyFinalized
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class BadCipher:
    def sha256sum(message):
        sha256sum = hashes.Hash(hashes.SHA256(), backend=default_backend())
        sha256sum.update(message)
        return sha256sum.finalize()

    def hmac256sum(key, message):
        hmac256sum = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
        hmac256sum.update(message)
        return hmac256sum.finalize()

    def pad_pkcs7_aes128(message):
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        return padder.update(message) + padder.finalize()

    def unpad_pkcs7_aes128(message):
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        return unpadder.update(message) + unpadder.finalize()

    def pbkdf2hmac_derive(salt, password):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=1000,
            backend=default_backend()
        )

        return kdf.derive(password)

    def encrypt(iv, key, pt):
        pt = BadCipher.pad_pkcs7_aes128(pt)
        encryptor = Cipher(
            algorithms.AES(key),
            modes.CBC(iv),
            backend=default_backend()
        ).encryptor()
        return encryptor.update(pt) + encryptor.finalize()

    def decrypt(iv, key, ct):
        decryptor = Cipher(
            algorithms.AES(key),
            modes.CBC(iv),
            backend=default_backend()
        ).decryptor()
        pt = decryptor.update(ct) + decryptor.finalize()
        return BadCipher.unpad_pkcs7_aes128(pt)
