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

        self.has_lock = False

        self.window = tkinter.Tk()
        self.window.title("Pomodoro Timer")
        self.window.config(padx=100, pady=50, bg=YELLOW)

        self.tomato_img = tkinter.PhotoImage(file="tomato.png")

        tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW,
                      font=(FONT_NAME, 26, "bold")
                      ).grid(column=1, row=0)

        self.canvas = tkinter.Canvas(width=200, height=224,
                                     bg=YELLOW, highlightthickness=0)
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.text_timer = self.canvas.create_text(100, 130, text="00:00",
                                                  fill="white",
                                                  font=(FONT_NAME, 26, "bold"))
        self.canvas.grid(column=1, row=1)

        tkinter.Button(text="Start", command=self.start_timer).grid(column=0, row=2)
        tkinter.Button(text="Reset").grid(column=2, row=2)

    def launch(self):
        self.window.mainloop()

    def start_timer(self):
        if self.has_lock:
            return

        self.has_lock = True
        self.time_left = 60 * self.WORK_MIN
        self.count_down()

    def count_down(self):
        self.refresh_timer()
        if self.time_left > 0:
            self.time_left -= 1
            self.window.after(1000, self.count_down)

    def refresh_timer(self):
        sec = self.time_left % 60
        min = int((self.time_left - sec) / 60)

        self.canvas.itemconfig(self.text_timer,
                               text=f"{min:02d}:{sec:02d}")
