# Welcome to Calculator GUI 1.0 made 10-7-2018 by Dariush Aligholizadeh

from Tkinter import *
import re

root = Tk()

def change_box(button):
	if button["text"] == "=":
		text['text'] = str(round((eval(text['text'])), 6))
	elif button['text'] == "clear":
		text['text'] = ""
	else:
		text['text'] = text['text'] + button['text']

text = Label(root, text = "", height = 2, width = 16, borderwidth = 2, relief = "sunken")
text.grid(row = 0, column = 0, columnspan = 3)

b1 = Button(root, text = "1", command = lambda:change_box(b1), bg = "black", fg = "gold", width = 2, height = 2)
b1.grid(row = 1, column = 0)

b2 = Button(root, text = "2", command = lambda:change_box(b2), bg = "black", fg = "gold", width = 2, height = 2)
b2.grid(row = 1, column = 1)

b3 = Button(root, text = "3", command = lambda:change_box(b3), bg = "black", fg = "gold", width = 2, height = 2)
b3.grid(row = 1, column = 2)

b4 = Button(root, text = "4", command = lambda:change_box(b4), bg = "black", fg = "gold", width = 2, height = 2)
b4.grid(row = 2, column = 0)

b5 = Button(root, text = "5", command = lambda:change_box(b5), bg = "black", fg = "gold", width = 2, height = 2)
b5.grid(row = 2, column = 1)

b6 = Button(root, text = "6", command = lambda:change_box(b6), bg = "black", fg = "gold", width = 2, height = 2)
b6.grid(row = 2, column = 2)

b7 = Button(root, text = "7", command = lambda:change_box(b7), bg = "black", fg = "gold", width = 2, height = 2)
b7.grid(row = 3, column = 0)

b8 = Button(root, text = "8", command = lambda:change_box(b8), bg = "black", fg = "gold", width = 2, height = 2)
b8.grid(row = 3, column = 1)

b9 = Button(root, text = "9", command = lambda:change_box(b9), bg = "black", fg = "gold", width = 2, height = 2)
b9.grid(row = 3, column = 2)

b10 = Button(root, text = "0", command = lambda:change_box(b10), bg = "black", fg = "gold", width = 2, height = 2)
b10.grid(row = 4, column = 0)

b11 = Button(root, text = ".", command = lambda:change_box(b11), bg = "black", fg = "gold", width = 2, height = 2)
b11.grid(row = 4, column = 1)

b12 = Button(root, text = "+", command = lambda:change_box(b12), bg = "black", fg = "gold", width = 2, height = 2)
b12.grid(row = 4, column = 2)

b13 = Button(root, text = "-", command = lambda:change_box(b13), bg = "black", fg = "gold", width = 2, height = 2)
b13.grid(row = 5, column = 0)

b14 = Button(root, text = "/", command = lambda:change_box(b14), bg = "black", fg = "gold", width = 2, height = 2)
b14.grid(row = 5, column = 1)

b15 = Button(root, text = "*", command = lambda:change_box(b15), bg = "black", fg = "gold", width = 2, height = 2)
b15.grid(row = 5, column = 2)

b16 = Button(root, text = "=", command = lambda:change_box(b16), bg = "black", fg = "gold", width = 2, height = 2)
b16.grid(row = 6, column = 0)

b17 = Button(root, text = "clear", command = lambda:change_box(b17), bg = "black", fg = "gold", width = 8, height = 2)
b17.grid(row = 6, column = 1, columnspan = 2, sticky = W)

root.title("Calculator")

f = Frame(root)

menu = Menu(root)
root.config(menu = menu)
submenu = Menu(menu)
menu.add_cascade(label = "File", menu = submenu)
submenu.add_command(label = "Exit", command = f.quit)

root.mainloop()
