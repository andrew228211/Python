from audioop import tomono
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
import tkinter as tk
import sqlite3
#demo
uname="Tuan"
class Group():
    def __init__(self,root):      
        self.root=root
        self.root.title("Add a transaction")
        self.root.geometry("400x300+550+100")
        Label(self.root,text="Add your transaction : ").grid(row=0,column=0,sticky = W, pady = 2)
        v = StringVar()         # for type
        v.set(1)
        name=StringVar()        # for name of expense
        amt=StringVar()
        tg=StringVar()
        typ=StringVar()
        edate=StringVar()
        typ.set("expense")
        def event():
            if v.get()=="1":
                nl.config(text="Name of Expense : ")
                radio1.config(text="Entertainment")
                radio2.config(text="Utilities")
                radio3.config(text="Education")
                radio4.config(text="Others")
                radioVar.set(0)
                typ.set("expense")
            else:
                nl.config(text="Name of Income : ")
                radio1.config(text="Salary")
                radio2.config(text="Bonus")
                radio3.config(text="Gift Income")
                radio4.config(text="Pension")
                radioVar.set(0)
                typ.set("income")
        def update():
            if(radioVar.get()=='1'):
                tg.set(radio1.cget("text"))
            if(radioVar.get()=='2'):
                tg.set(radio2.cget("text"))
            if(radioVar.get()=='3'):
                tg.set(radio3.cget("text"))
            if(radioVar.get()=='4'):
                tg.set(radio4.cget("text"))
            
        Radiobutton(self.root,text="Expense",variable=v,value =1,command=event).grid(row=2,column=0,sticky = W, pady = 2)
        Radiobutton(self.root,text="Income",variable=v,value =2,command=event).grid(row=2,column=3,sticky = W, pady = 2)
        nl=Label(self.root,text="Name of Expense : ")
        nl.grid(row=3,column=0,sticky = W, pady = 2)
        Entry(self.root,textvariable=name).grid(row=3,column=3,sticky = W, pady = 2)
        Label(self.root,text="Amount : ").grid(row=4,column=0,sticky = W, pady = 2)
        Entry(self.root,textvariable=amt).grid(row=4,column=3,sticky = W, pady = 2)
        Label(self.root,text="Date : ").grid(row=5,column=0,sticky = W, pady = 2)
        Entry(self.root,textvariable=edate).grid(row=5,column=3,sticky = W, pady = 2)
        Label(self.root,text="Tags : ").grid(row=6,column=0,sticky = W, pady = 2)
        radioVar = StringVar()
        radioVar.set(0)
        radio1 = Radiobutton(self.root,text = "Entertainment", variable=radioVar,command=update,value=1)
        radio1.grid(row = 6, column = 3, sticky = W,padx=2,pady=2)
        radio2 = Radiobutton(self.root,text = "Utilities", variable=radioVar,command=update,value=2)
        radio2.grid(row = 6, column = 5, sticky = W,padx=2,pady=2)
        radio3 = Radiobutton(self.root,text = "Education", variable=radioVar,command=update,value=3)
        radio3.grid(row = 7, column = 3, sticky = W,padx=2,pady=2)
        radio4 = Radiobutton(self.root,text = "Others", variable = radioVar,command=update,value=4)
        radio4.grid(row = 7, column = 5, sticky = W,padx=2,pady=2)
        def add_to_database():
            try:
                edate="2022/07/11"
                conn=sqlite3.connect("Manage.db")               
                conn.execute("INSERT into Expense(username,item,tag,type,amount,edate) VALUES ('%s','%s','%s','%s','%d','%s');"%(uname,name.get(),tg.get(),typ.get(),int(amt.get()),edate))
                conn.commit()
                Label(self.root,text="Transaction Added", fg="green", font=("calibri", 11)).grid(row=8,column=3,sticky = W, pady = 2)
                self.root.destroy()
            except:                
                Label(self.root,text="Transaction Failed!! Try Again", fg="red", font=("calibri", 11)).grid(row=8,column=3,sticky = W, pady = 2)


        add=Button(self.root, text="Add", width=10, command=add_to_database)
        add.grid(row=8,column=3,sticky = W, pady = 2)
if __name__=="__main__":		
    root=Tk()
    app=Group(root)
    root.mainloop()