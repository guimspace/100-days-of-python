from base64 import b64encode, b64decode
from random import choices

from cryptography.exceptions import AlreadyFinalized
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

POOL = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255)


class BadCrypto:
    def randbytes(num):
        return bytes(choices(POOL, k=num))

    def verify_sha(m1, m2):
        sha256sum = hashes.Hash(hashes.SHA256(), backend=default_backend())
        sha256sum.update(m1)
        tag1 = sha256sum.finalize()

        sha256sum = hashes.Hash(hashes.SHA256(), backend=default_backend())
        sha256sum.update(m2)
        tag2 = sha256sum.finalize()

        if tag1 != tag2:
            raise ValueError("BadCrypto: sha doesn't match")

    def decrypt(password, data):
        data = b64decode(bytearray(data, "utf-8"))

        salt = data[:16]
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=1000,
            backend=default_backend()
        )

        key = kdf.derive(bytes(password, "utf-8"))

        sha256sum = hashes.Hash(hashes.SHA256(), backend=default_backend())
        sha256sum.update(key)
        subkeys = sha256sum.finalize()

        hmac256sum = hmac.HMAC(subkeys[16:], hashes.SHA256(), backend=default_backend())

        hmac256sum.update(data[16:-32])
        tag = hmac256sum.finalize()

        BadCrypto.verify_sha(tag, data[-32:])

        iv = data[16:32]
        decryptor = Cipher(
            algorithms.AES(subkeys[:16]),
            modes.CBC(iv),
            backend=default_backend()
        ).decryptor()

        ct = data[32:-32]

        pt = decryptor.update(ct) + decryptor.finalize()

        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        pt = unpadder.update(pt) + unpadder.finalize()

        return pt.decode("utf-8")

    def encrypt(password, data):
        salt = BadCrypto.randbytes(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=1000,
            backend=default_backend()
        )

        key = kdf.derive(bytes(password, "utf-8"))

        sha256sum = hashes.Hash(hashes.SHA256(), backend=default_backend())
        sha256sum.update(key)
        subkeys = sha256sum.finalize()

        iv = BadCrypto.randbytes(16)
        encryptor = Cipher(
            algorithms.AES(subkeys[:16]),
            modes.CBC(iv),
            backend=default_backend()
        ).encryptor()

        pt = bytes(data, "utf-8")

        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        pt = padder.update(pt)
        pt += padder.finalize()

        ct = encryptor.update(pt)
        ct += encryptor.finalize()

        hmac256sum = hmac.HMAC(subkeys[16:], hashes.SHA256(), backend=default_backend())

        hmac256sum.update(iv + ct)
        tag = hmac256sum.finalize()

        return b64encode(salt + iv + ct + tag).decode("utf-8")
