import tkinter as tk
import os

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

def open_downloads_folder():
    downloads_folder = os.path.expanduser('~') + '/Downloads'
    os.system(f'explorer {downloads_folder}')

def open_n1():
    custom_folder_path = "S:\\1 ÞJÓNUSTUSVIÐ\\Verkefnastjórn\\1 TÆKNIBORÐ\\N1\\"
    os.system(f'explorer {custom_folder_path}')

# Create the main Tkinter window
root = tk.Tk()
root.title("Button with Context Menu")

# Create three buttons
button1 = tk.Button(root, text="Button 1")
button1.pack(pady=10)

button2 = tk.Button(root, text="Button 2")
button2.pack(pady=10)

button3 = tk.Button(root, text="Tækniborð", foreground="purple")
button3.pack(pady=10)

# Create a context menu
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Option 1", command=open_downloads_folder)
context_menu.add_command(label="1 Tækniborð/N1", command=open_n1)
context_menu.add_command(label="Option 3")

# Attach the context menu to a specific button for left-click
button3.bind("<Button-3>", show_context_menu)

# Start the Tkinter event loop
root.mainloop()
