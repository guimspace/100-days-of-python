from tkinter import *
from tkinter import messagebox

from bad_db import BadDb


class App:
    def __init__(self):
        self._root = Tk()
        self._entries = {}
        self._buttons = {}
        self._media = {}

        self._db = BadDb("./plaintext.csv")

    def create_frame(self):
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
        self._buttons["add"] = Button(text="Add", width=32, command=self.add_item).grid(column=1, row=4, columnspan=2)

    def launch(self):
        self.create_frame()
        self._entries["name"].focus()
        self._root.mainloop()

    def add_item(self):
        item = {}
        for key in self._entries:
            item[key] = str(self._entries[key].get())
            if len(item[key]) == 0:
                self._entries[key].focus()
                messagebox.showinfo(title="Can't add item",
                                    message="Please complete all the fields.")
                return

        self._db.append_item(item)
        self.clear_entries()

    def clear_entries(self):
        for key in self._entries:
            self._entries[key].delete(0, END)
