from tkinter import *
from tkinter import messagebox
import random
import string
import json

FILE_PATH = 'day-30/passwords.json'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_random_password():
    maxLetters = random.randint(8,10)
    maxSimbols = random.randint(2,4)
    maxNumber = random.randint(2,4)

    passwordLetters = []

    for i in range(0,maxLetters + maxSimbols + maxNumber):
        if maxSimbols > 0: 
            passwordLetters.append(random.choice(string.punctuation))
            maxSimbols -= 1
        elif maxNumber > 0:
            passwordLetters.append(random.choice(string.digits))
            maxNumber -= 1
        else:
            passwordLetters.append(random.choice(string.ascii_letters))

    random.shuffle(passwordLetters)

    random_password = f"{''.join(passwordLetters)}"

    input_password.delete(0,END)
    input_password.insert(0,random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = input_website.get()
    username = input_username.get()
    password = input_password.get()

    new_data = {
        website: {
            'email': username,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Missing fiels",message="website and password are not allowed to be empty!")
        return 

    try:
        with open(FILE_PATH,'r') as file:
            data = json.load(file)
            
    except FileNotFoundError:
        with open(FILE_PATH,'w') as file:
            json.dump(new_data,file, indent=4)
    else:
        data.update(new_data)
        with open(FILE_PATH,'w') as file:
            json.dump(data,file, indent=4)
    finally:
        input_website.delete(0, END)
        input_password.delete(0, END)

def search_json():
    website = input_website.get()
    try:
        with open(FILE_PATH,'r') as file:
            data = json.load(file)

            messagebox.showinfo(title=f"{website} infos",message=f"email: {data[website]['email']}\npassword: {data[website]['password']}")

    except FileNotFoundError:
        messagebox.showerror(title='Not Found',message=f"{website} not found!")
    except KeyError:
        messagebox.showerror(title='Not Found',message=f"{website} not found!")
# ---------------------------- UI SETUP ------------------------------- #   

BG_COLOR="#FFFFFF"

window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

logo_img = PhotoImage(file='day-29/logo.png')
canva = Canvas(width=200, height=200,highlightthickness=0)
canva.create_image(100,100,image=logo_img)
canva.grid(row=0,column=1)


label_website = Label(text='Website:')
label_website.grid(row=1,column=0)
label_website.config(padx=10,pady=10)
label_username = Label(text='Email/Username:')
label_username.grid(row=2,column=0)
label_username.config(padx=10,pady=10)
label_password = Label(text='Password:')
label_password.grid(row=3,column=0)
label_password.config(padx=10,pady=10)


input_website = Entry(width=21)
input_website.grid(row=1,column=1)
input_website.focus()

input_username = Entry(width=41)
input_username.grid(row=2,column=1,columnspan=2)
input_username.insert(0,'gabrielvictor933@gmail.com')

input_password = Entry(width=21)
input_password.grid(row=3,column=1)

button_search = Button(text='search', command=search_json)
button_search.grid(row=1,column=2)

button_password = Button(text='Generate Password', command=generate_random_password)
button_password.grid(row=3,column=2)

button_add = Button(text='Add',width=36, command=save_data)
button_add.grid(row=4,column=1,columnspan=2)

window.mainloop()