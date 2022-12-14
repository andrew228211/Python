import sqlite3
import tkinter as tk
from calendar import Calendar
from datetime import date, datetime
from distutils.cmd import Command
from select import select
from tkinter import *
from tkinter import messagebox, ttk
from turtle import bgcolor, right
from xmlrpc.client import DateTime

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
from tkcalendar import DateEntry

from baocao import Report
# from cuahang import Store
from ngansach import Budget
from sogiaodich import Transaction

uname="Tuan"
nhaptien=0
conn=sqlite3.connect("Manage.db")
class Summary:
    def __init__(self,root):
        #Hinh nen
        self.root=root
        self.root.title("Management")
        self.root.geometry("1600x900+0+0")
        self.bg=ImageTk.PhotoImage(file="image/nen.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)   
        
        #Báo cáo
        
        #---------------------------------------------------------------------------------

        #Khoang trang dọc
        frame= Frame(self.root,bg="black")  
        frame.place(x=0,y=0,width=100,height=1600)
        #Khoang trang tren cung
        # lbltrang=Label(self.root,fg="black",bg="white")
        # lbltrang.place(x=101,y=0,width=1600,height=50)
        lblTen=Label(self.root,text=uname,font=("times new roman",15,"bold"),bg="green")
        lblTen.place(x=280,y=10)
        global nhaptien
        self.sum_income=StringVar()
        cursor = conn.execute("SELECT SUM(amount) FROM Expense WHERE type='income'")
        sum=0
        for r in cursor:
            if r[0] == None:
                 sum +=0
            else:
                sum+=r[0]
        txtTienbanthan=Entry(self.root,font=("times new roman",15,"bold"),textvariable=self.sum_income,fg="black",bg="green")
        txtTienbanthan.place(x=350,y=10,width=100,height=30)
        nhaptien=sum
        self.sum_income.set(str(sum))
        #Tinh nang con:
        Thembtn=Button(self.root,text="THÊM GIAO DỊCH",command=self.Giaodich_windoW,font=("times new roman",15,"bold"),bg="green",fg="white",borderwidth=0)
        Thembtn.place(x=1300,y=10,width=250,height=20)
        Themngansachbtn=Button(self.root,command=self.Ngansach_window,text="THÊM NGÂN SÁCH",font=("times new roman",15,"bold"),bg="green",fg="white",borderwidth=0)       
        # Tính năng thay đổi giao dịch 
        Thaydoibtn=Button(self.root,text="THAY ĐỔI GIAO DỊCH",command=self.Change_window,font=("times new roman",15,"bold"),bg="green",fg="white",borderwidth=0)
        Thaydoibtn.place(x=1300,y=40,width=250,height=20)
        # #Tinh nang 1: Sổ giao dich
        img1=Image.open("image/sogiaodich.webp")
        img1=img1.resize((22,22),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(frame,image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=30,y=80)
        
        Sobtn=Button(self.root,command=lambda:[self.Transaction_windoW(),Thembtn.place(x=1300,y=10,width=200,height=20),Themngansachbtn.place_forget()],text="Giao dịch",font=("times new roman",13,"bold"),bg="black",fg="green",borderwidth=0)
        Sobtn.place(x=2,y=100)
        #Tinh nang 2: Báo cáo
        img2=Image.open("image/baocao.jpg")
        img2=img2.resize((20,20),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(frame,image=self.photoimage2,bg="white",borderwidth=0)
        lblimg2.place(x=30,y=180)
        
        Baocaobtn=Button(self.root,command=self.Report_window,text="Báo cáo",font=("times new roman",13,"bold"),bg="black",fg="green",borderwidth=0)
        Baocaobtn.place(x=9,y=200)
        #Tinh nang 3: Ngân sách
        img3=Image.open("image/Ngansach.png")
        img3=img3.resize((20,20),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(frame,image=self.photoimage3,bg="white",borderwidth=0)
        lblimg3.place(x=30,y=280)
        
        Ngansachbtn=Button(self.root,command=lambda:[self.Budget_window(),Themngansachbtn.place(x=1300,y=10,width=200,height=20),Thembtn.place_forget()],text="Ngân sách",font=("times new roman",13,"bold"),bg="black",fg="green",borderwidth=0)
        Ngansachbtn.place(x=9,y=300)
        #Tinh nang 4: Cửa hàng
        img4=Image.open("image/Cuahang.jpg")
        img4=img4.resize((20,20),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        lblimg4=Label(frame,image=self.photoimage4,bg="white",borderwidth=0)
        lblimg4.place(x=30,y=380)
        
        Cuahangbtn=Button(self.root,text="Cửa hàng",font=("times new roman",13,"bold"),bg="black",fg="green",borderwidth=0)
        Cuahangbtn.place(x=9,y=400)
        #Tinh nang 5: Trợ giúp
        img5=Image.open("image/trogiup.png")
        img5=img5.resize((20,20),Image.ANTIALIAS)
        self.photoimage5=ImageTk.PhotoImage(img5)
        lblimg5=Label(frame,image=self.photoimage5,bg="white",borderwidth=0)
        lblimg5.place(x=30,y=480)
        
        Trogiupbtn=Button(self.root,text="Trợ giúp",font=("times new roman",13,"bold"),bg="black",fg="green",borderwidth=0)
        Trogiupbtn.place(x=9,y=500)
        
    #------------------------------------------------------
        
    #-------------------Giao dịch---------------------------
    def Transaction_windoW(self):
        self.new_window=tk.Toplevel(self.root)
        self.app= Transaction(self.new_window)
    def Giaodich_windoW(self):
        self.new_window=Toplevel(self.root)
        self.app=Group(self.new_window)
    def Change_window(self):
        self.new_window=tk.Toplevel(self.root)
        self.app=Change(self.new_window)
    #------------------Báo cáo------------------------------   
    def Report_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Report(self.new_window)
    #------------------Ngân sách----------------------------
    def Budget_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Budget(self.new_window)
    def Ngansach_window(self):
        self.root2=Toplevel()
        self.root2.title("Thêm ngân sách")
        self.root2.geometry("600x200+500+150")        
    #------------------Cửa hàng-----------------------------
    def Store_window(self):
        self.new_window=Toplevel(self.root)
        #self.app=Store(self.new_window)
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
        Label(self.root,text="Date(yyyy/mm/dd): ").grid(row=5,column=0,sticky = W, pady = 2)
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
                global uname
                conn.execute("INSERT into Expense(username,item,tag,type,amount,edate) VALUES ('%s','%s','%s','%s','%d','%s');"%(uname,name.get(),tg.get(),typ.get(),int(amt.get()),edate.get()))
                conn.commit()
                Label(self.root,text="Transaction Added", fg="green", font=("calibri", 11)).grid(row=8,column=3,sticky = W, pady = 2)
                self.root.destroy()
            except:                
                Label(self.root,text="Transaction Failed!! Try Again", fg="red", font=("calibri", 11)).grid(row=8,column=3,sticky = W, pady = 2)


        add=Button(self.root, text="Add", width=10, command=add_to_database)
        add.grid(row=8,column=3,sticky = W, pady = 2)
class Change(tk.Tk):
    def __init__(self, root):
        self.root=root
        self.root.title("Change a transaction")
        self.root.geometry("600x400+550+100")
        frame = Frame(self.root, bg="gray")
        frame.place(x=0, y=0, width=600, height=400)
        #-----------------Tạo biến lưu----------------------------------------
        self.itemvar=StringVar()
        self.amountvar=StringVar()
        self.datevar=StringVar()
        select_rowid=0
        #----------------------------Tạo hàm Clear-----------------------------------
        def clearEntry():
            txt_name.delete(0, 'end')
            txt_amont.delete(0,'end')
            txt_date.delete(0,'end')
        #----------------------------------------------------------------------------
        #------------------Tạo Fetch-------------------------------------------------
        def fetch():
            cursor = conn.execute("SELECT rowid,item,amount,edate FROM Expense")
            for i in cursor:
                self.tree.insert(parent='',index='0',values=i)
        #------------------------Tạo total-------------------------------------------
        global nhaptien
        def total():
            curson = conn.execute("SELECT SUM(amount) FROM Expense WHERE type='expense'")
            for i in curson:
                for j in i:
                    print(j)
                    messagebox.showinfo('Current Balance: ', f"Total Expense: ' {j} \nBalance Remaining: {nhaptien - j}",parent=self.root)
        #----------------------Tạo Select in TreeView--------------------------------
        def select_record(event):
            global select_rowid
            selected = self.tree.focus()    
            val = self.tree.item(selected, 'values')
            try:
                select_rowid = val[0]
                self.itemvar.set(val[1])
                self.amountvar.set(val[2])
                self.datevar.set(val[3])
            except Exception as ep:
                pass
        #---------------------Tạo Repair---------------------------------------------
        def repair():
            global select_rowid
            selected=self.tree.focus()
            try:
                conn.execute("UPDATE Expense SET item=?, amount=?,edate=? WHERE rowid = ?",(self.itemvar.get(),self.amountvar.get(),self.datevar.get(),select_rowid))             
                self.tree.item(selected, text="", values=(select_rowid,self.itemvar.get(), self.amountvar.get(), self.datevar.get()))
            except Exception as ep:
                messagebox.showerror('Error',  ep,parent=self.root)
            clearEntry()
        
        #----------------------------------------------------------------------------
        #-------------------------Tạo Delete---------------------------------------------
        def deleteRow():
            global selected_rowid
            conn.execute("DELETE FROM Expense_record WHERE rowid=?", (selected_rowid))
        #--------------------------Exit---------------------------------------------
        def exit():
            self.root.destroy()
        #----------------------------------------------------------------------------
        self.tree= ttk.Treeview(frame, columns=(1, 2, 3, 4), show='headings', height=8)
        # Add heading to self.treeview
        self.tree.column(1, anchor=CENTER,width=100)
        self.tree.column(2, anchor=CENTER,width=190)
        self.tree.column(3, anchor=CENTER,width=150)
        self.tree.column(4, anchor=CENTER,width=140)
        self.tree.heading(1, text="Id")
        self.tree.heading(2, text='Item', )
        self.tree.heading(3, text='Amount')
        self.tree.heading(4,text='Date')
       
        self.tree.grid(row=0, column=0)
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        fetch()
        #----nơi chứa dữ liệu-----------------------
        lbl_name=Label(frame,text="ITEM NAME",font=("times new roman",13,"bold"),bg="gray")
        lbl_name.place(x=20,y=260)
        txt_name=Entry(frame,font=("times new roman",13,"bold"),textvariable=self.itemvar)
        txt_name.place(x=150,y=250,width=200,height=30)
        lbl_amont=Label(frame,text="ITEM PRICE",font=("times new roman",13,"bold"),bg="gray")
        lbl_amont.place(x=20,y=310)
        txt_amont=Entry(frame,font=("times new roman",13,"bold"),textvariable=self.amountvar)
        txt_amont.place(x=150,y=300,width=200,height=30)
        lbl_date=Label(frame,text="DATE",font=("times new roman",13,"bold"),bg="gray")
        lbl_date.place(x=20,y=360)
        txt_date=Entry(frame,font=("times new roman",13,"bold"),textvariable=self.datevar)
        txt_date.place(x=150,y=350,width=200,height=30)
        #----Các chức năng sửa xóa dữ liệu--------------------------
        total_btn=Button(frame,text='Total',font=("times new roman",13,"bold"),command=total,bg="blue",fg="black")
        total_btn.place(x=380,y=280,width=100,height=50)
        history_btn=Button(frame,text='History',font=("times new roman",13,"bold"),bg="blue",fg="black")
        history_btn.place(x=480,y=280,width=100,height=50)
        repair_btn=Button(frame,text='Repair',font=("times new roman",13,"bold"),command=repair,bg="yellow4",fg="black")
        repair_btn.place(x=480,y=230,width=100,height=50)
        delete_btn=Button(frame,text='Delete',command=deleteRow,font=("times new roman",13,"bold"),bg="red",fg="black")
        delete_btn.place(x=480,y=330,width=100,height=50)
        clear_btn=Button(frame,text="Clear Entry",command=clearEntry,font=("times new roman",13,"bold"),bg="yellow4",fg="black")
        clear_btn.place(x=380,y=230,width=100,height=50)
        exit_btn=Button(frame,text="Exit",font=("times new roman",13,"bold"),command=exit,bg="red",fg="black")
        exit_btn.place(x=380,y=330,height=50,width=100)
        #-------------------------------------------------------
        self.tree.bind("<ButtonRelease-1>", select_record)
            
if __name__=="__main__":		
    root=tk.Tk()
    app=Summary(root)
    root.mainloop()      