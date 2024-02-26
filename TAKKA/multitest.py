import tkinter as tk

def glugg1():
    tekks = tk.StringVar()
    gluggi = tk.Toplevel(root)
    label1 = tk.Label(gluggi, textvariable=tekks).pack()
    entry1 = tk.Entry(gluggi, textvariable=tekks).pack()

def glugg2():
    

    var = tk.StringVar()
    
    def seiv():
        with open("C:\\Users\\peturdaniel\\code\\python\\TAKKA\\test.txt", "a", encoding="utf-8") as f:
            f.write(f"{var.get()} \n")
        # Núllar/initializer-ar StringVar
        var.set("")
        

    gluggi = tk.Toplevel(root)

    lab_nafn = tk.Label(gluggi, text = "nafn").pack()
    ent_nafn = tk.Entry(gluggi, textvariable=var).pack()

    but_nafn = tk.Button(gluggi, text="Seif", command=seiv).pack()




root = tk.Tk()



glugg1_takki = tk.Button(root, text="Gluggi 1", command=glugg1).pack()

glugg2_takki = tk.Button(root, text="Gluggi 2", command=glugg2).pack()





root.mainloop()