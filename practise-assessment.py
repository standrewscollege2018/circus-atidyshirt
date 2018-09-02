from tkinter import *

root = Tk()
root.title("Circus Tickets")
root.geometry('450x300')

class Ticket:
    def __init__(self, time, capacity, cost):
        self._time = time
        self._capacity = capacity
        self._cost = cost
        tickets.append(self)

def update_label():
    ticket_info.set("")
    for t in tickets:
        ticket_info.set(ticket_info.get() + t._time + t._capacity + "  $" + str(t._cost) + "\n")

time = []
capacity = []
cost = []
sold = 0

Ticket("10am", 150, 5)
Ticket("3pm", 150, 5)
Ticket("8pm", 250, 12)

ticket_lbl = Label(root, textvariable=ticket_info)
ticket_lbl.grid(row = 0)

selected_tickets = StringVar()
selected_tickets.set(names[0])









root.mainloop()
