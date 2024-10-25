import tkinter as tk
from tkinter import ttk, messagebox
from Assigngui import AssignDriver
from DriverRegistration import DriverRegistrationGUI

class AdminDashboard:

    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard")
        self.root.geometry("1000x700+200+50")

        self.top_frame = tk.Frame(self.root, width=1000, height=80, bg="blue")
        self.top_frame.pack(side="top")

        self.top_title = tk.Label(self.top_frame, text="Admin Dashboard", font=("Times", 20))
        self.top_title.place(x=400, y=20)

        self.bottom_frame = tk.Frame(self.root, width=1000, height=600, bg="yellow")
        self.bottom_frame.pack(side="bottom", fill="x", expand=True)

        self.add_driver_button = tk.Button(self.bottom_frame, text="Add Driver", command=self.register_driver,
                                           font=("Times", 20))
        self.add_driver_button.place(x=30, y=100)

        self.assign_driver_button = tk.Button(self.bottom_frame, text="Assign Driver", command=self.open_assign_driver,
                                              font=("Times", 20))
        self.assign_driver_button.place(x=30, y=180)

        # Uncomment these lines if needed
        # self.driver_management_button = tk.Button(self.bottom_frame, text="Driver Management", font=("Times", 20))
        # self.driver_management_button.place(x=30, y=260)

        # self.payment_button = tk.Button(self.bottom_frame, text="Payment", font=("Times", 20))
        # self.payment_button.place(x=30, y=340)

        self.logout_button = tk.Button(self.bottom_frame, text="Logout", command=self.logout, font=("Times", 20))
        self.logout_button.place(x=30, y=420)

    def register_driver(self):
        add_driver = tk.Toplevel(self.root)
        DriverRegistrationGUI(add_driver)

    def open_assign_driver(self):
        assign_driver = tk.Toplevel(self.root)
        AssignDriver(assign_driver)
        

    def logout(self):
        result = messagebox.askquestion("Logout", "Are you sure you want to logout?")
        if result == "yes":
            from loginpagegui import Login
            self.root.destroy()
            login_window = tk.Tk()
            login_instance = Login(login_window)
            login_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    AdminDashboard(root)
    root.mainloop()
    self.root.destroy()
    
