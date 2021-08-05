from tkinter import *

root = Tk()

entry1 = Entry(root, width=50, borderwidth=5)
entry1.grid(row=0, column=0)
entry1.insert(0, "First Name")

entry2 = Entry(root, width=50, borderwidth=5)
entry2.grid(row=1, column=0)
entry2.insert(0, "Last Name")

entry3 = Entry(root, width=50, borderwidth=5)
entry3.grid(row=2, column=0)
entry3.insert(0, "Email")

def execution():
    entries = entry1.get()
    entries2 = entry2.get()
    entries3 = entry3.get()
    label = Label(root, text=entries)
    label.grid(row=4, column=0)
    label2 = Label(root, text=entries2)
    label2.grid(row=5, column=0)
    label3 = Label(root, text=entries3)
    label3.grid(row=6, column=0)

button = Button(root, text="Enter", command=execution)
button.grid(row=3, column=0)





root.mainloop()
