from tkinter import *
from tkinter.ttk import Progressbar
import tkinter
import tkinter.messagebox
import pyperclip
import random, string

no_of_options = 0
length_value = 7


def get_slider_value(value):
    global length_value
    length_value = int(value)
    progress_status()


def progress_status():
    score = 0

    if upper_case.get():
        score += 10
    if small_case.get():
        score += 10
    if num.get():
        score += 10
    if special_Chars.get():
        score += 15

    score += length_value * 2

    length_progress['value'] = score


def generate_pass():
    global no_of_options, length_value
    password = ""

    switchCode = str(upper_case.get())+str(small_case.get())+str(special_Chars.get())+str(num.get())

    switcher = {
        '1100': generate1,
        '1101': generate2,
        '0001': generate3,
        '1111': generate4,
        '0100': generate5,
        '1000': generate6,
        '0010': generate7,
        '1001': generate8,
        '0101': generate9,
        '1010': generate10,
        '0110': generate11,
        '1110': generate12,
        '0011': generate13,
        '0111': generate14
    }
        
    password = switcher.get(switchCode, lambda: "Please select atleast one checkbox ")()

    password_entry.delete(0, END)
    password_entry.insert(0, password)

def save_password():
    password = password_entry.get()
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")

def dark_mode():
    root.configure(bg="black")

def generate1():
    "Upper Smaller"
    try:
        n = int(length_value)
        password = ""
        up_sm = string.ascii_uppercase + string.ascii_lowercase
        if n > len(up_sm):
            return "Length too large"
        password = ''.join(random.choices(up_sm, k=n))
    except:
        return "Invalid length_value"


def generate2():
    "Upper smaller number"
    try:
        n = int(length_value)
        password = ""
        up_sm_num = string.ascii_uppercase + string.ascii_lowercase + string.digits
        password = password.join(random.sample(up_sm_num, n))
        return password
    except:
        return "Invalid length_value"


def generate3():
    "Number"
    try:
        n = int(length_value)
        password = ""
        num = string.digits
        password = password.join(random.sample(num, n))
        return password
    except:
        return "Invalid length_value"


def generate4():
    "Upper smaller number special"
    try:
        n = int(length_value)
        password = ""
        up_sm_num_spc = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        password = password.join(random.sample(up_sm_num_spc, n))
        return password
    except:
        return "Invalid length_value"


def generate5():
    "Smaller"
    try:
        n = int(length_value)
        password = ""
        sm = string.ascii_lowercase
        password = password.join(random.sample(sm, n))
        return password
    except:
        return "Invalid length_value"


def generate6():
    "Upper"
    try:
        n = int(length_value)
        password = ""
        up = string.ascii_uppercase
        password = password.join(random.sample(up, n))
        return password
    except:
        return "Invalid length_value"


def generate7():
    "Special"
    try:
        n = int(length_value)
        password = ""
        spc = string.punctuation
        password = password.join(random.sample(spc, n))
        return password
    except:
        return "Invalid length_value"


def generate8():
    "Upper number"
    try:
        n = int(length_value)
        password = ""
        up_num = string.ascii_uppercase + string.digits
        password = password.join(random.sample(up_num, n))
        return password
    except:
        return "Invalid length_value"


def generate9():
    "Smaller Number"
    try:
        n = int(length_value)
        password = ""
        sm_num = string.digits + string.ascii_lowercase
        password = password.join(random.sample(sm_num, n))
        return password
    except:
        return "Invalid length_value"


def generate10():
    "Upper Special"
    try:
        n = int(length_value)
        password = ""
        up_spc = string.ascii_uppercase + string.punctuation
        password = password.join(random.sample(up_spc, n))
        return password
    except:
        return "Invalid length_value"


def generate11():
    "Smaller Special"
    try:
        n = int(length_value)
        password = ""
        sm_spc = string.punctuation + string.ascii_lowercase
        password = password.join(random.sample(sm_spc, n))
        return password
    except:
        return "Invalid length_value"


def generate12():
    "Smaller Upper Special"
    try:
        n = int(length_value)
        password = ""
        sm_up_spc = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
        password = password.join(random.sample(sm_up_spc, n))
        return password
    except:
        return "Invalid length_value"


def generate13():
    "Number Spceial"
    try:
        n = int(length_value)
        password = ""
        num_spc = string.digits + string.punctuation
        password = password.join(random.sample(num_spc, n))
        return password
    except:
        return "Invalid length_value"


def generate14():
    "Smaller Number Special"
    try:
        n = int(length_value)
        password = ""
        sm_num_spc = string.digits + string.ascii_lowercase + string.punctuation
        password = password.join(random.sample(sm_num_spc, n))
        return password
    except:
        return "Invalid length_value"


def copyclip():
    passwordcopy = password_entry.get()
    pyperclip.copy(passwordcopy)


root = Tk()
root.title("TryCatch Password Generator")
root.geometry("700x300")

title = Label(root, text="TryCatch-Password Generator",
              fg="Blue", font=("Arial", 15, 'bold')).place(x=200, y=10)

num = IntVar()
small_case = IntVar()
upper_case = IntVar()
special_Chars = IntVar()
length = IntVar()
password_str = StringVar()

# Checkboxes
C1 = Checkbutton(root, text="A-Z", variable=upper_case, onvalue=1, offvalue=0, command=progress_status)
C1.place(x=100, y=40)
C2 = Checkbutton(root, text="a-z", variable=small_case, onvalue=1, offvalue=0, command=progress_status)
C2.place(x=180, y=40)
C3 = Checkbutton(root, text="0-9", variable=num, onvalue=1, offvalue=0, command=progress_status)
C3.place(x=250, y=40)
C4 = Checkbutton(root, text="special characters", variable=special_Chars, onvalue=1, offvalue=0,
                 command=progress_status)
C4.place(x=320, y=40)

# Length scale
s1 = Scale(root, variable=length,
           from_=7, to=16,
           orient=HORIZONTAL, command=get_slider_value
           )
s1.place(x=550, y=40)
scale_lable = Label(root, text="Length",
                    font=("Arial", 11)).place(x=500, y=40)

strength_lable = Label(root, text="Password Strength",
                       font=("Arial", 12, "bold")).place(x=280, y=80)

# Progressbar to show strength
length_progress = Progressbar(root, orient=HORIZONTAL,
                              length=400, mode='determinate')
length_progress.place(x=150, y=120)

btn = Button(master=root, text="calculate", fg="green",
             font=("Arial", 10, 'bold'), command=generate_pass).place(x=300, y=150)

password_entry = Entry(root, width=30)
password_entry.place(x=220, y=200)
save_btn = Button(root, text="Save", command=save_password)
save_btn.place(x=380, y=230)

dark_btn = Button(root, text="Dark Mode", command=dark_mode)
dark_btn.place(x=450, y=230)

copy_btn = Button(master=root, text="Copy", fg="green",
                  font=("Arial", 10, 'bold'), command=copyclip).place(x=320, y=230)

photo = PhotoImage(file="Password Genetator/password.png")
root.iconphoto(False, photo)

root.mainloop()
