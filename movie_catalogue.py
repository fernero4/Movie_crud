import tkinter as tk
from client.gui_app import *


def main():
    root = tk.Tk()
    root.title("Movie's Catalogue")
    root.resizable(False, False)
    menu_bar(root)

    app = Frame(root=root)
    root.mainloop()


if __name__ == '__main__':
    main()
