from datetime import date
from tkinter import *
from tkinter import ttk
from turtle import width
from PIL import Image, ImageTk
import tkinter as tk
import sqlite3
uname = "Tuan"

class Transaction:
    def __init__(self, root):
        self.root = root
        self.root.title("Transaction")
        self.root.geometry("600x600+550+100")
        frame = Frame(self.root, bg="white")
        frame.place(x=0, y=0, width=600, height=600)
        Label(frame, text = "This Month's Expense", width= 600, height = 3, anchor=CENTER, bg='green',fg='white',bd=4,font=('Times new roman','13','bold')).pack()
        expenseFrame = Frame(frame, padx = 10, pady=10)
        expenseFrame.pack(fill = BOTH, expand = True)
        expenseFrame.grid_columnconfigure(0, weight=1)
        expenseFrame.grid_columnconfigure(1, weight=1)
        # start date of current month (format : yyyy/mm/dd)
        sdate = '2022/08/28'
        today=str(date.today()).replace("-","/")
        #print("SELECT SUM(amount) FROM Expense WHERE type='expense' and username='%s' and edate>='%s' and edate<='%s'"%(uname,sdate,today))
        global uname
        conn = sqlite3.connect("Manage.db")
        cursor = conn.execute(
            "SELECT SUM(amount) FROM Expense WHERE type='expense' and username='%s' and edate>='%s' and edate<='%s'" % (uname, sdate, today))
        sum = 0
        flag1 = 0
        flag2 = 0
        for r in cursor:
            if r[0] == None:
                sum += 0
        else:
            sum += r[0]
            flag1 = 1
        self.Ex = Label(expenseFrame, text='Expense', pady=5, width=50, height=3, borderwidth='1', relief='solid',
                        bg='red3', fg='white', font=('Times new roman', '13')).grid(row=0,column=0)
        self.Rs1 = Label(expenseFrame, text='Rs. %s' % str(sum), pady=5, width=50, height=3, borderwidth='1',
                         relief='solid', bg='red3', fg='white', font=('Times new roman', '13')).grid(row=0,column=1)
        #database
        i = 1
        if flag1 == 1:
            cursor = conn.execute("SELECT * FROM Expense WHERE type='expense' and username='%s'  and edate>='%s' and edate<='%s'" % (uname, sdate, today))
            for r in cursor:
                Label(expenseFrame, text="%s" % r[2], pady=6, width=50, height=3, borderwidth='1', relief='solid', bg='red4', fg='white', font=(
                     'Times new roman', '13')).grid(row=i, column=0)
                Label(expenseFrame, text="%s" % r[4], pady=6, width=50, height=3, borderwidth='1', relief='solid', bg='red4', fg='white', font=(
                    'Times new roman', '13')).grid(row=i, column=1)
            i += 1
        cursor = conn.execute("SELECT SUM(amount) FROM Expense WHERE type='income' and username='%s'  and edate>='%s' and edate<='%s'"%(uname,sdate,today))
        sum=0
        for r in cursor:
            if r[0] == None:
                 sum +=0
            else:
                sum+=r[0]
                flag2 = 1
        Label(expenseFrame, text = 'Income', pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid', bg='SpringGreen4',fg='white',font=('Times new roman','13')).grid(row=i, column = 0)
        Label(expenseFrame, text = 'Rs. %s'%str(sum), pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid', bg='SpringGreen4',fg='white',font=('Times new roman','13')).grid(row=i, column = 1)
        i+=1
        if flag2 == 1:
            cursor = conn.execute("SELECT * FROM Expense WHERE type='income' and username='%s'  and edate>='%s' and edate<='%s'"%(uname,sdate,today))
        for r in cursor:
            Label(expenseFrame, text = "%s"%r[2],pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid', bg='green',fg='white',font=('Times new roman','13')).grid(row=i,column=0)
            Label(expenseFrame, text = "%s"%r[4],pady = 5,width=50,height = 3,borderwidth='1',relief = 'solid', bg='green',fg='white',font=('Times new roman','13')).grid(row=i,column=1)
            i+=1

if __name__ == "__main__":
    root = Tk()
    app = Transaction(root)
    root.mainloop()
