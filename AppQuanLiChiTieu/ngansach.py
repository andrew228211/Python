from datetime import date
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
uname="Tuan"
class Budget:
    def __init__(self,root):
        #frame con hoat dong
        self.root = root
        self.root.title("Report")
        self.root.geometry("600x600+550+100")
        frame = Frame(self.root, bg="white")
        frame.place(x=0, y=0, width=600, height=600) 
        daily_sum=Frame(frame,width=100,height=100)
        Label(daily_sum,text="Graph Budget",anchor=W,justify=LEFT).pack()
        #data 
        today=str(date.today()).replace("-","/")
        conn=sqlite3.connect("Manage.db")
        
if __name__=="__main__":		
    root=Tk()
    app=Budget(root)
    root.mainloop()     