from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class Registration:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x750+200+10")
        self.root.configure(bg="#FAEED1")
        self.root.title("REGISTRATION PAGE")

        #database creation
        self.connection = sqlite3.connect("customer.db")
        self.cursor = self.connection.cursor()

        #creating table
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS customers
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            firstname TEXT,
                            lastname TEXT,
                            email TEXT,
                            gender TEXT,
                            address TEXT, 
                            password TEXT,
                            mobile INTEGER,
                            payment_method TEXT)
                            
        ''')

        self.connection.commit()


        self.title_label = Label(self.root, text="Registration Form", bg="#FAEED1",width=18, font=("Arial",20,"bold"))
        self.title_label.place(x=250, y=20)

        self.first_name_label = Label(self.root, text="First Name: ", bg="#FAEED1",width=15, font=("Arial", 13, "bold"))
        self.first_name_label.place(x=100, y=140)

        self.first_name_entry = Entry(self.root, font=("Arial",15,"bold"))
        self.first_name_entry.place(x=310, y=140)

        self.last_name_label = Label(self.root, text="Last Name: ",bg="#FAEED1", width=15, font=("Arial",13,"bold"))
        self.last_name_label.place(x=100, y=180)

        self.last_name_entry = Entry(self.root, font=("Arial",15,"bold"))
        self.last_name_entry.place(x=310, y=180)

        self.email_label = Label(self.root, text="Email: ", bg="#FAEED1",width=15, font=("Arial",13,"bold"))
        self.email_label.place(x=100, y= 220)

        self.email_entry = Entry(self.root, font=("Arial",15,"bold"))
        self.email_entry.place(x=310, y=220)

        self.gender_label = Label(self.root, text="Gender",bg="#FAEED1", width=15, font=("Arial",13,"bold"))
        self.gender_label.place(x=100, y=260)

        self.gender_vars = StringVar()
        self.male_radiobutton = ttk.Radiobutton(self.root, text="Male",variable = self.gender_vars, value="Male")
        self.male_radiobutton.place(x=310, y=260)

        self.female_radiobutton = ttk.Radiobutton(self.root, text="Female", variable=self.gender_vars,
                                                value="Female")
        self.female_radiobutton.place(x=400, y=260)

        self.others_radiobutton = ttk.Radiobutton(self.root, text="Others", variable=self.gender_vars,
                                                value="Others")
        self.others_radiobutton.place(x=500, y=260)

        self.address_label = Label(self.root, text="Address", bg="#FAEED1",width=15, font=("Arial",13,"bold"))
        self.address_label.place(x=100, y=300)

        self.address_entry =  Entry(self.root, font=("Arial",13,"bold"))
        self.address_entry.place(x=310, y=300)

        self.password_label = Label(self.root, text="Password", bg="#FAEED1",width=15, font=("Arial",13,"bold"))
        self.password_label.place(x=100, y=340)

        self.password_entry = Entry(self.root, font=("Arial",13,"bold"), show="*")
        self.password_entry.place(x=310, y=340)

        self.mobile_label = Label(self.root, text="Mobile : ", bg="#FAEED1",width=15, font=("Arial",13,"bold"))
        self.mobile_label.place(x=100, y=380)

        self.mobile_entry = Entry(self.root, font=("Arial",13,"bold"))
        self.mobile_entry.place(x=310, y=380)

        self.payment_label = Label(self.root, text="Payment Method: ", bg="#FAEED1",width=15, font=("Arial",13,"bold"))
        self.payment_label.place(x=100, y=420)

        self.payment_choices = ["Esewa","FonePay","PayPal"]
        self.payment_combobox = ttk.Combobox(self.root, values=self.payment_choices, style="TCombobox")
        self.payment_combobox.place(x=310, y=420)

        self.submit_button = Button(self.root, text="Register", command=self.register, width=15, font=("Arial",15,"bold"))
        self.submit_button.place(x=190, y=470)

        self.cancel_button = Button(self.root, text="Cancel", width=15, font=("Arial",15,"bold"), command=self.cancel_action)
        self.cancel_button.place(x=380, y=470)


    def cancel_action(self):
        from loginpagegui import Login
        self.root.destroy()
        root = Tk()
        Login(root)



    def register(self):
        firstname = self.first_name_entry.get()
        lastname = self.last_name_entry.get()
        email = self.email_entry.get()
        gender = self.gender_vars.get()
        address = self.address_entry.get()
        password = self.password_entry.get()
        mobile = self.mobile_entry.get()
        payment_method = self.payment_combobox.get()

        if not all([firstname, lastname,email,gender,address,password,mobile,payment_method ]):
            messagebox.showerror("Registration Fail","Please fill in all fields")
        else:
            try:
                self.cursor.execute('''INSERT INTO customers (firstname, lastname, email, gender, address, password, mobile,payment_method) VALUES (?,?,?,?,?,?,?,?)
                ''', (firstname, lastname, email, gender, address, password, mobile,payment_method))
            except:
                print('Wrong')

            self.connection.commit()
            messagebox.showinfo("Success","Registration Successfull")
            from loginpagegui import Login
            self.root.destroy()
            root = Tk()
            Login(root)

if __name__ == "__main__":
    root = Tk()
    registration_app  = Registration(root)
    root.mainloop()


