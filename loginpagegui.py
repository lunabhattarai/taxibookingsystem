import tkinter as tk
import sqlite3
from PIL import Image, ImageTk
from customerdashgui import CustomerDashboard
from driverdashgui import DriverDashboard
from Admin import AdminDashboard
from tkinter import messagebox
# import Globalvariable

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x600")
        self.root.resizable(False, False)

        # Load image
        self.image = Image.open(r"C:\Users\LENOVO\Music\Online-Cab-Booking-Image-jpeg.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        image_label = tk.Label(self.root, image=self.photo)
        image_label.place(x=80, y=60)

        # Username entry
        label_username = tk.Label(self.root, text="Email:", font=("Arial", 10, "bold"))
        label_username.place(x=780, y=170)
        self.entry_username = tk.Entry(self.root, font=("Arial", 10, "bold"))
        self.entry_username.place(x=780, y=200)

        # Password entry
        label_password = tk.Label(self.root, text="Password:", font=("Arial", 10, "bold"))
        label_password.place(x=780, y=220)
        self.entry_password = tk.Entry(self.root, font=("Arial", 10, "bold"), show="*")
        self.entry_password.place(x=780, y=250)

        # Login button
        login_button = tk.Button(self.root, text="Login", width=10, command=self.login, font=("Arial", 10, "bold"), bg="yellow")
        login_button.place(x=850, y=430)

        register_button = tk.Button(self.root, text="Register", width=10, command=self.register_fun, font=("Arial", 10, "bold"), bg="yellow")
        register_button.place(x=850, y=470)

        # Database connection
        self.conn = sqlite3.connect("customer.db")
        self.cursor = self.conn.cursor()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "admin" and password == "pass":
            messagebox.showinfo("Welcome", f" Welcome  {self.entry_username.get()} !")
            self.root.destroy()
            root = tk.Tk()
            AdminDashboard(root)
            root.mainloop()
        else:
            try:
                self.cursor.execute("SELECT * FROM tbl_register WHERE email=? AND password=?", (username, password,))
                row = self.cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", " Password or username is incorrect!", parent=self.root)
                else:
                    messagebox.showinfo("Welcome", f" Welcome  {self.entry_username.get()} !")
                    self.root.destroy()
                    root = tk.Tk()
                    CustomerDashboard(root)
                    root.mainloop()
            except Exception as error:
                print(f"{error}")

                # The following code seems incorrect and has been commented out
                # try:
                #     conn = sqlite3.connect("customer.db")
                #     cursor = conn.cursor()
                #     sql_for_customer = "SELECT * FROM tbl_register WHERE email = ? and password = ? "
                #     values = (username, sql_for_customer)
                #     cursor.execute(sql_for_customer, values)
                #     customer = cursor.fetchone()
                #     if customer:
                #         Globalvariable.user_information = customer
                #         messagebox.showinfo("Welcome", f"Welcome {Globalvariable[1]}")
                #         print(Globalvariable.user_information[0])

        # Corrected typo 'destory' to 'destroy'
        self.root.destroy()
        root = tk.Tk()
        CustomerDashboard(root)
        root.mainloop()

        # Close cursor and connection
        self.cursor.close()
        self.conn.close()

    def register_fun(self):
        self.root.destroy()
        from registrationgui import Registration
        root = tk.Tk()
        Registration(root)

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
