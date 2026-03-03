import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        if combo.get() == "Celsius to Fahrenheit":
            result = (temp * 9/5) + 32
            label_result.config(text=f"Result: {result:.2f} °F")
        elif combo.get() == "Fahrenheit to Celsius":
            result = (temp - 32) * 5/9
            label_result.config(text=f"Result: {result:.2f} °C")
    except ValueError:
        label_result.config(text="Please enter a valid number")

# Main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x250")

# Title
tk.Label(root, text="Temperature Converter", font=("Arial", 14, "bold")).pack(pady=10)

# Entry
entry_temp = tk.Entry(root, font=("Arial", 12))
entry_temp.pack(pady=5)

# Dropdown
combo = ttk.Combobox(root, values=[
    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius"
])
combo.current(0)
combo.pack(pady=5)

# Button
tk.Button(root, text="Convert", command=convert_temperature).pack(pady=10)

# Result Label
label_result = tk.Label(root, text="Result: ", font=("Arial", 12))
label_result.pack(pady=10)

root.mainloop()