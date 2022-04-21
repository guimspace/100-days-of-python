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

        self.window = tkinter.Tk()
        self.window.title("Pomodoro Timer")
        self.window.config(padx=100, pady=50, bg=YELLOW)

        self.tomato_img = tkinter.PhotoImage(file="tomato.png")

        tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW,
                      font=(FONT_NAME, 26, "bold")
                      ).grid(column=1, row=0)

        canvas = tkinter.Canvas(width=200, height=224,
                                bg=YELLOW, highlightthickness=0)
        canvas.create_image(100, 112, image=self.tomato_img)
        canvas.create_text(100, 130, text="00:00",
                           fill="white", font=(FONT_NAME, 26, "bold"))
        canvas.grid(column=1, row=1)

        tkinter.Button(text="Start").grid(column=0, row=2)
        tkinter.Button(text="Reset").grid(column=2, row=2)

    def launch(self):
        self.window.mainloop()
