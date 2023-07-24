import tkinter as tk
from tkinter import ttk

def button_func():
    print("Button pressed")
    
def button_func2():
    print("Hello")

# create a window
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x500")

# ttk label
label = ttk.Label(master = window, text = "This a test")
label.pack()

# create widgets
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# ttk label 2
label2 = ttk.Label(master = window, text = "My label")
label2.pack()

# ttk button
button = ttk.Button(master = window, text = "A button", command = button_func)
button.pack()

# ttk button 2
# button2 = ttk.Button(master = window, text = "Hello", command = button_func2)
button2 = ttk.Button(master = window, text = "Hello", command = lambda: print("Hello"))
button2.pack()

#run the window
window.mainloop()