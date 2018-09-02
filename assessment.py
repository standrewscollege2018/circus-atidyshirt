from tkinter import *
#-------------------------------------------------------------------------------
#FUNCTIONS & OBJECT ORIENTATION
def update_label():
    comic_info_name.set("")
    for p in comics:
        comic_info_name.set(comic_info_name.get() + p._name + "\n")
    comic_info_stock.set("")
    for p in comics:
        comic_info_stock.set(comic_info_stock.get() + "  In Stock: " + str(p._stock) + " Comics" + "\n")
        
def update_menu():
    global sell_menu
    global restock_menu
    global del_menu

    selected_comic_sell.set(comic_names[0])
    #refreshing dropdown menu for selling items
    sell_menu.grid_forget()
    sell_menu = OptionMenu(root, selected_comic_sell, *comic_names)
    sell_menu.grid(row=2, column = 0)

    selected_comic_stock.set(comic_names[0])
    #refreshing dropdown menu for restocking items
    restock_menu.grid_forget()
    restock_menu = OptionMenu(root, selected_comic_stock, *comic_names)
    restock_menu.grid(row=2, column = 2)


    del_name.set(comic_names[0])
    #refreshing dropdown menu for deleting items
    del_menu.grid_forget()
    del_menu = OptionMenu(root, del_name, *comic_names)
    del_menu.grid(row = 7, column = 2)

#placeholder functions are used to display pre-fills in all entry fields
def comic_add_placeholder(event):
    add_title.set("")

def comic_add_stock_placeholder(event):
    add_stock.set("")

def sell_comic_placeholder(event):
    num_comics_sell.set("")

def stock_comic_placeholder(event):
    num_comics_stock.set("")

def sell_comics():
    for c in comics:
        try:
            if selected_comic_sell.get() == c._name:
                if int(num_comics_sell.get()) >= 1 and int(num_comics_sell.get()) <= c._stock:
                    c._stock -= int(num_comics_sell.get())
                    message.set("You sold {} Comics".format(int(num_comics_sell.get())))

                elif int(num_comics_sell.get()) <= 0:
                    message.set("Please enter an intiger above 1")

                elif int(num_comics_sell.get()) > c._stock:
                    message.set("You can not sell more than your stock")

        except ValueError:
            message.set("please enter an intiger")

    update_label()

def stock_comic():
    for c in comics:
        try:
            if selected_comic_stock.get() == c._name:
                if int(num_comics_stock.get()) >= 1 and (int(num_comics_stock.get()) + c._stock) <= 20:
                    c.restock(int(num_comics_stock.get()))
                    message2.set("You stocked {} {} comics".format(int(num_comics_stock.get()), c._name))

                elif int(num_comics_stock.get()) < 1:
                    message2.set("Please enter a positive intiger")

                elif (int(num_comics_stock.get()) + c._stock) > 20:
                    message2.set("You can only have maximum 20 comics")

        except ValueError:
            message2.set("Please enter an integer")

    update_label()

def new_comic():
    try:
        if add_title.get() == '':
            message3.set("Please enter the comic title")
        elif int(add_stock.get()) < 1:
            message3.set("Please enter a value greater than 1")
        elif int(add_stock.get()) > 20:
            message3.set("you can only stock 20 comics")
        else:
            Comics(add_title.get(), int(add_stock.get()))
            update_label()
            message3.set("")
            update_menu()
    except ValueError:
        message3.set("Please type in an integer")

def delete_comic():
    for c in comics:
        if del_name.get() == c._name:
            comics.remove(c)
            comic_names.remove(c._name)
            update_label()
            update_menu()


#END OF FUNCTIONS
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#OBJECT ORIENTATION

class Comics:
    def __init__(self, name, stock):
        self._name = name
        self._stock = stock
        comics.append(self)
        comic_names.append(self._name)

    def restock(self, stock):
        self._stock += stock

    def sell_comic(self, stock):
        self._stock -= stock

    def sell_number(self, stock):
        self._sold += stock




comics = []
comic_names = []

Comics("Python Panic", 8)
Comics("Scrath the Cat", 12)
Comics("Tony Tkinter", 3)


