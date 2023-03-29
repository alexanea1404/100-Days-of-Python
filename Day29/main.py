import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(END,password)
    #copy a specific element
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website:{"email":email,
                        "password":password
                         }
                }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="You left a box empty", message="You left a box empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                 #Reading the old data
                 data = json.load(data_file)

        except FileNotFoundError:
             with open("data.json", "w") as data_file:
                #Saving the data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving the data
                 json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

#----------------------------FIND PASSWORD-----------------------------#
def find_password():
    website = website_input.get()
    try:
        with open ("data.json") as data_file:
            data_entries = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="You left a box empty", message="Error, no file found")
    else:

        if website in data_entries:
            email = data_entries[website]["email"]
            password = data_entries[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\n Password:{password}")
        else:
            messagebox.showinfo(title="Password", message="No details for this website exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_text = Label(text="Website:")
website_text.grid(column=0, row=1)

website_input = Entry(width=21)
website_input.focus()
website_input.grid(column=1, row=1)

search = Button(text="Search", command=find_password, width=10)
search.grid(column=2, row=1)

email_text = Label(text="Email/Username:")
email_text.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.insert(END, "email@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)

password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate = Button(text="Generate", command=generate_password, width=10)
generate.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
