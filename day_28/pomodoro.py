WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


class Pomodoro:
    def __init__(self):
        self.WORK_MIN = WORK_MIN
        self.SHORT_BREAK_MIN = SHORT_BREAK_MIN
        self.LONG_BREAK_MIN = LONG_BREAK_MIN

        self.time_left = 0
