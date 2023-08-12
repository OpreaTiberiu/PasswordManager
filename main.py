import re
from tkinter import *
from tkinter import messagebox
from generate_pass import generate_pass


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def set_password():
    pass_entry.delete(0, END)
    pass_entry.insert(0, generate_pass())
    messagebox.showinfo(message="Your password was copied to Clipboard!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, user_entry.get()):
        with open("credentials.txt", "a") as f:
            f.write(f"{website_entry.get()} | {user_entry.get()} | {pass_entry.get()}\n")
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
    else:
        messagebox.showerror(title="Error", message="You do not appear to have introduced a proper email. Try again!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

logo = PhotoImage(file="logo.png")
canvas = Canvas(
    width=200,
    height=200,
    bg="white",
    highlightthickness=0
)
canvas.create_image(100,
                    100,
                    image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)
website_entry = Entry(width=52, bg="white")
website_entry.grid(row=1, column=1, columnspan=2)

user_label = Label(text="Email/Username:", bg="white")
user_label.grid(row=2, column=0)
user_entry = Entry(width=52, bg="white")
user_entry.grid(row=2, column=1, columnspan=2)

pass_label = Label(text="Password:", bg="white")
pass_label.grid(row=3, column=0)
pass_entry = Entry(width=33, bg="white", show='*')
pass_entry.grid(row=3, column=1, padx=1)

generate_pass_button = Button(text="Generate Password", command=set_password)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save_to_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
