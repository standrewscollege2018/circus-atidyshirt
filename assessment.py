from tkinter import *
#-------------------------------------------------------------------------------
#FUNCTIONS & OBJECT ORIENTATION
def update_label():
    comic_info.set("")
    for p in comics:
        comic_info.set(comic_info.get() + p._name + "    Comics Available:   " + str(p._amount) + "    Comics Sold:   " + str(p._sold) + "\n")

def update_menu():
    #letting menus be called within the function
    global sell_menu
    global restock_menu
    global del_menu

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
    
def restock_comic_placeholder(event):
    num_comics_stock.set("")
    
def update_label():
    comic_info_name.set("")
    for p in comics:
        comic_info_name.set(comic_info_name.get() + p._name + "\n")
    comic_info_stock.set("")
    for p in comics:
        comic_info_stock.set(comic_info_stock.get() + "  In Stock: " + str(p._stock) + " Comics" + "\n")

def sell_comics():
    for c in comics:
        try:
            if selected_comic_sell.get() == c._name:
                if int(num_comics_sell.get()) >= 1 and int(num_comics_sell.get()) <= c._stock:
                    c._stock -= int(num_comics_sell.get())
                    message.set("You sold {} Comics".format(int(num_comics_sell.get())))

                elif int(num_comics_sell.get()) <= 0:
                    message.set("Please enter a positive intiger")

                elif int(num_comics_sell.get()) > c._stock:
                    message.set("Please enter a value that is valid")

        except ValueError:
            message.set("Please enter an integer value")

    update_label()

def stock_comics():
    for c in comics:
        try:
            if selected_comic_stock.get() == c._name:
                if int(num_comics_stock.get()) >= 1 and int(num_comics_stock.get()) <= 99999:
                    c._stock += int(num_comics_stock.get())
                    message2.set("You re-stocked {} Comics".format(int(num_comics_stock.get())))

                elif int(num_comics_stock.get()) <= 0:
                    message2.set("Please enter a positive intiger")

        except ValueError:
            message2.set("Please enter an integer value")

    update_label()
    
def new_comic():
    try:
        if add_title.get() == '':
            message3.set("Please enter a title for the comic")
        elif int(add_stock.get()) <= 0:
            message3.set("Please enter a positive intiger")
        else:
            Comics(add_title.get(), int(add_stock.get()))
            update_label()
            message3.set("")
            update_menu()
            
    except ValueError:
        message3.set("Please type in an integer value")
        message3.set("Please type in an integer value")

def del_comic():
    for i in comics:
        if del_name.get() == i._name:
            comics.remove(i)
            comic_names.remove(i._name)
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


root = Tk()
root.title("comics")
root.geometry('560x400')

#arrays storing all info and names
comics = []
comic_names = []

Comics("Python Panic", 8)
Comics("Scratch The Cat", 12)
Comics("Tony Tkinter", 3)
#END OF FUNCTIONS & OBJECT ORIENTATION
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

comic_entry = Entry(root, textvariable=num_comics_sell, justify=LEFT)
comic_entry.grid(row=3, column = 0)
comic_entry.bind("<Button-1>", sell_comic_placeholder)

sell_btn = Button(root, text="Sell Comics", command=sell_comics, justify=RIGHT)
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
stock_items = Label(root, text = "Restock Comic(s)", justify=LEFT)
stock_items.grid(row=0, column = 2)

#string
selected_comic_stock = StringVar()
selected_comic_stock.set(comic_names[0])

#Dropdown
restock_menu = OptionMenu(root, selected_comic_stock, *comic_names)
restock_menu.grid(row=2, column = 2)

#string
num_comics_stock = StringVar()
num_comics_stock.set("Quantity: ")

#creating entry field
comic_entry_stock = Entry(root, textvariable=num_comics_stock, justify=LEFT)
comic_entry_stock.grid(row=3, column = 2)
comic_entry_stock.bind("<Button-1>", restock_comic_placeholder)

#select button to push the command
select_btn_stock = Button(root, text="Stock comics", command=stock_comics, justify=RIGHT)
select_btn_stock.grid(row=4, column = 2)

#message re-direct
message2 = StringVar()
message2.set("")

#restock Comic error
error_message_stock = Label(root, textvariable=message2, fg="red")
error_message_stock.grid(row=5, column = 2)
#END OF RE-STOCK PANEL
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#ADDING NEW COMICS
#label
add_comic = Label(root, text="Add New Comic(s)")
add_comic.grid(row = 6, columnspan = 1)

#setting to string variable
add_title = StringVar()
add_title.set("Title: ")

#entry field for name
comic_add_enter = Entry(root, textvariable=add_title)
comic_add_enter.grid(row = 7, column = 0)
comic_add_enter.bind("<Button-1>", comic_add_placeholder)

#setting string variable
add_stock = StringVar()
add_stock.set("Quantity: ")

#entry field for quantity
stock_enter = Entry(root, textvariable=add_stock)
stock_enter.grid(row = 8, column = 0)
stock_enter.bind("<Button-1>", comic_add_stock_placeholder)

#submit button
add_button = Button(root, text="Add Comic", command=new_comic)
add_button.grid(row = 9, columnspan = 1)

#error checking
message3 = StringVar()
message3.set("")

add_error = Label(root, textvariable=message3, fg="red")
add_error.grid(row= 10 , columnspan = 1)
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

#creating dropdown menu
del_menu = OptionMenu(root, del_name, *comic_names)
del_menu.grid(row = 7, column = 2)

#delete button (pushing the command (function))
del_button = Button(root, text="Delete comic", command=del_comic)
del_button.grid(row = 8, column = 2)
#END OF DELETE COMICS
#-------------------------------------------------------------------------------

update_label()
root.mainloop()