import tkinter


class App:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Mile to Km Converter")
        self.window.minsize(width=240, height=144)
        self.window.config(padx=20, pady=20)

        self.entry_mile = tkinter.Entry(width=8)
        self.entry_mile.grid(column=1, row=0)

        tkinter.Label(text="Miles").grid(column=2, row=0)
        tkinter.Label(text="is equal to").grid(column=0, row=1)

        self.label_km = tkinter.Label(text="0")
        self.label_km.grid(column=1, row=1)

        tkinter.Label(text="Km").grid(column=2, row=1)

        self.button_convert = tkinter.Button(text="Calculate", command=self.convert)
        self.button_convert.grid(column=1, row=2)

    def convert(self):
        mile = float(self.entry_mile.get())
        if mile < 0:
            return

        km = round(1.60934 * mile, 3)

        print(f"mile={mile}\nkm={km}")
        self.label_km.config(text=str(km))

    def start(self):
        self.window.mainloop()


def main():
    app = App()
    app.start()


if __name__ == "__main__":
    main()
