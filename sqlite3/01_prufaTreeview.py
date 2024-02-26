import tkinter as tk
from tkinter import ttk
import sqlite3

def display_data():

    # Create a Treeview widget
    tree = ttk.Treeview(root, columns=('Dags', 'Haus', 'Erindi'))

    # Define the column headings
    tree.heading('#0', text='ID')
    tree.heading('#1', text='Column 1')
    tree.heading('#2', text='Column 2')
    tree.heading('#3', text='Column 3')

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

root = tk.Tk()

# Create a button to display the data
button = tk.Button(root, text='Display Data', command=display_data)
button.pack()

root.mainloop()
