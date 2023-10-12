from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    chosen_letters = random.choices(letters, k=random.randint(8, 10))
    chosen_symbols = random.choices(symbols, k=random.randint(2, 4))
    chosen_numbers = random.choices(numbers, k=random.randint(2, 4))

    password = chosen_letters + chosen_symbols + chosen_numbers
    random_password = ''

    randomize = random.sample(password, len(password))

    for character in range(len(randomize)):

        random_password += randomize[character]

    password_entry.insert(END, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title='No Entry', message='Please enter both the website and password')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details enter: \nUsername: {username} '
                                                              f'\nPassword: {password} \nIs it ok to save?')
        if is_ok:
            with open('mypassword.txt', 'a') as password_file:
                password_file.write(f'{website} | {username} | {password} \n')

                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
photo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo_image)
canvas.grid(row=0, column=1)

website_label = Label(text='Website: ')
website_label.grid(row=1, column=0)

username_label = Label(text='Email/Username: ')
username_label.grid(row=2, column=0)

password_label = Label(text='Password: ')
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(END, 'sample_email@gmail.com')

password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)

password_button = Button(text='Generate Password', command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text='Add', width=30, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()

