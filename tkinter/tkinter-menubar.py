import tkinter as tk

def new_file_clicked(event=None):
    print("The New File menu was clicked")

root = tk.Tk()
root.title("Menubar in Tk")
root.geometry("400x300")

# Create a menubar
menubar = tk.Menu()
# Create the first menu
file_menu = tk.Menu(menubar, tearoff=False)
# add commands
file_menu.add_command(label="Njú", accelerator="Ctrl+N", command=new_file_clicked)





# Bind the Ctrl+N shortcut to the "new_file_clicked()" function
root.bind_all("<Control-n>", new_file_clicked)
# Make sure the shortcut works with the CapsLock on
root.bind

# Append the menu to the menubar
menubar.add_cascade(menu=file_menu, label="Fæl")
# Insert the menubar in the main window
root.config(menu=menubar)
root.mainloop()