from tkinter import *

root = Tk()
root.title("Backup")
root.geometry("500x500")


def openMenu():
    inputTxt = e.get()
    labelTwo = Label(root, text=inputTxt, font=("arial", 20)).pack()


def showMenuItems():
    menu_label = Label(root, text="You clicked a menu item")
    menu_label.pack(pady=10)


def hide():
    pass


def show():
    pass


# labelOne = Label(root, text="Enter Dir to Backup", fg="black",
# font=("arial", 20)).pack(pady=10)

#e = Entry(root, font=("arial", 20))
# e.pack(pady=15)

#menuButton = Button(root, text="Backup", command=openMenu).pack(pady=10)
# Create menu
mainMenu = Menu(root)
root.config(menu=mainMenu)

# Create menu items
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="File", menu=fileMenu)
#   Menu items (file,edit...)
fileMenu.add_command(label="New", command=showMenuItems)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

# Edit menu
edit_menu = Menu(mainMenu)
mainMenu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=showMenuItems)
edit_menu.add_command(label="Copy", command=showMenuItems)
edit_menu.add_command(label="Paste", command=showMenuItems)

show_button = Button(root, text="show", command=show)
hide_button = Button(root, text="hide", command=hide)
show_button.grid(row=0, column=0)
hide_button.grid(row=0, column=1)

menu_frame = Frame(root, width=200, height=200,
                   bd=3, bg="blue", relief="sunken")
menu_frame.grid(row=4, column=1, columnspan=2, padx=20, pady=20)


root.mainloop()
