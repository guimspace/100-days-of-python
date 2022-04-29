import random


class BadPwGenerator:
    def generate(lenngth=19):
        return "".join([chr(32 + n) for n in random.choices(range(94), k=lenngth)])
