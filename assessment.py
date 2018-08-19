from tkinter import *
#-------------------------------------------------------------------------------
#FUNCTIONS
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
                    message.set("You re-stocked {} Comics".format(int(num_comics_stock.get())))

                elif int(num_comics_stock.get()) <= 0:
                    message.set("Please enter a positive intiger")

        except ValueError:
            message.set("Please enter an integer value")

    update_label()
    
def new_comic():
    try:
        if add_title.get() == '':
            message.set("Please enter a title for the comic")
        elif int(add_stock.get()) <= 0:
            message.set("Please enter a value that is larger than 0")
        else:
            Comics(add_title.get(), int(add_stock.get()))
            update_label()
            message.set("")
            #adding new comic to dropdowns
            comic_menu = OptionMenu(root, selected_comic_sell, *comic_names)
            comic_menu.grid(row=3, column = 0)
            comic_menu = OptionMenu(root, selected_comic_stock, *comic_names)
            comic_menu.grid(row=3, column = 2)
            
    except ValueError:
        message.set("Please type in an integer value")

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
root.geometry('800x800')

#arrays storing all info and names
comics = []
comic_names = []

Comics("Python Panic", 8)
Comics("Scratch The Cat", 12)
Comics("Tony Tkinter", 3)
#END OF OBJECT ORIENTATION
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#INFO PANEL
comic_info_name = StringVar()
comic_info_stock = StringVar()

comic_label_name = Label(root, textvariable=comic_info_name, justify=LEFT)
comic_label_name.grid(row=0, column = 0)

comic_label_stock = Label(root, textvariable=comic_info_stock, justify=LEFT)
comic_label_stock.grid(row=0, column = 1)
#END OF INFO PANEL
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#SELLING PANEL
#Heading
sell_items = Label(root, text = "Sell Comics", justify=LEFT)
sell_items.grid(row=1, column = 0)

#selecting from list
selected_comic_sell = StringVar()
selected_comic_sell.set(comic_names[0])

#Dropdown
comic_menu = OptionMenu(root, selected_comic_sell, *comic_names)
comic_menu.grid(row=3, column = 0)

num_comics_sell = StringVar()
num_comics_sell.set("Quantity: ")

comic_entry = Entry(root, textvariable=num_comics_sell, justify=LEFT)
comic_entry.grid(row=3, column = 1)
comic_entry.bind("<Button-1>", sell_comic_placeholder)

select_btn = Button(root, text="Select", command=sell_comics, justify=RIGHT)
select_btn.grid(row=5, column = 1)

#message re-direct
message = StringVar()
message.set("")

#selling Comic error
error_message_sell = Label(root, textvariable=message, fg="red")
error_message_sell.grid(row=4, column = 1)
#END OF SELLING PANEL
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#RE-STOCK PANEL
#Heading
stock_items = Label(root, text = "Restock Comics", justify=LEFT)
stock_items.grid(row=1, column = 2)

#selecting from list
selected_comic_stock = StringVar()
selected_comic_stock.set(comic_names[0])

#Dropdown
comic_menu = OptionMenu(root, selected_comic_stock, *comic_names)
comic_menu.grid(row=3, column = 2)

num_comics_stock = StringVar()
num_comics_stock.set("Quantity: ")

comic_entry_stock = Entry(root, textvariable=num_comics_stock, justify=LEFT)
comic_entry_stock.grid(row=3, column = 3)
comic_entry_stock.bind("<Button-1>", restock_comic_placeholder)

select_btn_stock = Button(root, text="Select", command=stock_comics, justify=RIGHT)
select_btn_stock.grid(row=5, column = 3)

#message re-direct
message = StringVar()
message.set("")

#restock Comic error
error_message_sell = Label(root, textvariable=message, fg="red")
error_message_sell.grid(row=4, column = 3)
#END OF RE-STOCK PANEL
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#ADDING NEW COMICS
#label
add_comic = Label(root, text="Add New Comic")
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
add_btn = Button(root, text="Select", command=new_comic)
add_btn.grid(row = 10, columnspan = 1)

#error checking
message = StringVar()
message.set("")

add_error = Label(root, textvariable=message, fg="red")
add_error.grid(row= 9 , columnspan = 2)
#END OF ADDING NEW COMICS
#-------------------------------------------------------------------------------



update_label()
root.mainloop()