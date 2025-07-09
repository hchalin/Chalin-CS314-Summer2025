import tkinter as tk

#name
YOUR_NAME = "Hayden"

def say_morning():
    label.config(text=f"Good Morning {YOUR_NAME}")

def say_afternoon():
    label.config(text=f"Good Afternoon {YOUR_NAME}")

# Initialize the window
window = tk.Tk()
window.title("Lab 3 - Greetings")
window.geometry("300x200")

# Create buttons
btn_morning = tk.Button(window, text="Morning", command=say_morning)
btn_afternoon = tk.Button(window, text="Afternoon", command=say_afternoon)

btn_morning.pack(pady=10)
btn_afternoon.pack(pady=10)

# Add label below 2 buttons
label = tk.Label(window, text="")
label.pack(pady=20)

# run
window.mainloop()
