from tkinter import *

root = Tk()
root.title("Hello World")
root.geometry("400x400")

my_label = Label(root, text="Hello World", fg="blue",
                 bg="gold", font=("Helvetica", 20))
my_label.pack()
my_label2 = Label(root, text="More Hello World", relief="sunken")
my_label2.pack()









root.mainloop()
