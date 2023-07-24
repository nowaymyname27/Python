# Required libraries for GUI and theme styling
import tkinter as tk
import ttkbootstrap as ttk

# Function to convert miles to kilometers
def convert():
    # Extracting the user input from the entry field
    mile_input = entry_int.get()

    # Conversion formula from miles to kilometers
    km_output = mile_input * 1.61

    # Setting the output_string to the converted kilometers
    output_string.set(km_output)

# Creating the main application window
window = ttk.Window(themename = 'darkly') # Using 'darkly' theme for styling
window.title('Demo') # Window title
window.geometry('300x150') # Setting window dimensions

# Label for the application title
title_label = ttk.Label(master = window, text = "Miles to Kilometers", font = "Calibri 24 bold")
title_label.pack() # Placing the label on the window

# Creating a frame for input widgets (entry field and button)
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar() # Variable to hold user input

# Entry field and button configuration
entry = ttk.Entry(master = input_frame, textvariable = entry_int) # Entry field for user input
button = ttk.Button(master = input_frame, text = 'Convert', command = convert) # Button to initiate conversion

# Placing the entry and button on the window
entry.pack(side = 'left', padx = 10) 
button.pack(side = 'left')
input_frame.pack(pady = 10) # Placing the frame on the window

# Creating a label to display the output
output_string = tk.StringVar() # Variable to hold the output
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)

# Placing the output label on the window
output_label.pack(pady = 5)

# Start the main event loop
window.mainloop() 
