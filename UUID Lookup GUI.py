import tkinter as tk
import requests
import os.path

#Root menu setup
root = tk.Tk()
root.title("UUID Lookup")
root.configure(background='black')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.geometry("500x300")

#Final Menu
def Final_Menu(data, filename):
    menu = tk.Tk()
    menu.title("UUID + Username!")
    text = tk.Entry(menu)
    text.insert(tk.END, data)
    text.grid(row=0, column=0, sticky="NSEW", columnspan=2)
    text.configure(selectforeground="blue", foreground="red", background="black", selectbackground="red", font=("Arial", 32, "bold"))

    menu.configure(background='black')
    menu.columnconfigure(0, weight=1)
    menu.rowconfigure(0, weight=1)

    menu.geometry("1500x100")
    menu.mainloop()

    if os.path.isfile("files/"+filename + ".txt"):
        f = open("files/"+filename + ".txt", "x")
        f.write(str(data))
        f.close()
    else:
        f = open("files/"+filename + ".txt", "x")
        f.write(str(data))
        f.close()

#User Menu
def USER_pressed():
    user_menu = tk.Tk()
    user_menu.title("Enter Username")
    user_menu.configure(background='black')
    root.destroy()

    def enter_username(event=None):
        USER = username.get()
        if USER:
            api_url = "https://api.mojang.com/users/profiles/minecraft/" + USER
            resp = requests.get(url=api_url)
            data = resp.json()
            user_menu.destroy()
            Final_Menu(data,USER)
            username.delete(0, tk.END)

    username = tk.Entry(user_menu)
    username.grid(row=0, column=0)
    username.configure(selectforeground="blue", foreground="red", background="black", selectbackground="red",font=("Arial", 16, "bold"))

    add_user_button = tk.Button(user_menu, text="Add User", command=enter_username)
    add_user_button.grid(row=0, column=1)
    add_user_button.configure(background='black', foreground='Red', font=("Arial", 16, "bold"), highlightcolor="red")
    user_menu.bind("<Return>", enter_username)

    user_menu.configure(background='black')
    user_menu.columnconfigure(0, weight=1)
    user_menu.columnconfigure(1, weight=1)
    user_menu.rowconfigure(0, weight=1)
    user_menu.geometry("400x100")
    user_menu.mainloop()

#UUID Menu
def UUID_pressed():
    UUID_menu = tk.Tk()
    UUID_menu.title("Enter UUID")
    root.destroy()

    def enter_UUID(event=None):
        UUID = UUID_input.get()
        if UUID:
            api_url = "https://api.minecraftservices.com/minecraft/profile/lookup/" + UUID
            resp = requests.get(url=api_url)
            data = resp.json()
            Final_Menu(data,UUID)
            UUID_menu.destroy()
            UUID_input.delete(0, tk.END)

    UUID_input = tk.Entry(UUID_menu)
    UUID_input.grid(row=0, column=0)
    UUID_input.configure(selectforeground="blue", foreground="red", background="black", selectbackground="red",font=("Arial", 16, "bold"))

    entry_button = tk.Button(UUID_menu, text="Enter UUID", command=enter_UUID)
    entry_button.grid(row=0, column=1)
    entry_button.configure(background='black',foreground='Red',font=("Arial",16,"bold"),highlightcolor="red")
    UUID_menu.bind("<Return>", enter_UUID)

    UUID_menu.configure(background='black')
    UUID_menu.columnconfigure(0, weight=1)
    UUID_menu.columnconfigure(1, weight=1)
    UUID_menu.rowconfigure(0, weight=1)
    UUID_menu.geometry("400x100")
    UUID_menu.mainloop()

#Root Menu
USER_btn = tk.Button(root, text="Username", command=USER_pressed)
USER_btn.grid(row=0, column=0, sticky="NSEW")
USER_btn.configure(background='black',foreground='Red',font=("Arial",16,"bold"),highlightcolor="red")

UUID_btn = tk.Button(root, text="UUID", command=UUID_pressed)
UUID_btn.grid(row=1, column=0, sticky="NSEW")
UUID_btn.configure(background='black',foreground='blue',font=("Arial", 16, "bold"),highlightcolor="blue")

root.mainloop()