import tkinter as tk
from time import strftime

# Function to update the time
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)  # Update the time every 1 second

# Function to create a gradient background
def create_gradient(canvas, color1, color2):
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    limit = height
    (r1, g1, b1) = canvas.winfo_rgb(color1)
    (r2, g2, b2) = canvas.winfo_rgb(color2)
    r_ratio = float(r2 - r1) / limit
    g_ratio = float(g2 - g1) / limit
    b_ratio = float(b2 - b1) / limit

    for i in range(limit):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = f'#{nr:04x}{ng:04x}{nb:04x}'
        canvas.create_line(0, i, width, i, fill=color)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a canvas for gradient background
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack(fill='both', expand=True)

# Create gradient background
canvas.bind('<Configure>', lambda event: create_gradient(canvas, '#000428', '#004e92'))

# Create a frame for the clock
frame = tk.Frame(canvas, bg='black')
frame.place(relx=0.5, rely=0.5, anchor='center')

# Configure the appearance of the clock
label = tk.Label(frame, font=('Helvetica', 48, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

# Call the time function to initialize the clock
time()

# Run the application
root.mainloop()
