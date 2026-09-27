import tkinter as tk
import pywinstyles
from tkinter import ttk, messagebox
import sqlite3

def fetch():
    try:
        conn = sqlite3.connect('library.db')
        curser = conn.cursor()
        query = "SELECT *  FROM library"
        curser.execute(query)
        data = curser.fetchall()
        conn.close()
        return data
    except Exception as e:
        messagebox.showerror("Error", e)

root = tk.Tk()

root.title("LibraryMate - The Library Management System")
Icon = tk.PhotoImage(file="Logo.png")
root.iconphoto(False, Icon)
root.geometry("900x600")
root.resizable(False, False)
root.config(bg="#000000")
pywinstyles.apply_style(root,'dark')

Frame1 = tk.Frame(root,bg='black')
Frame1.place(relwidth=1, relheight=1)

lbl_username = tk.Label(Frame1, text="Username",fg="blue",font=("Arial", 12))
lbl_password = tk.Label(Frame1, text="Password",fg="blue",font=("Arial", 12))
txtb_username = tk.Entry(Frame1)
txtb_password = tk.Entry(Frame1)
lbl_AppHeader = tk.Label(Frame1, text="LibraryMate - The Library Management System",fg="blue",font=("Arial", 16, "bold"))

def login():
    uname = str(txtb_username.get())
    pword = str(txtb_password.get())

    if uname == 'admin' and pword == 'admin':
        print("Login Successful")
        txtb_username.delete(0, tk.END)
        txtb_password.delete(0, tk.END)
        Frame2.tkraise()

    else:
         print("Login Failed")


lbl_AppHeader.place(x=425,y=150,anchor="center")

btn_login = tk.Button(Frame1, text="Login",fg="blue",font=("Arial", 12),command=login)
#btn_login.pack(side='bottom',fill='x',padx=50,pady=10)

#lbl_username.grid(row=0, column=0,padx=5, pady=5)
lbl_username.place(x=350,y=200,anchor="center")

#lbl_password.grid(row=1, column=0,padx=5, pady=5)
lbl_password.place(x=350,y=250,anchor="center")

#txtb_username.grid(row=0, column=1,padx=5, pady=5)
txtb_username.place(x=475,y=200,anchor="center")

#txtb_password.grid(row=1, column=1,padx=5, pady=5)
txtb_password.place(x=475,y=250,anchor='center')

#btn_login.grid(row=2, column=1,padx=5, pady=5
btn_login.place(x=450,y=300, anchor='center')

Frame2 = tk.Frame(root,bg='black')
Frame2.place(relwidth=1, relheight=1)

lbl_AppHeader = tk.Label(Frame2, text="LibraryMate - The Library Management System",fg="blue",font=("Arial", 18, "bold"))
lbl_AppHeader.place(x=425,y=100,anchor="center")

def logout():
    Frame1.tkraise()

btn_AddBooks = tk.Button(Frame2, text="Add Books",fg="blue",font=("Arial", 12))
btn_UpdateBooks = tk.Button(Frame2, text="Update Books",fg="blue",font=("Arial", 12))
btn_DeleteBooks = tk.Button(Frame2, text="Delete Books",fg="blue",font=("Arial", 12))
btn_logout = tk.Button(Frame2, text="logout",fg="blue",font=("Arial", 12),command=logout)

btn_AddBooks.place(x=220,y=500, anchor='center')
btn_UpdateBooks.place(x=350,y=500, anchor='center')
btn_DeleteBooks.place(x=500,y=500, anchor='center')
btn_logout.place(x=650,y=500, anchor='center')

style = ttk.Style()

style.configure(
    "Treeview.Heading",
    background="white",
    foreground="blue",
    font=("Arial", 10, "bold")
)

table = ttk.Treeview(Frame2,columns=('C1','C2','C3','C4'),show='headings')
table.place(relx=0.5, rely=0.5, anchor='center')
table.heading('C1', text='No')
table.heading('C2', text='Book Name')
table.heading('C3', text='Author Name')
table.heading('C4', text='Available Quantity')

table.column('C1',width=250,anchor='center')
table.column('C2',width=250,anchor='center')
table.column('C3',width=150,anchor='center')
table.column('C4',width=150,anchor='center')

try:
    data = fetch()
    for i in data:
        table.insert(parent='', index='end', values=i)
except :
    pass

Frame1.tkraise()
root.mainloop()