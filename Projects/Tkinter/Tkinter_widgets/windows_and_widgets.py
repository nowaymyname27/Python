import tkinter as tk
from tkinter import ttk

# create a window
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x500")

# create widgets
text = tk.Text(master = window)
text.pack()

# ttk widgets


#run the window
window.mainloop()