from tkinter import *


class App:
    def __init__(self):
        self._root = Tk()
        self._entries = {}
        self._buttons = {}
        self._media = {}

        self._media["logo"] = PhotoImage(file="logo.png")

        self._root.title("Bad Password Manager")
        self._root.config(padx=20, pady=20)

        canvas = Canvas(width=200, height=200)
        canvas.create_image(100, 100, image=self._media["logo"])
        canvas.grid(column=0, row=0, columnspan=3)

        Label(text="Name").grid(column=0, row=1)
        self._entries["name"] = Entry(width=35)
        self._entries["name"].grid(column=1, row=1, columnspan=2)

        Label(text="Username").grid(column=0, row=2)
        self._entries["username"] = Entry(width=35)
        self._entries["username"].grid(column=1, row=2, columnspan=2)

        Label(text="Password").grid(column=0, row=3)
        self._entries["password"] = Entry(width=21)
        self._entries["password"].grid(column=1, row=3)

        self._buttons["generate"] = Button(text="Generate").grid(column=2, row=3)
        self._buttons["add"] = Button(text="Add", width=32).grid(column=1, row=4, columnspan=2)

    def launch(self):
        self._entries["name"].focus()
        self._root.mainloop()
