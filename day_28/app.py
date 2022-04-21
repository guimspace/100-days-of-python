import tkinter

from pomodoro import Pomodoro

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


class App(Pomodoro):
    def __init__(self):
        super().__init__()

        self.job = None
        self.after_id = None

        self.window = tkinter.Tk()
        self.window.title("Pomodoro Timer")
        self.window.config(padx=100, pady=50, bg=YELLOW)

        self.tomato_img = tkinter.PhotoImage(file="tomato.png")

        self.header = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW,
                                    font=(FONT_NAME, 26, "bold"))
        self.header.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(width=200, height=224,
                                     bg=YELLOW, highlightthickness=0)
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.text_timer = self.canvas.create_text(100, 130, text="00:00",
                                                  fill="white",
                                                  font=(FONT_NAME, 26, "bold"))
        self.canvas.grid(column=1, row=1)

        self.button_main = tkinter.Button(text="Start", width=8, command=self.process_job)
        self.button_main.grid(column=0, row=2)

        tkinter.Button(text="Reset").grid(column=2, row=2)

    def launch(self):
        self.window.mainloop()

    def process_job(self):
        if self.job is None:
            self.job = "work"
            self.header.config(text="Work", fg=GREEN)
            self.button_main.config(text="Pause", width=8, command=self.pause_job)
            self.start_timer(self.WORK_MIN)

        elif self.job == "work":
            self.job = "short-break"
            self.button_main.config(text="Skip", width=8, command=self.process_job)
            self.header.config(text="Break", fg=PINK)
            self.start_timer(self.SHORT_BREAK_MIN)

        elif self.job == "short-break":
            self.job = None
            self.header.config(text="Timer", fg=GREEN)
            self.button_main.config(text="Start", width=8, command=self.process_job)
            if self.after_id is not None:
                self.window.after_cancel(self.after_id)
                self.time_left = 0
                self.refresh_timer()

    def start_timer(self, time):
        self.time_left = 60 * time
        self.count_down()

    def pause_job(self):
        self.window.after_cancel(self.after_id)
        self.after_id = None
        self.button_main.config(text="Continue", width=8, command=self.continue_job)

    def continue_job(self):
        self.button_main.config(text="Pause", width=8, command=self.pause_job)
        self.count_down()

    def count_down(self):
        self.refresh_timer()
        if self.time_left > 0:
            self.time_left -= 1
            self.after_id = self.window.after(1000, self.count_down)
        else:
            self.after_id = None
            self.process_job()

    def refresh_timer(self):
        sec = self.time_left % 60
        min = int((self.time_left - sec) / 60)

        self.canvas.itemconfig(self.text_timer,
                               text=f"{min:02d}:{sec:02d}")
