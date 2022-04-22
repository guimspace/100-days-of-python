from tkinter import *


def main():
    root = Tk()
    img_logo = PhotoImage(file="logo.png")

    root.title("Bad Password Manager")
    root.config(padx=20, pady=20)

    canvas = Canvas(width=200, height=200)
    canvas.create_image(100, 100, image=img_logo)
    canvas.grid(column=0, row=0, columnspan=3)

    Label(text="Name").grid(column=0, row=1)
    entry_name = Entry(width=35)
    entry_name.grid(column=1, row=1, columnspan=2)

    Label(text="Username").grid(column=0, row=2)
    entry_username = Entry(width=35)
    entry_username.grid(column=1, row=2, columnspan=2)

    Label(text="Password").grid(column=0, row=3)
    entry_password = Entry(width=21)
    entry_password.grid(column=1, row=3)
    Button(text="Generate").grid(column=2, row=3)

    Button(text="Add", width=32).grid(column=1, row=4, columnspan=2)

    root.mainloop()


if __name__ == "__main__":
    main()
