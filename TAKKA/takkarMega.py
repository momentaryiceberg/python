import tkinter as tk
import os
import subprocess
import pyperclip

# Þetta er fyrir context menu-ið
def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

def open_notepad():
    subprocess.run(["notepad.exe"])

def open_calc():
    subprocess.run(["calc.exe"])

def open_personal_folder():
    os.startfile(os.path.expanduser("~"))

def open_shortcut():
    subprocess.run([''])



# Nota þetta þegar kveiki á tölvunni. KeePass, N1 vél, Cisco, Olís vél, outlook, chromeDaglegt-Olíustjórinn
def open_kveikja():
    """
    subprocess.run(['path/to/program.exe'])          - to open an application
    subprocess.run(['explorer', 'path/to/folder'])   - to open a folder
    subprocess.run(['start', 'path/to/file'])        - to open a file with its default application
    """
    enneinn = "nB5J2R7ELX"
    pyperclip.copy(enneinn)

    #subprocess.run(['C:\Users\peturdaniel\Desktop\N1 vél.rdp'])     # N1 vél
    #subprocess.run(['C:\Users\peturdaniel\Desktop\Olís vél.rdp'])   # Olís vél

    # Cisco - "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Cisco\Cisco AnyConnect Secure Mobility Client\Cisco AnyConnect Secure Mobility Client.lnk"
    # Outlook - "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Outlook.lnk"


def run_python():
    folder_path = "C:\\Users\\peturdaniel\\code\\python"
    # þetta keyrir python program
    command = f'cd /d "{folder_path}" && python takkar2_contextMenu.py'

    # Opnar cmd og execute-ar commandið
    subprocess.Popen(command, shell=True)

def open_petur():
    personal_folder = "C:\\Users\\peturdaniel"
    os.system(f'explorer {personal_folder}')





# Create the main application window etc........
app = tk.Tk()
app.title("Pétur Takkaval")

# define buttons
button1 = tk.Button(app, text="Pétur Daníel", foreground="purple", command=open_petur)
button2 = tk.Button(app, text="open shortcut", command=open_shortcut)
button3 = tk.Button(app, text="Button 3")
button4 = tk.Button(app, text="Button 4")
button5 = tk.Button(app, text="Button 5")
button6 = tk.Button(app, text="Button 6")
button7 = tk.Button(app, text="Button 7")
button8 = tk.Button(app, text="Button 8")
button9 = tk.Button(app, text="Button 9")
button10 = tk.Button(app, text="Button 10")





button1.grid(row=0, column=0, padx=10, pady=10)
button2.grid(row=0, column=1, padx=10, pady=10)
button3.grid(row=0, column=2, padx=10, pady=10)
button4.grid(row=1, column=0, padx=10, pady=10)
button5.grid(row=1, column=1, padx=10, pady=10)
button6.grid(row=1, column=2, padx=10, pady=10)
button7.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
button8.grid(row=3, column=0, padx=10, pady=10)
button9.grid(row=3, column=1, padx=10, pady=10)
button10.grid(row=3, column=2, padx=10, pady=10)



# Create a context menu
context_menu = tk.Menu(app, tearoff=0)
context_menu.add_command(label="Glós")
context_menu.add_command(label="Downloads")


# Binds the keyboard shortcut to the function
app.bind("<Control-1>", open_petur)
# Opnar context menu-ið á button 1
button1.bind("<Button-3>", show_context_menu)

# Gerir gluggan "always on top"
#app.attributes("-topmost", True)

app.mainloop()

