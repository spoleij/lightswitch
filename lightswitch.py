import tkinter as tk
from typing import Text
window = tk.Tk()

button = tk.Button(text='...', bg="white", fg="black")                      
button.pack(pady = 20, padx = 20)
                                                              
# schijf hier tussen je code
button.config(text='switch light on')                               # changed the text= to say 'switch light on' instead of the standard '...'. this is how the button looks when you start the program
window['bg'] = 'black'                                              # change the window background color from grey to black (light is now off) same window as line 3

def clickButton(event):
    if button.config('text')[-1] == 'switch light on':              # if the text on the button equals 'switch light ON' it will now change to 'switch light OFF'
        button.config(text='switch light off')                      
        window['bg'] = 'yellow'                                     # change the window background color from black gto yellow (light is now on)
        print ("the light is on")
    else:
        button.config(text='switch light on')                       # opposite. if the button text equals LIGHT ON, it will now become LIGHT OFF. and the background color is now black (light is now off again)
        print ("the light is off")
        window['bg'] = 'black'

button.bind("<Button-1>", clickButton)                              # Button-1 is the left mouse button. if you click on the button with the left mouse button you start the clickButton function
# schijf hier tussen je code

window.mainloop()