from tkinter import *

root = Tk()
root.title("comics")
root.geometry('450x300')

def update_label():
    comic_info.set("")
    for p in comics:
        comic_info.set(comic_info.get() + p._name + " |  In Stock:  " + str(p._stock) + "\n")



class Comics:
    def __init__(self, name, stock):
        self._name = name   
        self._stock = stock
        comics.append(self)
        comic_names.append(self._name)

comics = []
comic_names = []

Comics("Python Panic", 8)
Comics("Scratch The Cat", 12)
Comics("Tony Tkinter :(", 3)

comic_info = StringVar()

comic_label = Label(root, textvariable=comic_info)
comic_label.grid(row=0, column = 0)


update_label()
root.mainloop()