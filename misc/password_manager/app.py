from tkinter import *
from tkinter import messagebox

from bad_vault import BadVault
from bad_pw_generator import BadPwGenerator


class App:
    def __init__(self):
        self._root = Tk()
        self._root.withdraw()

        self._entries = {}
        self._buttons = {}
        self._media = {}

        self._vault = BadVault("./plaintext.json")

    def create_frame(self):
        self._media["logo"] = PhotoImage(file="logo.png")

        self._root.title("Bad Password Manager")
        self._root.config(padx=20, pady=20)

        canvas = Canvas(width=200, height=200)
        canvas.create_image(100, 100, image=self._media["logo"])
        canvas.grid(column=0, row=0, columnspan=3)

        Label(text="Name").grid(column=0, row=1)
        self._entries["name"] = Entry(width=26)
        self._entries["name"].grid(column=1, row=1)

        self._buttons["search"] = Button(text="Search", command=self.search_item).grid(column=2, row=1)

        Label(text="Username").grid(column=0, row=2)
        self._entries["username"] = Entry(width=35)
        self._entries["username"].grid(column=1, row=2, columnspan=2)

        Label(text="Password").grid(column=0, row=3)
        self._entries["password"] = Entry(width=21)
        self._entries["password"].grid(column=1, row=3)

        self._buttons["generate"] = Button(text="Generate", command=self.generate_pw).grid(column=2, row=3)
        self._buttons["add"] = Button(text="Add", width=32, command=self.add_item).grid(column=1, row=4, columnspan=2)

        self._root.deiconify()

    def launch(self):
        self._vault.open_vault()
        self.create_frame()
        self._entries["name"].focus()
        self._root.mainloop()

    def add_item(self):
        item = {}
        for key in self._entries:
            item[key] = str(self._entries[key].get())
            if len(item[key]) == 0:
                self._entries[key].focus()
                messagebox.showinfo(title="Can't Add Item",
                                    message="Please complete all the fields.")
                return

        self._vault.add_item(item)
        self.clear_entries()

    def search_item(self):
        name = str(self._entries["name"].get())
        if len(name) == 0:
            self._entries["name"].focus()
            messagebox.showinfo(title="Can't Search Item",
                                message="Please enter a name.")
            return

        item = self._vault.get_item(name)
        if item is None:
            messagebox.showinfo(title="Item Not Found",
                                message="Could not find this item.")
            return

        self._entries["username"].delete(0, END)
        self._entries["username"].insert(0, item["username"])

        self._entries["password"].delete(0, END)
        self._entries["password"].insert(0, item["password"])

    def clear_entries(self):
        for key in self._entries:
            self._entries[key].delete(0, END)

    def generate_pw(self):
        pw = BadPwGenerator.generate()
        self._entries["password"].delete(0, END)
        self._entries["password"].insert(0, pw)
