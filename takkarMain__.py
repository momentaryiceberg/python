import tkinter as tk
import os
import subprocess

# Context menu
def show_context_menu1(event):
    context_menu1.post(event.x_root, event.y_root)

def show_context_menu2(event):
    context_menu2.post(event.x_root, event.y_root)

def openPersonal():
    personal_folder = "C:\\Users\\peturdaniel\\"
    os.system(f"explorer {personal_folder}")

def openODR():
    odr_folder = "S:\\1 ÞJÓNUSTUSVIÐ\\"
    os.system(f"explorer {odr_folder}")

def openDownloads():
    downloads_folder = "C:\\Users\\peturdaniel\\Downloads"
    os.system(f'explorer {downloads_folder}')

def openN1():
    custom_folder_path = "S:\\1 ÞJÓNUSTUSVIÐ\\Verkefnastjórn\\1 TÆKNIBORÐ\\N1\\"
    os.system(f'explorer {custom_folder_path}')

root = tk.Tk()
root.title("Aðalval")

packFrame = tk.Frame(root)
packFrame.pack(side=tk.LEFT)

button1 = tk.Button(root, text="Personal Folder", command=openPersonal, foreground="purple")
button1.pack(pady=10, padx=10)

button2 = tk.Button(root, text="ODR Folder", command=openODR, foreground="purple")
button2.pack(pady=10, padx=10)

button3 = tk.Button(root, text="Takki 3")
button3.pack(pady=10, padx=10)



#############################################

button4 = tk.Button(master=root, text="Takki 4")
button4.pack(root, padx=10)

button5 = tk.Button(root, text="Takki 5")
button5.pack(root, padx=10)

# Create a context menu
context_menu1 = tk.Menu(root, tearoff=0)
context_menu1.add_command(label="Downloads", command=openDownloads)
context_menu1.add_command(label="Personal", command=openPersonal)
context_menu1.add_command(label="Option 3")

context_menu2 = tk.Menu(root, tearoff=0)
context_menu2.add_command(label="TÆKNIBORÐ N1", command=openN1)
context_menu2.add_command(label="Option 2")
context_menu2.add_command(label="Option 3")


# Attach the context menu to a specific button for left-click
button1.bind("<Button-3>", show_context_menu1)
button2.bind("<Button-3>", show_context_menu2)


root.mainloop()