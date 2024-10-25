import tkinter as tk
from tkinter import ttk, messagebox

class DriverDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Driver Dashboard")
        self.root.geometry("800x600+400+100")
        self.root.resizable(False, False)

        # Set colorful background
        self.root.configure(bg="#9AD0C2")

        # Heading label with a different color
        self.heading_label = tk.Label(root, text="Driver Dashboard", font=("Arial", 20, "bold"), background="#93B1A6", foreground="black")
        self.heading_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Table to display assigned trips
        self.trips_table_columns = ["Booking_id", "Pickup Address", "pickup date", "pickuptime", "Drop Address", "Driver_id"]
        self.trips_table = ttk.Treeview(root, columns=self.trips_table_columns, show="headings", height=5)
        self.view_table()

        for col in self.trips_table_columns:
            self.trips_table.heading(col, text=col)
            self.trips_table.column(col, width=120)

        self.trips_table.grid(row=1, column=0, padx=15, pady=60, sticky="nsew")

        # Button to mark trip as completed with a colorful background
        self.complete_trip_button = tk.Button(root, text="CLOSE", command=self.logout, fg="Blue", bg="#3498db", font=("Arial", 15, "bold"))
        self.complete_trip_button.grid(row=2, column=0, padx=80, pady=20, sticky="e")

        # Sample Data (you can replace this with your actual data)
        # sample_trip_data = [
        #     (1, "Bardiya", "Work", "2023-02-02 09:00:00", "Assigned"),
        #     (2, "Kathmandu", "Home", "2023-02-02 14:30:00", "In Progress"),
        #     # Add more trip data as needed
        # ]


        # for data in sample_trip_data:
    def view_table(self):
    # Clear existing data in the tree
        for item in self.trips_table.get_children():
         self.trips_table.delete(item)

    # Fetch data from the "booking" table and display in the tree view
    # Assuming you have a database connection and cursor set up, you can modify this part accordingly
    # For example, if you are using SQLite:
        import sqlite3
        conn = sqlite3.connect('customer.db')
        self.cursor = conn.cursor()

        self.cursor.execute("SELECT booking_id, pickup_address, pickup_date, pickup_time, drop_address, driverid FROM booking")
        rows = self.cursor.fetchall()
        for row in rows:
         self.trips_table.insert("", "end", values=row)

    def logout(self):
        result = messagebox.askquestion("Logout", "Are you sure you want to logout?")
        if result == "yes":
            from loginpagegui import Login
            self.root.destroy()
            login_window = tk.Tk()  
            login_instance = Login(login_window)  
            login_window.mainloop()
        # You can implement your completion logic here

if __name__ == "__main__":
    root = tk.Tk()
    app = DriverDashboard(root)
    root.mainloop()
