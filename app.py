import tkinter as tk
import sqlite3
root = tk.Tk()

def save():
    messagebox.showinfo("Saved", "Data    has been saved ✅")
    conn = sqlite3.connect("student_DB.    db")
    cursor = conn.cursor()
    cur.execute(" CREATE TABLE IF NOT           EXISTS  StudentInformation (id       INTEGER PRIMARY KEY,Surname TEXT, OtherName TEXT,Dept TEXT, Email TEXT,Phone INTEGER, Addr TEXT)")
   

SurnameLabel=tk.Label(root,text= "Surname:", font =("Arial,11")).place(x = 40, y = 100)

SurnameEntry= tk.Entry(root).place(x=40 , y= 160)

DeptLabel= tk.Label(root, text = "Department:", font = ("Arial, 11")).place(x =40, y =240)

DeptEntry= tk.Entry(root).place(x= 40, y= 300)

EmailLabel= tk.Label(root, text = "Email:", font = ("Arial, 11")).place(x =40, y =380)

EmailEntry= tk.Entry(root).place(x= 40, y= 440)

OthLabel= tk.Label(root, text = "Other Names:", font = ("Arial, 11")).place(x =650, y =100)

OthEntry= tk.Entry(root).place(x= 600, y= 160)

PhoneLabel= tk.Label(root, text = "Phone:", font = ("Arial, 11")).place(x =650, y =240)

PhoneEntry= tk.Entry(root).place(x= 600, y= 300)

AddrLabel= tk.Label(root, text = "Address:", font = ("Arial, 11")).place(x =620, y =380)

AddrEntry= tk.Entry(root).place(x= 600, y= 440)

SaveButton= tk.Button(root, text = "Save").place(x =60, y = 520)

def quit():
	root.dispose

ExitButton= tk.Button(root, text = "Exit", command= quit).place(x =650, y = 520)
root.mainloop()