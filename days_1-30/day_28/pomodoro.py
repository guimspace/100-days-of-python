WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
NUM_SESSIONS = 4


class Pomodoro:
    def __init__(self):
        self.WORK_MIN = WORK_MIN
        self.SHORT_BREAK_MIN = SHORT_BREAK_MIN
        self.LONG_BREAK_MIN = LONG_BREAK_MIN
        self.NUM_SESSIONS = NUM_SESSIONS

        self.time_left = 0
        self.this_session = 0
