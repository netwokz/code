
# importing whole module
from tkinter import * 
from tkinter.ttk import *
import sv_ttk
# importing strftime function to
# retrieve system's time
import psutil
  
# creating tkinter window
root = Tk()
root.title('Clock')
root.minsize(600, 600)

# This function is used to 
# display time on the label
def display_time():
    string = psutil.cpu_percent(1)
    lbl.config(text = string)
    lbl.after(500, display_time)
  
# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'black',
            foreground = 'white')
  
# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor = 'center')
display_time()
sv_ttk.set_theme("dark")
mainloop()

