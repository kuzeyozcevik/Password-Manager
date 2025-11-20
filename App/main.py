import tkinter
import tkinter.messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def create_pass():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    return password
def put_pass():
    created_pass = create_pass()
    password_entry.delete(0,tkinter.END)
    password_entry.insert(0,created_pass)
    pyperclip.copy(created_pass)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    password = f"{website_entry.get()} | {email_username_entry.get()} | {password_entry.get()}"
    if ((len(website_entry.get()) == 0) or (len(website_entry.get()) == 0) or (len(password_entry.get()) == 0)):
        msg_box = tkinter.messagebox.showwarning(title="You must enter something",message="Don't leave empty blank")
    else:
        is_ok = tkinter.messagebox.askokcancel(title=website_entry.get(),message=f"These are the details entered: "
                                                                  f"\nEmail/Username: {email_username_entry.get()}\n "
                                                                  f"Password: {password_entry.get()}\n "
                                                                 f"Do you want to save these?")
        if is_ok:
            with open("password.txt","a")as f:
                f.write(password + "\n")
            website_entry.delete(0,tkinter.END)
            email_username_entry.delete(0,tkinter.END)
            password_entry.delete(0,tkinter.END)
            email_username_entry.insert(0,"@gmail.com")


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)


canvas = tkinter.Canvas(height=200,width=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

website_text = tkinter.Label(text="Website")
website_text.grid(column=0,row=1)

website_entry = tkinter.Entry(width=39)
website_entry.grid(column=1,row=1,columnspan=2)

email_username_text = tkinter.Label(text="Email/Username")
email_username_text.grid(column=0,row=2)

email_username_entry = tkinter.Entry(width=39)
email_username_entry.grid(column=1,row=2,columnspan=2)
email_username_entry.insert(0,"@gmail.com")

password_text = tkinter.Label(text="Password")
password_text.grid(column=0,row=3)

password_entry = tkinter.Entry()
password_entry.grid(column=1,row=3, sticky="ew")

generate_password = tkinter.Button(text="Generate Password",command=put_pass)
generate_password.grid(column=2,row=3, sticky="ew")

add_button = tkinter.Button(text="Add",width=37,command=save)
add_button.grid(column=1,row=4,columnspan=2)





window.mainloop()