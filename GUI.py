import tkinter as tk

window = tk.Tk()

def button_click():
    print("button click")

def login():
    if username_entry.get() == "Maryam Jabbar" and password_entry.get() == "123":
        message_label.config(text="Login Successfully", fg="green")
    else:
        message_label.config(text="Login Failed. Please try again", fg="red")

window.title("Login Window")
window.geometry("300x250")

# Username Label
label_username = tk.Label(window, text="Username", font=("Arial", 16))
label_username.pack()

# Username Entry
username_entry = tk.Entry(window, width=30)
username_entry.pack()

# Password Label
label_password = tk.Label(window, text="Password", font=("Arial", 16))
label_password.pack()

# Password Entry
password_entry = tk.Entry(window, width=30, show="*")
password_entry.pack()

# Login Button
login_button = tk.Button(window, text="Login", command=login)
login_button.pack(pady=10)

# Message Label
message_label = tk.Label(window, text="")
message_label.pack()

window.mainloop()
