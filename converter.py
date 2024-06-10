from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx= 20, pady= 20)

def convert():
    result = int(mile_entry.get()) * 1.60934
    num_of_km["text"] = int(result)
    
    
mile_entry = Entry()
mile_entry["width"] = 10
mile_entry.grid(row=0, column=1)

mile_label = Label(text="Miles")
mile_label.grid(row=0, column=2)

num_of_km = Label(text= "0")
num_of_km.grid(row=1, column=1)

km = Label(text= "Km")
km.grid(row=1, column=2)

button = Button(text="Calculate", command= convert)
button.grid(row=2, column=1)

window.mainloop()