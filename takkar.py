import tkinter as tk
import os
import subprocess

def open_notepad():
    subprocess.run(["notepad.exe"])

def open_personal_folder():
    os.startfile(os.path.expanduser("~"))

def open_cmd():
    pass
    # subprocess.run(["cmd.exe"])

def open_custom_exe():
    # Replace 'path/to/your/program.exe' with the actual path to your .exe file
    subprocess.run(["path/to/your/program.exe"])

def run_command():
    folder_path = "C:\\Users\\peturdaniel\\code\\python"  # Replace with your actual folder path
    command = f'cd /d "{folder_path}" && python takkar2_contextMenu.py'
    
    # Open a command prompt and execute the command
    subprocess.Popen(command, shell=True)

def open_petur():
    personal_folder = "C:\\Users\\peturdaniel"
    os.system(f'explorer {personal_folder}')

# Create the main application window
app = tk.Tk()
app.title("Takkaval")

# Define buttons
button_notepad = tk.Button(app, text="Open Notepad", command=open_notepad)
button_personal_folder = tk.Button(app, text="Open Personal Folder", command=open_personal_folder)
button_cmd = tk.Button(app, text="Open CMD", command=open_cmd)
button_custom_exe = tk.Button(app, text="Open Custom .exe", command=open_custom_exe)
button5 = tk.Button(app, text = "Python script", command=run_command)
button6 = tk.Button(app, text = "peturdaniel", command = open_petur)
button7 = tk.Button(app, text = "Takki 7")


# Arrange buttons in a grid layout
button_notepad.grid(row=0, column=0, padx=10, pady=10)
button_personal_folder.grid(row=0, column=1, padx=10, pady=10)
button_cmd.grid(row=0, column=2, padx=10, pady=10)
button_custom_exe.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
button5.grid(row=2, column=0, padx=10, pady=10)
button6.grid(row=2, column=1, padx=10, pady=10)
button7.grid(row=2, column=2, padx=10, pady=10)

# gerir gluggan "always on top"
app.attributes("-topmost", True)

# Start the Tkinter event loop
app.mainloop()
