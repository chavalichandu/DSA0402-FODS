from tkinter import *

root = Tk()
root.title("Basic Graph")

canvas = Canvas(root, width=400, height=300, bg="white")
canvas.pack()

canvas.create_line(50, 250, 100, 180, fill="blue", width=2)
canvas.create_line(100, 180, 150, 200, fill="blue", width=2)
canvas.create_line(150, 200, 200, 120, fill="blue", width=2)
canvas.create_line(200, 120, 250, 80, fill="blue", width=2)

canvas.create_rectangle(280, 200, 310, 250, fill="red")
canvas.create_rectangle(320, 150, 350, 250, fill="green")
canvas.create_rectangle(360, 100, 390, 250, fill="orange")

root.mainloop()
