from Tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()

blackline = canvas.create_line(0, 0, 300, 300)
redline = canvas.create_line(0, 300, 300, 0,fill="purple")
greenbox = canvas.create_rectangle(150, 150, 300, 300,fill="red")


root.mainloop()