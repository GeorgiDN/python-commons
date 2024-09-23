import re
import tkinter as tk
from tkinter import messagebox


class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.geometry('500x500')
        self.root.title("Registration Form")

        # Instance variables for error labels
        self.first_name_error_label = None
        self.last_name_error_label = None
        self.phone_number_error_label = None
        self.address_error_label = None
        self.email_error_label = None
        self.password_error_label = None

        self.registration_form("Registration form")
        self.first_name_register("First Name")
        self.last_name_register("Last Name")
        self.phone_number_register("Phone Number")
        self.address_register("Address")
        self.email_register("Email")
        self.password_register("Password")

        tk.Button(self.root, text='Submit', width=20, bg='brown', fg='white', command=self.validate_inputs).place(x=180, y=440)

    def registration_form(self, header="Registration form"):
        label = tk.Label(self.root, text=header, width=20, font=("bold", 20))
        label.place(x=90, y=53)

    def first_name_register(self, header="Firstname"):
        label = tk.Label(self.root, text=header, width=20, font=("bold", 10))
        label.place(x=80, y=130)
        self.first_name_entry = tk.Entry(self.root)
        self.first_name_entry.place(x=250, y=130)

    def last_name_register(self, header="Last name"):
        label = tk.Label(self.root, text=header, width=20, font=("bold", 10))
        label.place(x=80, y=180)
        self.last_name_entry = tk.Entry(self.root)
        self.last_name_entry.place(x=250, y=180)

    def phone_number_register(self, header="Phone Number"):
        label = tk.Label(self.root, text=header, width=20, font=("bold", 10))
        label.place(x=80, y=230)
        self.phone_number_entry = tk.Entry(self.root)
        self.phone_number_entry.place(x=250, y=230)

    def address_register(self, header="Address"):
        label = tk.Label(self.root, text=header, width=20, font=("bold", 10))
        label.place(x=80, y=280)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.place(x=250, y=280)

    def email_register(self, header="Email"):
        label = tk.Label(self.root, text=header, width=20, font=("bold", 10))
        label.place(x=80, y=330)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.place(x=250, y=330)

    def password_register(self, header="Password"):
        label = tk.Label(self.root, text=header, width=20, font=("bold", 10))
        label.place(x=80, y=380)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.place(x=250, y=380)

    def validate_inputs(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        phone_number = self.phone_number_entry.get()
        address = self.address_entry.get()
        my_email = self.email_entry.get()
        my_password = self.password_entry.get()

        data = [
            self.first_name_error_label,
            self.last_name_error_label,
            self.phone_number_error_label,
            self.address_error_label,
            self.email_error_label,
            self.password_error_label
        ]

        for error_label in data:
            if error_label:
                error_label.destroy()

        is_valid = True

        # Validate first name
        if not re.match(r"^[A-Z][a-z]{1,50}$", first_name):
            self.first_name_error_label = tk.Label(self.root, text="Invalid first name!", width=20, fg="red")
            self.first_name_error_label.place(x=250, y=150)
            is_valid = False

        # Validate last name
        if not re.match(r"^[A-Z][a-z]{1,50}$", last_name):
            self.last_name_error_label = tk.Label(self.root, text="Invalid last name!", width=20, fg="red")
            self.last_name_error_label.place(x=250, y=200)
            is_valid = False

        # Validate phone number
        if not re.match(r"^\d{10}$", phone_number):
            self.phone_number_error_label = tk.Label(self.root, text="Invalid phone number!", width=20, fg="red")
            self.phone_number_error_label.place(x=250, y=250)
            is_valid = False

        if len(address) < 10:
            self.address_error_label = tk.Label(self.root, text="Invalid address!", width=20, fg="red")
            self.address_error_label.place(x=250, y=300)
            is_valid = False

        # Validate email
        if not re.match(r"^(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]{2,3}){1,2})\b", my_email):
            self.email_error_label = tk.Label(self.root, text="Invalid email!", width=20, fg="red")
            self.email_error_label.place(x=250, y=350)
            is_valid = False

        # Validate password
        if not self.validate_password(my_password):
            is_valid = False

        if is_valid:
            messagebox.showinfo("Success", "Registration Successful!")

        return is_valid

    def validate_password(self, password):
        if self.password_error_label:
            self.password_error_label.destroy()

        possible_errors = [
            (r'.{6,}', "Password must be at least 6 characters long"),
            (r'[A-Z]', "Password must contain at least one uppercase letter"),
            (r'[a-z]', "Password must contain at least one lowercase letter"),
            (r'[0-9]', "Password must contain at least one digit"),
            (r'[@$!%*?&#_]', "Password must contain at least \none special character: @$!%*?&#_")
        ]

        is_valid = True
        for pattern, error_message in possible_errors:
            if not re.search(pattern, password):
                self.password_error_label = tk.Label(self.root, text=error_message, width=50, fg="red")
                self.password_error_label.place(x=150, y=400)
                is_valid = False
                return is_valid
        return is_valid


if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()
    print("Registration form is created successfully...")
  
