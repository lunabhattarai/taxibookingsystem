import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from tkcalendar import DateEntry

class CustomerDashboard:

    def __init__(self, root):
        self.root = root
        self.root.title("Customer Window")
        self.root.geometry("1200x800+130+2")
        self.root.resizable(False, False)

        self.Create_leftTop_frame()
        self.Create_left_frame()
        self.setup_database()
        self.view_table()

    def setup_database(self):
        # Connect to the SQLite database
        self.conn = sqlite3.connect("customer.db")
        self.cursor = self.conn.cursor()

        # Create the "booking" table if not exists
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS booking (
                booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                pickup_address TEXT,
                pickup_date TEXT,
                pickup_time TEXT,
                drop_address TEXT,
                booking_status TEXT
            )
        ''')
        self.conn.commit()

    def update_data(self, booking_id, pickup_address, pickup_date, pickup_time, drop_address):
        # Update all text fields except "booking_status" in the "booking" table
        self.cursor.execute('''
            UPDATE booking
            SET pickup_address=?, pickup_date=?, pickup_time=?, drop_address=?
            WHERE booking_id=?
        ''', (pickup_address, pickup_date, pickup_time, drop_address, booking_id))
        self.conn.commit()

    def insert_data(self, pickup_address, pickup_date, pickup_time, drop_address):
        # Insert data into the "booking" table
        self.cursor.execute('''
            INSERT INTO booking (pickup_address, pickup_date, pickup_time, drop_address, booking_status)
            VALUES (?, ?, ?, ?, 'Booked')
        ''', (pickup_address, pickup_date, pickup_time, drop_address))
        self.conn.commit()

    def delete_data(self, booking_id):
        # Delete data from the "booking" table
        self.cursor.execute('''
            DELETE FROM booking
            WHERE booking_id=?
        ''', (booking_id,))
        self.conn.commit()

    def Create_leftTop_frame(self):
        leftTop_frame = tk.Frame(self.root, bg="#93B1A6", width=1200, height=300)
        leftTop_frame.place(x=0, y=0)

        pickup_label = tk.Label(leftTop_frame, text="PickUp Address:", font=("Helvetica", 18, "bold"), bg="#93B1A6", fg="black")
        pickup_label.place(x=50, y=40)
        self.entry_pickup = tk.Entry(leftTop_frame,  font=("Helvetica", 18, "bold"))
        self.entry_pickup.place(x=270, y=40)

        date_label = tk.Label(leftTop_frame, text="PickUp Date:", font=("Helvetica", 18, "bold"), bg="#93B1A6",
                                fg="black")
        date_label.place(x=50, y=100)
        self.entry_date = DateEntry(leftTop_frame, font=("Helvetica", 18, "bold"))
        self.entry_date.place(x=270, y=100)

        time_label = tk.Label(leftTop_frame, text="PickUp Time:", font=("Helvetica", 18, "bold"), bg="#93B1A6",
                                fg="black")
        time_label.place(x=50, y=160)
        self.entry_time = tk.Entry(leftTop_frame, font=("Helvetica", 18, "bold"))
        self.entry_time.place(x=270, y=160)

        drop_label = tk.Label(leftTop_frame, text="Drop Address:", font=("Helvetica", 18, "bold"), bg="#93B1A6",
                                fg="black")
        drop_label.place(x=50, y=220)
        self.entry_drop = tk.Entry(leftTop_frame, font=("Helvetica", 18, "bold"))
        self.entry_drop.place(x=270, y=220)

        button_book = tk.Button(leftTop_frame, text="Book Trip", bg="#0E8388", width=15, fg="white",
                                font=("Arial", 15, "bold"), command=self.book_trip, pady=6)
        button_book.place(x=900, y=30)

        button_update = tk.Button(leftTop_frame, text="Update Trip", width=15, pady=6, font=("Arial", 15, "bold"),
                                  bg="#0E8388", fg="white", command=self.update_trip)
        button_update.place(x=900, y=130)

        button_cancel = tk.Button(leftTop_frame, text="Cancel Trip", width=15, pady=6, font=("Arial", 15, "bold"),
                                  bg="#0E8388", fg="white", command=self.cancel_trip)
        button_cancel.place(x=900, y=230)

    def Create_left_frame(self):
        self.left_frame = tk.Frame(self.root, bg="#B9B4C7", width=1200, height=500)
        self.left_frame.place(x=0, y=300)

        columns = (
            "Booking ID", "Pickup Address", "Pickup Time", "Pickup Date",
            "Drop Address", "booking_status",
        )

        self.tree = ttk.Treeview(self.left_frame, columns=columns, show="headings", height=17)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=180, anchor="center")
        self.tree.place(x=50, y=0)
        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)  # Bind the selection event

        logout_view = tk.Button(self.left_frame, text="Logout", bg="#0E8388", width=15, fg="white",
                            font=("Arial", 15, "bold"),  pady=5, command=self.logout)
        logout_view.place(x=500, y=400)  # Adjust the y-coordinate according to your layout

    def logout(self):
        result = messagebox.askquestion("Logout", "Are you sure you want to logout?")
        if result == "yes":
            from loginpagegui import Login
            self.root.destroy()
            login_window = tk.Tk()  
            login_instance = Login(login_window)  
            login_window.mainloop()

    def book_trip(self):
        # Get values from entry fields
        pickup_address = self.entry_pickup.get()
        pickup_date = self.entry_date.get()
        pickup_time = self.entry_time.get()
        drop_address = self.entry_drop.get()

        # Insert data into the database
        self.insert_data(pickup_address, pickup_date, pickup_time, drop_address)

        # Update the tree view
        self.view_table()

        # Show a success message box
        messagebox.showinfo("Success", "Your booking is successful!")

    def update_trip(self):
        # Get values from entry fields
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("Warning", "Please select a row to update.")
            return

        pickup_address = self.entry_pickup.get()
        pickup_date = self.entry_date.get()
        pickup_time = self.entry_time.get()
        drop_address = self.entry_drop.get()
        booking_id = self.tree.item(selected_item, "values")[0]

        # Update data in the database
        self.update_data(booking_id, pickup_address, pickup_date, pickup_time, drop_address)

        self.view_table()

        # Show a success message box
        messagebox.showinfo("Success", "Booking updated successfully!")

    def cancel_trip(self):
        # Get the selected item
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("Warning", "Please select a row to cancel.")
            return

        # Get booking ID from the selected item
        booking_id = self.tree.item(selected_item, "values")[0]
        self.delete_data(booking_id)
        self.view_table()

        # Show a success message box
        messagebox.showinfo("Success", "Booking canceled successfully!")

    def on_tree_select(self, event):
        # Get the selected item
        selected_item = self.tree.selection()

        if not selected_item:
            return

        # Get values from the selected item and populate the entry fields
        values = self.tree.item(selected_item, "values")
        self.entry_pickup.delete(0, tk.END)
        self.entry_pickup.insert(0, values[1])

        self.entry_date.delete(0, tk.END)
        self.entry_date.insert(0, values[3])

        self.entry_time.delete(0, tk.END)
        self.entry_time.insert(0, values[2])

        self.entry_drop.delete(0, tk.END)
        self.entry_drop.insert(0, values[4])

    def view_table(self):
        # Clear existing data in the tree
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch data from the "booking" table and display in the tree view
        self.cursor.execute("SELECT * FROM booking")
        rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert("", "end", values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomerDashboard(root)
    root.mainloop()
