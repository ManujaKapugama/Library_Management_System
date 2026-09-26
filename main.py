import tkinter as tk
from tkinter import messagebox
import pywinstyles
import sqlite3

connection = sqlite3.connect("library.db")


class LibraryManagementSystem(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("LibraryMate - The Library Management System")
        Icon = tk.PhotoImage(file="Logo.png")
        self.iconphoto(False, Icon)
        self.geometry("800x500")
        self.resizable(False, False)
        self.config(bg="#000000")
        pywinstyles.apply_style(self,'dark')

        # Container for all frames
        container = tk.Frame(self,bg='black')
        container.pack(fill="both", expand=True)

        # Create frames
        self.frame1 = LoginFrame(container, self)
        self.frame2 = DashboardFrame(container, self)

        self.frame1.grid(row=0, column=0, sticky="nsew")
        self.frame2.grid(row=0, column=0, sticky="nsew")

        # Show Login Frame first
        self.show_frame(self.frame1)

    def show_frame(self, frame):
        frame.tkraise()


class LoginFrame(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg="black")
        self.controller = controller

        self.controller = controller

        # Username
        tk.Label(self, text="Username").pack(pady=(100, 5))

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        # Password
        tk.Label(self, text="Password").pack(pady=(10, 5))

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        # Login Button
        tk.Button(
            self,
            text="Login",
            command=self.login
        ).pack(pady=20)

    def login(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin":

            # Navigate to Frame 2
            self.controller.show_frame(self.controller.frame2)

        else:
            messagebox.showerror(
                "Login Failed",
                "Invalid username or password"
            )


class DashboardFrame(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg="black")
        self.controller = controller

        tk.Label(
            self,
            text="LibraryMate - The Library Management System",
            font=("Arial", 24)
        ).pack(pady=100)

        tk.Label(
            self,
            text="Welcome to Admin Dashboard",
            font=("Arial", 16)
        ).pack()


# Start application
app = LibraryManagementSystem()
app.mainloop()