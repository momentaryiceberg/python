import tkinter as tk
import webbrowser

class BrowserOpenerApp:
    def __init__(self, master):
        self.master = master
        master.title("Browser Opener")

        # Button to open link in Edge
        self.edge_button = tk.Button(master, text="Open in Edge", command=self.open_in_edge)
        self.edge_button.pack(pady=10)

        # Button to open link in Chrome
        self.chrome_button = tk.Button(master, text="Open in Chrome", command=self.open_in_chrome)
        self.chrome_button.pack(pady=10)

    def open_in_edge(self):
        url = "https://www.example.com"  # Replace with your Edge URL
        webbrowser.get("microsoft-edge").open(url)

    def open_in_chrome(self):
        url = "https://www.example.com"  # Replace with your Chrome URL
        webbrowser.get("google-chrome").open(url)

if __name__ == "__main__":
    root = tk.Tk()
    app = BrowserOpenerApp(root)
    root.mainloop()
