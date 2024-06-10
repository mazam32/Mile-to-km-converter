from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height=300)
window.config(padx= 20, pady=20)
def button_clicked():
    my_label["text"] = input.get()
    

my_label = Label(text= "I am a label", font= ("Arial", 24, "bold"))
my_label.grid(column= 0, row= 0)
my_label["text"] = "New Text"

button = Button(text= "Click Me",command= button_clicked)
button.grid(row=1, column=1)

input = Entry(width= 10)
input.grid(row=2, column=3)

new_button = Button(text= "New Button")
new_button.grid(row=0, column=2)



window.mainloop()