root = Tk()
root.title("comics label")
root.geometry('800x1000')
#END OF OBJECT ORIENTATION
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#INFO PANEL
info_label = Label(root, text="Comics In stock", justify=LEFT)
info_label.grid(row = 12, column = 0)

comic_info_name = StringVar()
comic_info_stock = StringVar()

comic_label_name = Label(root, textvariable=comic_info_name, justify=LEFT)
comic_label_name.grid(row=13, column = 0)

comic_label_stock = Label(root, textvariable=comic_info_stock, justify=LEFT)
comic_label_stock.grid(row=13, column = 1)
#END OF INFO PANEL
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#SELLING PANEL
#Heading
sell_items = Label(root, text = "Sell Comic(s)", justify=LEFT)
sell_items.grid(row=0, column = 0)

#selecting from list
selected_comic_sell = StringVar()
selected_comic_sell.set(comic_names[0])

#Dropdown
sell_menu = OptionMenu(root, selected_comic_sell, *comic_names)
sell_menu.grid(row=2, column = 0)

num_comics_sell = StringVar()
num_comics_sell.set("Quantity: ")

comic_entry = Entry(root, textvariable=num_comics_sell)
comic_entry.grid(row=3, column = 0)
comic_entry.bind("<Button-1>", sell_comic_placeholder)

sell_btn = Button(root, text="Sell", command=sell_comics, justify=RIGHT)
sell_btn.grid(row=4, column = 0)

#message re-direct
message = StringVar()
message.set("")

#selling Comic error
error_message_sell = Label(root, textvariable=message, fg="red")
error_message_sell.grid(row=5, column = 0)
#END OF SELLING PANEL
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#RE-STOCK PANEL
#Heading
stock_items = Label(root, text="Restock Comic(s)")
stock_items.grid(row = 0, column = 2)

selected_comic_stock = StringVar()
selected_comic_stock.set(comic_names[0])

restock_menu = OptionMenu(root, selected_comic_stock, *comic_names)
restock_menu.grid(row = 2, column = 2)

num_comics_stock = StringVar()
num_comics_stock.set("Quantity: ")

comic_entry_stock = Entry(root, textvariable=num_comics_stock)
comic_entry_stock.grid(row = 3, column = 2)
comic_entry_stock.bind("<Button-1>", stock_comic_placeholder)

restock_btn = Button(root, text="Restock", command=stock_comic)
restock_btn.grid(row = 4, column = 2)

message2 = StringVar()
message2.set("")

restock_error = Label(root, textvariable=message2, fg="red")
restock_error.grid(row= 5 , column = 2)

#END OF RE-STOCK PANEL
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#ADDING NEW COMICS
add_comic = Label(root, text="Adding Comic(s)")
add_comic.grid(row = 6, column = 0)

add_title = StringVar()
add_title.set("Title: ")

add_enter = Entry(root, textvariable=add_title)
add_enter.grid(row = 7, column = 0)
add_enter.bind("<Button-1>", comic_add_placeholder)

add_stock = StringVar()
add_stock.set("Quantity: ")

stock_enter = Entry(root, textvariable=add_stock)
stock_enter.grid(row = 8, column = 0)
stock_enter.bind("<Button-1>", comic_add_stock_placeholder)

add_button = Button(root, text="Add", command=new_comic)
add_button.grid(row = 9, column = 0)

message3 = StringVar()
message3.set("")

add_error = Label(root, textvariable=message3, fg="red")
add_error.grid(row= 10 , column = 0)
#END OF ADDING NEW COMICS
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#DELETE COMICS
#label
del_comic = Label(root, text="Delete Comic(s)")
del_comic.grid(row = 6, column = 2)

#setting as string
del_name = StringVar()
del_name.set(comic_names[0])

del_menu = OptionMenu(root, del_name, *comic_names)
del_menu.grid(row = 7, column = 2)

del_button = Button(root, text="Delete", command=delete_comic)
del_button.grid(row = 8, column = 2)
#END OF DELETE COMICS
#-------------------------------------------------------------------------------
update_label()
root.mainloop()
