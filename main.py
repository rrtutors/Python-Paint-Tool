from tkinter import *
root = Tk()
root.title("Python Paint Tool")
root.geometry("500x350")
def paint(event):
    x1, y1 = (event.x-3), (event.y-3)
    x2, y2 = (event.x+3), (event.y+3)
    color = "black"
    wn.create_oval(x1, y1, x2, y2, fill=color, outline=color)
wn=Canvas(root, width=500, height=350, bg='white')
wn.bind('<B1-Motion>', paint)
wn.pack()
root.mainloop()