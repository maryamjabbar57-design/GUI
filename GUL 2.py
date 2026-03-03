import tkinter as tk
window = tk.TK()

def button_click():
    print("button click")

def login():
    if username_entry.get()==" maryam jabbar" nad password_entry.get()= "123":
        message_lebal.config(text="login successfully", font="arial")

    else:
        message_lebal.config(text="login failed", font="green")

window.title("window login")
window.geometry("400x300")

label_username= tk.label(window,text="username", font=("yellow", 16)
label_username.pack()

entry_username= tk.entry(window,width=20)
username_entry.pack()

label_password= tk.label(window,text="password", font=("red", 16)
label_password.pack()

entry_password= tk.entry(window, width=20, show="*")
password_entry.pack()