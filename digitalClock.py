import tkinter as tk
from time import strftime

# Function to update the time
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)  # Update the time every 1 second

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Configure the appearance of the clock
label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
label.pack(anchor='center')

# Call the time function to initialize the clock
time()

# Run the application
root.mainloop()
