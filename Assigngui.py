import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class AssignDriver:
    def __init__(self, root):
        self.root = root
        self.root.title("Assign Driver")
        self.root.state("zoomed")
        self.setup_database()

        self.pickup_address_label = tk.Label(self.root, text="Pickup Address:", font=("Times",15))
        self.pickup_address_label.grid(row=0, column=0, padx=20, pady=20)

        self.pick_up_address_entry = tk.Entry(self.root, font=("Times",15))
        self.pick_up_address_entry.grid(row=1, column=0, padx=20, pady=20)

        self.pickup_date_label = tk.Label(self.root, text="Pickup Date:", font=("Times",15))
        self.pickup_date_label.grid(row=0, column=1, padx=20, pady=20)

        self.pick_up_date_entry = tk.Entry(self.root, font=("Times",15))
        self.pick_up_date_entry.grid(row=1, column=1, padx=20, pady=20)

        self.pickup_time_label = tk.Label(self.root, text="Pickup Time:", font=("Times",15))
        self.pickup_time_label.grid(row=0, column=2, padx=20, pady=20)

        self.pick_up_time_entry = tk.Entry(self.root, font=("Times",15))
        self.pick_up_time_entry.grid(row=1, column=2, padx=20, pady=20)

        self.dropoff_address_label = tk.Label(self.root, text="Drop-off Address:", font=("Times", 15))
        self.dropoff_address_label.grid(row=0, column=3, padx=20, pady=20)

        self.dropoff_address_entry = tk.Entry(self.root, font=("Times", 15))
        self.dropoff_address_entry.grid(row=1, column=3, padx=20, pady=20)

        self.id_label = tk.Label(self.root, text="ID:", font=("Times",15))
        self.id_label.grid(row=2, column=0, padx=20, pady=20)

        self.id_entry = tk.Entry(self.root, font=("Times",15))
        self.id_entry.grid(row=2, column=1, padx=20, pady=20)

        self.booking_status_label = tk.Label(self.root, text="Booking Status:", font=("Times",15))
        self.booking_status_label.grid(row=2, column=2, padx=20, pady=20)

        self.booking_status_entry = tk.Entry(self.root,  font=("Times",15))
        self.booking_status_entry.grid(row=2, column=3, padx=20, pady=20)

        self.assign_button = tk.Button(self.root, text="ASSIGN", font=("Times",15), width=10, bg="blue", command=self.update_data)
        self.assign_button.grid(row=10, column=3, padx=20, pady=20)

        columns = ("BookingID", "Pickup Address", "Pickup Date", "Pickup Time", "Drop-off Address", "ID", "Booking Status")
        self.booking_tree = ttk.Treeview(self.root, columns=columns)
        self.booking_tree.heading("#0", text="BookingID")
        self.booking_tree.heading("#1", text="Pickup Address")
        self.booking_tree.heading("#2", text="Pickup Date")
        self.booking_tree.heading("#3", text="Pickup Time")
        self.booking_tree.heading("#4", text="Drop_off Address")
        self.booking_tree.heading("#5", text="ID")
        self.booking_tree.heading("#6", text="booking_status")
        self.booking_tree.grid(row=4, column=0, columnspan=4, padx=20, pady=20)

        for col in columns:
            self.booking_tree.heading(col, text=col)
            self.booking_tree.column(col, width=185, anchor="center")
        
        self.booking_tree.bind("<ButtonRelease-1>", self.on_tree_select)
        self.view_table()

    def setup_database(self):
        self.conn = sqlite3.connect("customer.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS booking (
                booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                pickup_address TEXT,
                pickup_date TEXT,
                pickup_time TEXT,
                drop_address TEXT,
                id TEXT,
                booking_status TEXT
            )
        ''')

        self.cursor.execute('''
            PRAGMA table_info(booking)
        ''')
        columns = [column[1] for column in self.cursor.fetchall()]
        if 'id' not in columns:
            self.cursor.execute('''
                ALTER TABLE booking
                ADD COLUMN id TEXT
            ''')

        self.conn.commit()

    def on_tree_select(self, event):
        selected_item = self.booking_tree.selection()
        if not selected_item:
            return
        values = self.booking_tree.item(selected_item, "values")
        self.pick_up_address_entry.delete(0, tk.END)
        self.pick_up_address_entry.insert(0, values[1])
        self.pick_up_date_entry.delete(0, tk.END)
        self.pick_up_date_entry.insert(0, values[3])
        self.pick_up_time_entry.delete(0, tk.END)
        self.pick_up_time_entry.insert(0, values[2])
        self.dropoff_address_entry.delete(0, tk.END)
        self.dropoff_address_entry.insert(0, values[4])
        self.id_entry.delete(0, tk.END)
        self.id_entry.insert(0, values[5])
        self.booking_status_entry.delete(0, tk.END)
        self.booking_status_entry.insert(0, values[6])

    def view_table(self):
        for item in self.booking_tree.get_children():
            self.booking_tree.delete(item)
        self.cursor.execute("SELECT booking_id, pickup_address, pickup_date, pickup_time, drop_address, id, booking_status FROM booking")
        rows = self.cursor.fetchall()
        for row in rows:
            self.booking_tree.insert("", "end", values=row)

    def update_data(self):
        selected_item = self.booking_tree.selection()
        selected_id = self.booking_tree.item(selected_item, "values")[0]
        id_value = self.id_entry.get()

        self.cursor.execute('''
            UPDATE booking
            SET id=?
            WHERE booking_id=?
        ''', (id_value, selected_id))
        self.conn.commit()
        messagebox.showinfo("Success", "ID assigned successfully")
        
        self.view_table()

    def update_data(self):
        # Update data in the "booking" table
        selected_item = self.booking_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a row.")
            return

        selected_id = self.booking_tree.item(selected_item, "values")[0]
        booking_status = "Assigned"  # Set the desired booking status here

        self.cursor.execute('''
            UPDATE booking
            SET booking_status=?
            WHERE booking_id=?
        ''', (booking_status, selected_id))
        self.root.destroy()

        self.conn.commit()
        messagebox.showinfo("Success", f"Booking status updated to {booking_status}")
        
        self.view_table()

if __name__ == "__main__":
    root = tk.Tk()
    AssignDriver(root)
    
    root.mainloop()
