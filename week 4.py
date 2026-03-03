# import tkinter as tk
# window=tk.Tk()
# window.geometry("300x200")
# label=tk.Label(window,text="hello, Tkinter", fg="blue", bg="yellow",padx=10, pady=5)
# label.pack()
#
# button=tk.Button(window, text="click me", width=15, command=lambda:
#                  print("Button clicked"))
# button.pack()
# window.mainloop()
# import tkinter as tk
#
# window = tk.Tk()
# window.geometry("300x200")
# label = tk.Label(window, text="Initial Text",bg="red")
# label.pack()
#
# current_text = label.cget("text")
# print(f"Current text: {current_text}")
# current_bg = label.config()["bg"][-1] # Using config() and dictionary access
# print(f"Current background: {current_bg} ")
# window.mainloop()

# button  color changing
# import tkinter as tk
# window= tk.Tk()
# window.geometry("300x200")
# def color():
#     current_color=button.cget("bg")
#     if current_color=="red":
#         button.config(bg="green")
#     else:
#         button.config(bg="red")
#
# button=tk.Button(window, text="color changing", bg="red",command=color)
# button.pack()
# window.mainloop()

import tkinter as tk

def handle_click(event):
  print(f"Button clicked at X={event.x}, Y={event.y}")

def handle_key(event):
  print(f"Key pressed: {event.char}")

window = tk.Tk()
window.geometry("400x400")
button = tk.Button(window, text="Click Me",command=handle_click)
button.pack()

entry = tk.Entry(window)
entry.pack()

# Bind a function to a left mouse click on the button
button.bind("<Button-1>", handle_click)

# Bind a function to any key press on the entry widget
entry.bind("<Key>", handle_key)

window.mainloop()