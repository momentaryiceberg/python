import tkinter as tk
import webbrowser

# Þetta svínvirkar! Nú þarf bara að hafa þetta ekki root window, heldur glugga sem 
# birtist þegar ýti á takka eða gera hotkey úr öðrum glugga
def open_url(event=None):
    query = entry.get().replace(' ','')
    url = f"https://ja.is/?q={query}"
    webbrowser.open(url)
    root.destroy()

def show_entry():
    entry.pack()
    entry.focus_set()

root = tk.Tk()
root.title("URL opnari")

entry = tk.Entry(root)
entry.bind("<Return>", open_url)

button = tk.Button(root, text="Já.is Númer", command=show_entry)
button.pack()

root.mainloop()