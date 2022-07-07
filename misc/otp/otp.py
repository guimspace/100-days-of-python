import time

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac

TIME_STEP = 30


class OTP:
    def sha256sum(message):
        sha256sum = hashes.Hash(hashes.SHA256(), backend=default_backend())
        sha256sum.update(message)
        return sha256sum.finalize()

    def hmac256sum(key, message):
        hmac256sum = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
        hmac256sum.update(message)
        return hmac256sum.finalize()

    def hotp(k, c):
        hs = OTP.hmac256sum(k, c)
        ob = hs[-1] & 0xf
        p = ((hs[ob] & 0x7f) << 24 |
             (hs[ob + 1] & 0xff) << 16 |
             (hs[ob + 2] & 0xff) << 8 |
             (hs[ob + 3] & 0xff))
        return p % 10 ** 6

    def totp(k, t):
        return OTP.hotp(k, t)

    def verify(key: bytes, value: bytes):
        t = int(time.time() / TIME_STEP).to_bytes(4, byteorder='big')
        otp = OTP.hotp(key, t).to_bytes(4, byteorder='big')
        return OTP.sha256sum(value) == OTP.sha256sum(otp)
