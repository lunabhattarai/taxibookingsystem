# import tkinter as tk
# from tkinter import messagebox
# import sqlite3

# class DriverRegistrationGUI():

#     def __init__(self, root):
#         self.root = root
#         self.root.title("Driver Registration")
#         self.root.geometry("1000x500+200+100")

#         self.connection = sqlite3.connect("customer.db")
#         self.cursor = self.connection.cursor()

#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS drivers (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             mobile INTEGER,
#             address TEXT,
#             email TEXT,
#             license_no INTEGER,
#             password TEXT,
#             driver_availability TEXT

#         )''')

#         self.connection.commit()
        

#         self.name_label = tk.Label(self.root, text="Name", font=("Times", 15))
#         self.name_label.grid(row=0, column=0, padx=100, pady=30)

#         self.name_entry = tk.Entry(self.root, font=("Times", 15))
#         self.name_entry.grid(row=0, column=1)

#         self.mobile_label = tk.Label(self.root, text="Mobile", font=("Times", 15))
#         self.mobile_label.grid(row=1, column=0, padx=20, pady=30)

#         self.mobile_entry = tk.Entry(self.root, font=("Times", 15))
#         self.mobile_entry.grid(row=1, column=1)

#         self.address_label = tk.Label(self.root, text="Address", font=("Times", 15))
#         self.address_label.grid(row=2, column=0, padx=20, pady=30)

#         self.address_entry = tk.Entry(self.root, font=("Times", 15))
#         self.address_entry.grid(row=2, column=1)

#         self.licenseno_label = tk.Label(self.root, text="License No", font=("Times", 15))
#         self.licenseno_label.grid(row=2, column=4, padx=20, pady=30)

#         self.licenseno_entry = tk.Entry(self.root, font=("Times", 15))
#         self.licenseno_entry.grid(row=2, column=5)

#         self.email_label = tk.Label(self.root, text="Email", font=("Times",15))
#         self.email_label.grid(row=0, column=4, padx=30, pady=10)

#         self.email_entry = tk.Entry(self.root, font=("Times", 15))
#         self.email_entry.grid(row=0, column=5)

#         self.password_label = tk.Label(self.root, text="Password", font=("Times",15))
#         self.password_label.grid(row=1, column=4,padx=30, pady=10)

#         self.password_entry = tk.Entry(self.root, font=("Times", 15))
#         self.password_entry.grid(row=1, column=5)

#         self.register_btn = tk.Button(self.root, text="ADD", font=("Times", 20), bg="blue",command=self.register)
#         self.register_btn.grid(row=6, column=2)

#     def register(self):
#         name = self.name_entry.get()
#         mobile = self.mobile_entry.get()
#         address = self.address_entry.get()
#         email = self.email_entry.get()
#         password = self.password_entry.get()
#         license = self.licenseno_entry.get()

#         if not all([name, mobile, address, email, password, license]):
#             messagebox.showerror("Registration Fail","Please fill in all fields")

#         else:
#             try:
#                 self.cursor.execute('''INSERT INTO drivers (name,mobile,address,email,password,license_no, driver_availability = 'Available') VALUES (?,?,?,?,?,?,?)''', (name,mobile,address,email,password,license))
#             except:
#                 print("Error")

#             self.connection.commit()
#             messagebox.showinfo("Success","Driver registered successfully")



# if __name__ == "__main__":
#     root = tk.Tk()
#     DriverRegistrationGUI(root)
#     root.mainloop()

import tkinter as tk
from tkinter import messagebox
import sqlite3

class DriverRegistrationGUI():

    def __init__(self, root):
        self.root = root
        self.root.title("Driver Registration")
        self.root.geometry("1000x500+200+100")

        self.connection = sqlite3.connect("customer.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS drivers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            mobile INTEGER,
            address TEXT,
            email TEXT,
            license_no INTEGER,
            password TEXT,
            driver_availability TEXT
        )''')

        self.name_label = tk.Label(self.root, text="Name", font=("Times", 15))
        self.name_label.grid(row=0, column=0, padx=100, pady=30)

        self.name_entry = tk.Entry(self.root, font=("Times", 15))
        self.name_entry.grid(row=0, column=1)

        self.mobile_label = tk.Label(self.root, text="Mobile", font=("Times", 15))
        self.mobile_label.grid(row=1, column=0, padx=20, pady=30)

        self.mobile_entry = tk.Entry(self.root, font=("Times", 15))
        self.mobile_entry.grid(row=1, column=1)

        self.address_label = tk.Label(self.root, text="Address", font=("Times", 15))
        self.address_label.grid(row=2, column=0, padx=20, pady=30)

        self.address_entry = tk.Entry(self.root, font=("Times", 15))
        self.address_entry.grid(row=2, column=1)

        self.licenseno_label = tk.Label(self.root, text="License No", font=("Times", 15))
        self.licenseno_label.grid(row=2, column=4, padx=20, pady=30)

        self.licenseno_entry = tk.Entry(self.root, font=("Times", 15))
        self.licenseno_entry.grid(row=2, column=5)

        self.email_label = tk.Label(self.root, text="Email", font=("Times", 15))
        self.email_label.grid(row=0, column=4, padx=30, pady=10)

        self.email_entry = tk.Entry(self.root, font=("Times", 15))
        self.email_entry.grid(row=0, column=5)

        self.password_label = tk.Label(self.root, text="Password", font=("Times", 15))
        self.password_label.grid(row=1, column=4, padx=30, pady=10)

        self.password_entry = tk.Entry(self.root, font=("Times", 15))
        self.password_entry.grid(row=1, column=5)

        self.register_btn = tk.Button(self.root, text="ADD", font=("Times", 20), bg="blue",     command=self.register)
        self.register_btn.grid(row=6, column=2)

    def register(self):
        name = self.name_entry.get()
        mobile = self.mobile_entry.get()
        address = self.address_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        license = self.licenseno_entry.get()

        if not all([name, mobile, address, email, password, license]):
            messagebox.showerror("Registration Fail", "Please fill in all fields")
        else:
            try:
                self.cursor.execute('''INSERT INTO drivers (name, mobile, address, email, password, license_no, driver_availability)
                                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (name, mobile, address, email, password, license, 'Available'))
            except sqlite3.Error as e:
                print("Error:", e)

            self.connection.commit()
            messagebox.showinfo("Success", "Driver registered successfully")

if __name__ == "__main__":
    root = tk.Tk()
    DriverRegistrationGUI(root)
    root.mainloop()
