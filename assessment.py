from tkinter import *

root = Tk()
root.title("comics")
root.geometry('450x300')

def update_label():
    comic_info_name.set("")
    for p in comics:
        comic_info_name.set(comic_info_name.get() + p._name + "\n")
    comic_info_stock.set("")
    for p in comics:
        comic_info_stock.set(comic_info_stock.get() + "  In Stock: " + str(p._stock) + "Comics" + "\n")

def sell_comics():
    print("")

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
Comics("Tony Tkinter", 3)

#Labels - Printing info at top
comic_info_name = StringVar()
comic_info_stock = StringVar()

comic_label_name = Label(root, textvariable=comic_info_name, justify=LEFT)
comic_label_name.grid(row=0, column = 0)

comic_label_stock = Label(root, textvariable=comic_info_stock, justify=LEFT)
comic_label_stock.grid(row=0, column = 1)

#SELLING COMICS
#selecting from list
selected_comic_sell = StringVar()
selected_comic_sell.set(comic_names[0])

#Dropdown
comic_menu = OptionMenu(root, selected_comic_sell, *comic_names)
comic_menu.grid(row=2, column = 0)

num_comics = StringVar()

comic_entry = Entry(root, textvariable=num_comics)
comic_entry.grid(row=2, column = 1)

select_btn = Button(root, text="Select", command=sell_comics)
select_btn.grid(row=3, column = 0)


update_label()
root.mainloop()