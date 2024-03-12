import tkinter as tk
import webbrowser

class LinkOpenerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Link Opener")
        self.root.geometry("300x100")

        self.link1 = ""  # Replace with your first link
        self.link2 = ""  # Replace with your second link

        self.create_widgets()

    def create_widgets(self):
        self.button1 = tk.Button(self.root, text="", command=lambda: self.open_link(self.link1))
        self.button1.pack(pady=10)

        self.button2 = tk.Button(self.root, text="", command=lambda: self.open_link(self.link2))
        self.button2.pack(pady=10)

    def open_link(self, link):
        webbrowser.open_new_tab(link)

if __name__ == "__main__":
    root = tk.Tk()
    app = LinkOpenerApp(root)
    root.mainloop()
