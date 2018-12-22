import tkinter
from tkinter import messagebox


def show_info(msg):
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo('info', msg)
