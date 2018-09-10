from tkinter import *
from tkinter import messagebox
#-------------------------------------------------------------------------------
#FUNCTIONS & OBJECT ORIENTATION
def update_label():
#setting each label to blank (""), after which we "refresh" the comic labels and in
#turn overlay them where the old labels were, they are then updated to the new values
#from the functions.
    comic_info_name.set("")
    for p in comics:
        comic_info_name.set(comic_info_name.get() + p._name +  "\n")
    comic_info_stock.set("")
    for p in comics:
        comic_info_stock.set(comic_info_stock.get() + "  In Stock: " + str(p._stock) + " Comics" + "\n")
    comic_info_sold.set("")
    for p in comics:
        comic_info_sold.set(comic_info_sold.get() + "  Comics Sold: " + str(p._sold) + "\n")
        
def update_menu():
#setting each option menu to blank (""), after which we "refresh" the option menus and in
#turn overlay them where the old menus were, they are then updated to the new values from 
#the functions. in order to do this we need to make the menus global.
    global sell_menu
    global restock_menu
    global del_menu
    
    if comics == []:
        selected_comic_stock.set("No Items")
        selected_comic_sell.set("No Items")
        del_name.set("No Items")
        
    else:
        #set variables to the first in menu
        selected_comic_stock.set(comic_names[0])
        selected_comic_sell.set(comic_names[0])
        del_name.set(comic_names[0])
        
        #refreshing dropdown menu for selling items
        sell_menu.grid_forget()
        sell_menu = OptionMenu(root, selected_comic_sell, *comic_names)
        sell_menu.grid(row=2, column = 0)

        #refreshing dropdown menu for restocking items
        restock_menu.grid_forget()
        restock_menu = OptionMenu(root, selected_comic_stock, *comic_names)
        restock_menu.grid(row=2, column = 2)


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
#The function sell_comic() is used to sell the amount of a comic. First we loop through the comics.
#after a comic in the loop is equal to the name of the comic selected, we sell the comic.
#If the input is negitive, or invalid, we show error messages, to correct the user.
    for c in comics:
        try:
            message_stock.set("")
            message_add.set("")
            message_del.set("")
            if c._name == selected_comic_sell.get():
                if int(num_comics_sell.get()) >= 1 and int(num_comics_sell.get()) <= c._stock:
                    c.sell(int(num_comics_sell.get()))
                    message_sell.set("You sold {} Comics".format(int(num_comics_sell.get())))

                elif int(num_comics_sell.get()) <= 0:
                    message_sell.set("Please enter an intiger above 1")

                elif int(num_comics_sell.get()) > c._stock:
                    message_sell.set("You can not sell more than your stock")

        except ValueError:
            message_sell.set("please enter an intiger")

def stock_comic():
#The function restock_comic() is used to restock the amount of a comic. First we loop through the comics.
#after a comic in the loop is equal to the name entered, we restock the comic based on the user's input.
#If the input is not between 1 and 20, we create error messages representing what the user did wrong.
    for c in comics:
        try:
            message_sell.set("")
            message_add.set("")
            message_del.set("")
            if c._name == selected_comic_stock.get():
                if int(num_comics_stock.get()) >= 1 and (int(num_comics_stock.get()) + c._stock) <= 20:
                    c.restock(int(num_comics_stock.get()))
                    message_stock.set("You stocked {} {} comics".format(int(num_comics_stock.get()), c._name))
                elif int(num_comics_stock.get()) < 1:
                    message_stock.set("Please enter a positive intiger")

                elif (int(num_comics_stock.get()) + c._stock) > 20:
                    message_stock.set("You can only have maximum 20 comics")

        except ValueError:
            message2.set("Please enter an integer")

def new_comic():
#this function is used to add a new comic to the lists of comics. If the values
#of the names and the comic amount are accepted, add the new comic to the class 
#(Comics class), otherwise show error message to display to the user what is wrong
        try:
            message_sell.set("")
            message_stock.set("")
            message_del.set("")
            title = add_title.get()
            if add_title.get() == '':
                message_add.set("Please enter the comic title")
            elif int(add_stock.get()) < 1:
                message_add.set("Please enter a value greater than 1")
            elif int(add_stock.get()) > 20:
                message_add.set("you can only stock 20 comics")
            elif title.strip() == "":
                message_add.set("dont enter blank spaces")
            elif title.lower().strip() in comic_names:
                message_add.set("dont try to break me with duplicates")
            else:
                Comics(title.strip(), int(add_stock.get()), 0)
                update_label()
                message_add.set("")
                update_menu()
        except ValueError:
            message_add.set("Please type in an integer")

def delete_comic():
#this function is used to delete a selected comic to the lists of comics. If the values
#of the names are accepted, delete the new comic and display a confirm window to let user
#make a final descision.
    if messagebox.askyesno("Delete this Comic?", "Do you wish to delete this comic? "):
        for c in comics:
            try:
                message_sell.set("")
                message_stock.set("")
                message_add.set("")
                if del_name.get() == c._name:
                    comics.remove(c)
                    comic_names.remove(c._name)
                    update_label()
                    update_menu()
                    
            except ValueError:
                message_del.set("enter a valid input")


#END OF FUNCTIONS
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#OBJECT ORIENTATION
class Comics:
#class storing all information on stock details
    def __init__(self, name, stock, sold):
        self._name = name.lower()
        self._stock = stock
        self._sold = sold
        comics.append(self)
        comic_names.append(self._name)
        
    def sell(self, qty):
        self._stock -= qty
        self._sold += qty
        update_label()
        
    def restock(self, qty):
        self._stock += qty
        update_label()
        
        
comics = []
comic_names = []

Comics("Python Panic", 8, 0)
Comics("Scrath the Cat", 12, 0)
Comics("Tony Tkinter", 3, 0)


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
comic_info_sold = StringVar()

comic_label_name = Label(root, textvariable=comic_info_name, justify=LEFT)
comic_label_name.grid(row=13, column = 0)

comic_label_stock = Label(root, textvariable=comic_info_stock, justify=LEFT)
comic_label_stock.grid(row=13, column = 1)

comic_label_sold = Label(root, textvariable=comic_info_sold, justify=LEFT)
comic_label_sold.grid(row=13, column = 2)
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
message_sell = StringVar()
message_sell.set("")

#selling Comic error
error_message_sell = Label(root, textvariable=message_sell, fg="red")
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

message_stock = StringVar()
message_stock.set("")

restock_error = Label(root, textvariable=message_stock, fg="red")
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

message_add = StringVar()
message_add.set("")

add_error = Label(root, textvariable=message_add , fg="red")
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

message_del = StringVar()
message_del.set("")

del_error = Label(root, textvariable=message_del , fg="red")
del_error.grid(row= 10 , column = 0)
#END OF DELETE COMICS
#-------------------------------------------------------------------------------
update_label()
root.mainloop()


