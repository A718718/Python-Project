import tkinter as tk
from time import strftime
def update_time():
    # Time display (12-hour format with AM/PM)
    current_time = strftime('%I:%M:%S %p')

    # Date display
    current_date = strftime('%A, %B %d, %Y')

    # Update labels
    time_label.config(text=current_time)
    date_label.config(text=current_date)

    # Schedule next update
    time_label.after(1000, update_time)


# Create main window
root = tk.Tk()
root.title("Python Digital Clock")
root.geometry("600x200")
root.configure(bg='black')
root.resizable(False, False)

# Time label styling
time_label = tk.Label(root,
                      font=('Courier New', 60, 'bold'),
                      bg='black',
                      fg='orange',
                      pady=20)
time_label.pack()

# Date label styling
date_label = tk.Label(root,
                      font=('Arial', 20),
                      bg='black',
                      fg='white')
date_label.pack()

# Initial update
update_time()

# Run the application
root.mainloop()


