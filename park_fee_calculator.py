# write a gui application that calculate some phone call charges 

import tkinter as tk
from tkinter import messagebox as mb

window = tk.Tk()
window.geometry("400x170")

var = tk.IntVar()

def ironman():
        return var.get()

def calculated_charges():
        if var.get() == 1:  #daytime
                result = (0.07) * int(entry.get())
                result = round(result,2)

        elif var.get() == 2:
                result = (0.12) * int(entry.get())
                result =  round(result,2)

        elif var.get() == 3:
                result = (0.05) * int(entry.get())
                result =  round(result,2)

        return message_box(result)
        
def message_box(result):
        mb.showinfo("Total Charges",f"Your total charges = ${result}")

entry = tk.Entry(window,font = ("Consolas",12) )
entry.place(x=200,y=88)


display_button = tk.Button(window,
                            text=("Display Charges"),
                            font=("Consolas",13),
                            fg="black",
                            command=calculated_charges)

display_button.place(x=90,y=120)
quit_button = tk.Button(window,
                            text=("Quit"),
                            font=("Consolas",13),
                            fg="black",
                            command=window.destroy)

quit_button.place(x=250,y=120)

entry_label = tk.Label(window,
                        text="Enter the number of minutes:",
                        font=("Consolas",8))

entry_label.place(x=10,y=90)


check_but1 = tk.Radiobutton(text="Daytime (6.00am - 5.59pm)",
                            font=("Consolas",11),variable = var, value= 1, command=ironman)

check_but2 = tk.Radiobutton(text="Evening (6.00pm - 11.59pm)",
                            font=("Consolas",11),variable = var, value= 2, command=ironman)

check_but3 = tk.Radiobutton(text="Off-Peak (12.00am - 5.59am)",
                            font=("Consolas",11),variable = var, value= 3,command=ironman)

check_but1.place(x=85,y=3)
check_but2.place(x=85,y=25)
check_but3.place(x=85,y=48)



window.mainloop()









