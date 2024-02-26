import tkinter as tk
from tkinter import ttk

class TreeView(tk.Frame):
    def __init__(self, master=None, columns=None, data=None):
        super().__init__(master)
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.pack(fill="both", expand=True)

    





        # Insert data into the tree
        if data:
            for key, value in data.items():
                self.tree.insert("", "end", values=(key, value))

# Create a dictionary
data = {
    "Name": "John Doe",
    "Age": 30,
    "City": "New York"
}

# Create a Tkinter root window
root = tk.Tk()
root.title("Treeview Example")

# Create a TreeView widget
tree_view = TreeView(root, columns=("Key", "Value"), data=data)
tree_view.pack(fill="both", expand=True)

# Start the Tkinter event loop
root.mainloop()