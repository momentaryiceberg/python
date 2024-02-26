import sqlite3
import tkinter as tk
from tkinter import ttk
import datetime

def display_data():
    disp = tk.Toplevel(root)

    # Create a Treeview widget
    tree = ttk.Treeview(disp, columns=('Dags', 'Haus', 'Erindi'))

    # Define the column headings
    tree.heading('#0', text='ID')
    tree.heading('#1', text='Dags/Tími')
    tree.heading('#2', text='Haus')
    tree.heading('#3', text='Erindi')

    # Display the Treeview widget
    tree.pack()


    # Connect to the SQLite3 database
    conn = sqlite3.connect('petur.db')
    cursor = conn.cursor()

    # Execute a SELECT query
    cursor.execute('SELECT * FROM vinna')

    # Fetch all the results
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    # Display the results in a Treeview widget
    for row in rows:
        tree.insert('', 'end', values=row)



def setja_inn_row():
    conn = sqlite3.connect('petur.db')
    cursor = conn.cursor()

    cursor.execute(f'''INSERT INTO vinna VALUES ("{current_date + " " + current_time}", "{haus_var.get()}", "{erindi_var.get()}")''')
    conn.commit()
    conn.close()

    haus_var.set('')
    erindi_var.set('')


current_date = datetime.date.today().strftime("%Y-%d-%m")
current_time = datetime.datetime.now().time().strftime("%H:%M")



root = tk.Tk()
root.title("Vinnu-DB")


haus_var = tk.StringVar()
erindi_var = tk.StringVar()

haus_label = tk.Label(root, text="Haus", padx=5, pady=5)
haus_entry = tk.Entry(root, textvariable=haus_var)

erindi_label = tk.Label(root, text="Erindi", padx=5, pady=5)
erindi_entry = tk.Entry(root, textvariable=erindi_var)

save_button = tk.Button(root, text="Seif", command=setja_inn_row, padx=10)

haus_label.grid(row=1, column=0)
haus_entry.grid(row=1, column=1)
erindi_label.grid(row=2, column=0)
erindi_entry.grid(row=2, column=1)
save_button.grid(row=3, column=1, padx=5, pady=5)


syna_takki = tk.Button(root, text="Sjá allt", command=display_data)
syna_takki.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()