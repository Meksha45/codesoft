import string
import random
from tkinter import *
from tkinter import messagebox
import re
import sqlite3

# Initialize the database
with sqlite3.connect("users.db") as db:
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            Username TEXT NOT NULL, 
            GeneratedPassword TEXT NOT NULL
        );
    """)
    db.commit()

class GUI():
    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.passwordlen = IntVar()
        self.generatedpassword = StringVar()
        self.n_username = StringVar()
        self.n_generatedpassword = StringVar()
        self.n_passwordlen = IntVar()

        # Checkbox variables
        self.use_upper = BooleanVar(value=True)
        self.use_lower = BooleanVar(value=True)
        self.use_digits = BooleanVar(value=True)
        self.use_special = BooleanVar(value=True)

        root.title('Unique Password Generator')
        root.geometry('700x600')
        root.config(bg='#FF8000')
        root.resizable(False, False)

        Label(text=":PASSWORD GENERATOR:", fg='darkblue', bg='#FF8000', font='arial 20 bold underline').grid(row=0, column=1, pady=10)

        Label(text="Enter User Name: ", font='times 15 bold', bg='#FF8000', fg='darkblue').grid(row=1, column=0, sticky=E)
        self.textfield = Entry(textvariable=self.n_username, font='times 15', bd=6, relief='ridge')
        self.textfield.grid(row=1, column=1)
        self.textfield.focus_set()

        Label(text="Enter Password Length: ", font='times 15 bold', bg='#FF8000', fg='darkblue').grid(row=2, column=0, sticky=E)
        self.length_textfield = Entry(textvariable=self.n_passwordlen, font='times 15', bd=6, relief='ridge')
        self.length_textfield.grid(row=2, column=1)

        # Character type options
        Checkbutton(master, text="Uppercase", variable=self.use_upper, bg='#FF8000', font='times 12').grid(row=3, column=0)
        Checkbutton(master, text="Lowercase", variable=self.use_lower, bg='#FF8000', font='times 12').grid(row=3, column=1)
        Checkbutton(master, text="Digits", variable=self.use_digits, bg='#FF8000', font='times 12').grid(row=4, column=0)
        Checkbutton(master, text="Special Characters", variable=self.use_special, bg='#FF8000', font='times 12').grid(row=4, column=1)

        Label(text="Generated Password: ", font='times 15 bold', bg='#FF8000', fg='darkblue').grid(row=5, column=0, sticky=E)
        self.generated_password_textfield = Entry(textvariable=self.n_generatedpassword, font='times 15', bd=6, relief='ridge', fg='#DC143C')
        self.generated_password_textfield.grid(row=5, column=1)

        self.strength_label = Label(text="", bg='#FF8000', font='times 13 bold')
        self.strength_label.grid(row=6, column=1)

        Button(text="GENERATE PASSWORD", bd=3, relief='solid', font='Verdana 15 bold', fg='#68228B', bg='#BCEE68', command=self.generate_pass).grid(row=7, column=1, pady=10)
        Button(text="ACCEPT", bd=3, relief='solid', font='Helvetica 15 bold italic', fg='#458B00', bg='#FFFAF0', command=self.accept_fields).grid(row=8, column=1, pady=5)
        Button(text="RESET", bd=3, relief='solid', font='Helvetica 15 bold italic', fg='#458B00', bg='#FFFAF0', command=self.reset_fields).grid(row=9, column=1, pady=5)
        Button(text="SHOW USERS", font='Helvetica 12', bg='lightblue', command=self.show_users).grid(row=10, column=1, pady=10)

    def generate_pass(self):
        name = self.textfield.get().strip()
        leng = self.length_textfield.get().strip()

        if not name:
            messagebox.showerror("Error", "Name cannot be empty")
            return

        if not name.isalpha():
            messagebox.showerror("Error", "Name must be a string")
            self.textfield.delete(0, END)
            return

        if not leng.isdigit() or int(leng) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long")
            return

        length = int(leng)
        chars_pool = []
        if self.use_upper.get(): chars_pool += list(string.ascii_uppercase)
        if self.use_lower.get(): chars_pool += list(string.ascii_lowercase)
        if self.use_digits.get(): chars_pool += list(string.digits)
        if self.use_special.get(): chars_pool += list("@#%&()\"?!")

        if not chars_pool:
            messagebox.showerror("Error", "Select at least one character type")
            return

        password = ''.join(random.choices(chars_pool, k=length))
        self.generated_password_textfield.delete(0, END)
        self.generated_password_textfield.insert(0, password)

        strength = self.evaluate_strength(password)
        self.strength_label.config(text=f"Strength: {strength}", fg='green' if strength == 'Strong' else 'orange' if strength == 'Moderate' else 'red')

    def evaluate_strength(self, password):
        strength = "Weak"
        if (len(password) >= 8 and re.search(r"[A-Z]", password)
            and re.search(r"[a-z]", password)
            and re.search(r"[0-9]", password)
            and re.search(r"[@#%&()\"?!]", password)):
            strength = "Strong"
        elif len(password) >= 6:
            strength = "Moderate"
        return strength

    def accept_fields(self):
        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users WHERE Username = ?", (self.n_username.get(),))
            if cursor.fetchall():
                messagebox.showerror("Duplicate Username", "This username already exists!")
            else:
                cursor.execute("INSERT INTO users(Username, GeneratedPassword) VALUES (?, ?)", (self.n_username.get(), self.n_generatedpassword.get()))
                db.commit()
                messagebox.showinfo("Success", "Password stored successfully")

    def reset_fields(self):
        self.textfield.delete(0, END)
        self.length_textfield.delete(0, END)
        self.generated_password_textfield.delete(0, END)
        self.strength_label.config(text="")

    def show_users(self):
        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users")
            records = cursor.fetchall()

        win = Toplevel(self.master)
        win.title("Stored Users")
        win.geometry("400x300")
        for i, (user, pwd) in enumerate(records):
            Label(win, text=f"{i+1}. {user} - {pwd}", font='times 12').pack(anchor=W)

if __name__ == '__main__':
    root = Tk()
    pass_gen = GUI(root)
    root.mainloop()
