import tkinter as tk

def submit():
    name_var.set('')
    email_var.set('')
    phone_var.set('')
    name_entry.focus_set()


root = tk.Tk()
root.title("Entry form in frame")

# Create a frame
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

name_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()

tk.Label(frame, text="Nafn: ").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(frame, textvariable=name_var)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Email : ").grid(row=1, column=0, sticky="w")
email_entry = tk.Entry(frame, textvariable=email_var)
email_entry.grid(row=1, column=1)

tk.Label(frame, text="Phone: ").grid(row=2, column=0, sticky="w")
phone_entry = tk.Entry(frame, textvariable=phone_var)
phone_entry.grid(row=2, column=1)

submit_button = tk.Button(frame, text="Submit")
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# setur focus á name entry-ið
name_entry.focus_set()

# Enter submittar
root.bind("<Return>", lambda event: submit())

root.mainloop()
