from datetime import date
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import sqlite3
uname="Tuan"
class Report:
    def __init__(self, root):
        # frame con hoat dong
        self.root = root
        self.root.title("Report")
        self.root.geometry("600x600+550+100")
        frame = Frame(self.root, bg="white")
        frame.place(x=0, y=0, width=600, height=600)
        Label(frame, text="Your Report", width=600, height=3, anchor=CENTER,
              bg='blue4', fg='gold', bd=4, font=('Times new roman', '14', 'bold')).pack()
        searchFrame = Frame(frame, padx=10, pady=10)
        searchFrame.pack(fill=BOTH, expand=True)
        searchFrame.grid_columnconfigure(0, weight=1)
        searchFrame.grid_columnconfigure(1, weight=1)
        searchFrame.grid_columnconfigure(2, weight=1)
        searchFrame.grid_columnconfigure(3, weight=1)
        Label(searchFrame, text="From", font=('Times new roman', '12', 'bold'),
            bg='purple', fg='white', width=10).grid(row=0, column=1)
        startDate_E = DateEntry(searchFrame, width=20, bd=3,
                            date_pattern='yyyy/mm/dd')
        startDate_E.grid(row=0, column=2, pady=5)
        startDate_E.set_date("2022/11/01")
        Label(searchFrame, text="To", font=('Times new roman', '12', 'bold'),
            bg='purple', width=10, fg='white').grid(row=1, column=1)
        endDate_E = DateEntry(searchFrame, width=20, bd=3,
                          date_pattern='yyyy/mm/dd')
        endDate_E.grid(row=1, column=2, pady=5)
        dataFrame = Frame(frame, padx = 10, pady=10)
        dataFrame.pack(fill = BOTH, expand = True)
        dataFrame.grid_columnconfigure(0, weight=1)
        dataFrame.grid_columnconfigure(1, weight=2)
        dataFrame.grid_columnconfigure(2, weight=2)
        conn=sqlite3.connect("Manage.db")
        #------------------
        #Dùng ScrollBar đẹp có thể sửa sau
        #------------------
        def search():
            a = startDate_E.get()
            b = endDate_E.get()
            cursor = conn.execute("SELECT * FROM Expense where username='%s' and edate >= '%s' and edate <= '%s'"%(uname,a,b))
            i = 0
            for r in cursor:
                if r[3] == 'expense':
                    Label(dataFrame, text = "%s - (%s) :"%(r[1],r[5]),width=50,height = 3,borderwidth='1',relief = 'solid',bg='red3',pady=3,fg='white',font=('Times new roman','13')).grid(row=i,column=1)
                    Label(dataFrame, text = 'Rs. %s'%(r[4]), width = 50,height=3, borderwidth = '1',bg='red3',relief='solid',pady=3,fg='white',font=('Times new roman','13')).grid(row=i,column=2)
                    i+=1
                else:
                    Label(dataFrame, text = "%s - (%s) :"%(r[1],r[5]),width=50,height = 3,borderwidth='1',relief = 'solid',bg='green',pady=3,fg='white',font=('Times new roman','13')).grid(row=i,column=1)
                    Label(dataFrame, text = 'Rs. %s'%(r[4]), width = 50,height=3, borderwidth = '1',bg='green',relief='solid',pady=3,fg='white',font=('Times new roman','13')).grid(row=i,column=2)
                    i+=1
        Button(searchFrame, text="Search", width=10, command = search, bg = 'gold', activebackground='green2',font=('Times new roman','18')).grid(row = 2, column = 2,pady=10)
        #database 
        today=str(date.today()).replace("-","/")   
        cursor=conn.execute("SELECT * FROM Expense WHERE edate='%s' and type='expense' and username='%s'"%(today,uname))
        i = 0
        for r in cursor:
            Label(dataFrame, text = "%s - (%s)"%(r[1],r[5]),width=50,height = 3,borderwidth='1',relief = 'solid',bg='red3',pady=3,fg='white',font=('Times new roman','13')).grid(row=i,column=1)
            Label(dataFrame, text = 'Rs. %s'%(r[4]), width = 50,height=3, borderwidth = '1',bg='red3',relief='solid',pady=3,fg='white',font=('Times new roman','13')).grid(row=i,column=2)
            i+=1
        cursor=conn.execute("SELECT * FROM Expense WHERE edate='%s' and type='income' and username='%s'"%(today,uname))
        for r in cursor:
            Label(dataFrame, text = "%s - (%s) :"%(r[1],r[5]),width=50,height = 3,borderwidth='1',relief = 'solid',bg='green',pady=3,fg='white',font=('Times new roman','13')).grid(row=i,column=1)
            Label(dataFrame, text = 'Rs. %s'%(r[4]), width = 50,height=3, borderwidth = '1',bg='green',relief='solid',pady=3,fg='white',font=('Times new roman','13')).grid(row=i,column=2)
            i+=1      
if __name__ == "__main__":
    root = Tk()
    app = Report(root)
    root.mainloop()
