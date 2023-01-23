

from tkinter import *
from tokenize import Name

color_bg = "White"
color_fg = "Black"
Menu_bg = "Black"

MainWindow = Tk()
MainWindow.geometry("350x200")
MainWindow.title("Simple Sticky Notes")
MainWindow.wm_resizable(False, False)


def Change_appearance(color_bg, color_fg):
    NotesArea['bg'] = color_bg
    NotesArea['fg'] = color_fg


def White_on_black():
    global Menu_bg
    color_bg = "Black"
    color_fg = "White"
    Menubar['bg'] = Menu_bg
    NotesArea.configure(insertbackground="White")
    Change_appearance(color_bg, color_fg)


def Default():
    global color_bg, color_fg, Menu_bg
    Menubar['bg'] = Menu_bg
    Change_appearance(color_bg, color_fg)


def Black_on_orange():
    color_bg = "Orange"
    color_fg = "Black"
    Menubar['bg'] = "Green"
    Change_appearance(color_bg, color_fg)


def Change_color(name, textcolor):
    NotesArea.tag_configure(f"{Name}", foredround=textcolor)
    try:
        NotesArea.tag_add(f"{Name}", "sel.first", "sel.last")
    except Exception as e:
        pass


def Color_green():
    Name = "green_color"
    text_color = "Green"
    Change_color(Name, text_color)


def Color_Red():
    Name = "Red_color"
    text_color = Color_Red
    Change_color(Name, text_color)


def Color_blue():
    Name = "Blue_color"
    text_color = Color_blue
    Change_color(Name, text_color)


Menubar = Menu(MainWindow, bg=Menu_bg)
Appearance = Menu(Menubar, tearoff=0)
Menubar.add_cascade(label="Appearance", menu=Appearance)
Appearance.add_command(label="White on black", command=White_on_black)
Appearance.add_command(label="Default", command=Default)
Appearance.add_command(label="Black on orange", command=Black_on_orange)

Text_color = Menu(Menubar, tearoff=0)
Text_color.add_cascade(label="Text Color", menu=Text_color)
Text_color.add_command(label="Green", command=Color_green)
Text_color.add_command(label="Red", command=Color_Red)
Text_color.add_command(label="Blue", command=Color_blue)

MainWindow.config(menu=Menubar)

NotesArea = Text(MainWindow, bg=color_bg, fg=color_fg, font='Ubuntu 15 bold')
NotesArea.pack(fill=BOTH)


MainWindow.mainloop()


'''
import tkinter as tk


def cli():
    import time
    current_time = time.strftime("%H:%M")
    print("Welcome to Noty.You can now create sticky notes, easily.")
    time.sleep(2)
    note_input = input("Type your notes here: ")
    note = ("%s") % note_input
    time.sleep(1)
    root = tk.Tk()
    root.geometry("600x600")
    tk.Label(root, text=current_time).pack()
    tk.Label(root, text=note).pack()
    root.mainloop()


cli()
'''
