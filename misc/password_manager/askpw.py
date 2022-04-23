import tkinter
import tkinter.simpledialog


class AskPw:
    def ask(title="Vault"):
        root = tkinter.Tk()
        root.withdraw()
        password = tkinter.simpledialog.askstring(title, "Enter password:", show="")
        root.destroy()
        return password
