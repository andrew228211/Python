import sqlite3
from ctypes import resize
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
class Forgot:
    def __init__(self,root):
        #variable
        self.Check_email=StringVar()
        self.new_pass=StringVar()
        self.new_comfirm = StringVar()
        #Hinh nen
        self.root=root
        self.root.title("Forgot PassWord")
        self.root.geometry("1600x900+0+0")
        self.bg=ImageTk.PhotoImage(file="image/Forgot.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        #Main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)
        #Image
        img1=Image.open("image/6195699.png")
        img1=img1.resize((100,100))
        self.photo=ImageTk.PhotoImage(img1)
        lbl_img1=Label(frame,image=self.photo,bg="white",borderwidth=0)
        lbl_img1.place(x=120,y=5,width=100,height=100)
        #Nhap Email
        
        img2=Image.open(r"image/Login.png")
        img2=img2.resize((28,28),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(frame,image=self.photoimg2,bg="white",borderwidth=0)
        lblimg2.place(x=50,y=140)
        Email=Label(frame,text="Email",font=("times new roman",20,"bold"),fg="black",bg="white")
        Email.place(x=80,y=135)
        txt_Email=ttk.Entry(frame,textvariable=self.Check_email,font=("times new roman",15,"bold"))
        txt_Email.place(x=50,y=170,width=250,height=25)
        #Nhap Password
        
        img3=Image.open("image/PassWord.png")
        img3=img3.resize((28,28),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(frame,image=self.photoimage3,bg="white",borderwidth=0)
        lblimg3.place(x=50,y=215)
        password=Label(frame,text="Password",font=("times new roman",20,"bold"),fg="black",bg="white")
        password.place(x=80,y=210)        
        txt_password=ttk.Entry(frame,textvariable=self.new_pass,font=("times new roman",15,"bold"))
        txt_password.place(x=50,y=250,width=250,height=25)
        #Nhap Confirm Password
        
        lblimg4=Label(frame,image=self.photoimage3,bg="white",borderwidth=0)
        lblimg4.place(x=50,y=295)
        confirm_password=Label(frame,text="Confirm password",font=("times new roman",20,"bold"),fg="black",bg="white")
        confirm_password.place(x=80,y=290)
        txt_confirm_password=ttk.Entry(frame,textvariable=self.new_comfirm,font=("times new roman",15,"bold"))
        txt_confirm_password.place(x=50,y=335,width=250,height=25)
        
        #Button kiem tra:
        Okbtn=Button(frame,text="Ok",command=self.forgot_Password,font=("times new roman",15,"bold"),relief=RIDGE,fg="white",bg="red")
        Okbtn.place(x=110,y=385,width=120,height=30)
        #Exit Forgot
        imgX=Image.open("image/flagX.png")
        imgX=imgX.resize((20,20),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(imgX)
        Xbtn=Button(frame,image=self.photoimage4,command=self.return_login,borderwidth=0,bg="white")
        Xbtn.place(x=300,y=10)
    def forgot_Password(self):
        if self.Check_email.get()=="":
            messagebox.showerror("Error","Please enter your mail",parent=self.root)
        elif self.new_pass.get()=="":
            messagebox.showerror("Error","Please enter new password",parent=self.root)
        elif self.new_comfirm.get()=="":
            messagebox.showerror("Error","Please enter new confirm",parent=self.root)
        elif self.new_pass.get() !=self.new_comfirm.get():
            messagebox.showerror("Error","Password and Confirm Password are not the same",parent=self.root)
        else:
            conn=sqlite3.connect("Manage.db")
            ketnoi=conn.cursor()
            ketnoi.execute("SELECT * FROM User where email='"+self.Check_email.get()+"'")
            cursor=ketnoi.fetchone()
            print(cursor)
            if cursor==None :
                messagebox.showerror("Error","Email does not exist",parent=self.root)
            else:
                ketnoi.execute("UPDATE User set password='"+self.new_pass.get()+"'  where email='"+self.Check_email.get()+"'")
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Password has been reset, please login new password",parent=self.root)
    def return_login(self):
        self.root.destroy()   
if __name__=="__main__":
    root=Tk()
    app=Forgot(root)
    root.mainloop()