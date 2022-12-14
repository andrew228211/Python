import sqlite3
import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from Management import Summary
from forgot import Forgot
from register import Register
class Login_Window(Register):
    def __init__(self,root):
        super().__init__(root)
        #variable
        self.user=StringVar()
        self.password=StringVar()
        #Hinh anh
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")   
        self.bg=ImageTk.PhotoImage(file="image/Nen.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        #Tao frame con
        frame = Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        #Hinh anh
        img1=Image.open("image/User2.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Spend Management",font=("times new roman",20,"bold"),fg="white",bg="black").pack(pady=100)
        # get_str.place(x=70,y=100)
        #label1 User
        img2=Image.open("image/Login.png")
        img2=img2.resize((27,27),Image.ANTIALIAS)   
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=648,y=326,width=25,height=25)   
        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)       
        self.txtuser=Entry(frame,textvariable=self.user,font=("times new roman",10,"bold"))
        self.txtuser.place(x=40,y=180,width=280,height=30)
        #label2 Password
        img3=Image.open("image/PassWord.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=648,y=395,width=25,height=25)
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)        
        self.txtpassword=Entry(frame,textvariable=self.password,show="*",font=("times new roman",10,"bold"))
        self.txtpassword.place(x=40,y=250,width=280,height=30)
        #Login button
        loginbtn=Button(frame,command=self.Login,text="Login",font=("times new roman",15,"bold"),relief=RIDGE,fg="white",bg="red")
        loginbtn.place(x=110,y=290,width=120,height=30)
        #register button
        registerbtn=Button(frame,text="Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black")
        registerbtn.place(x=20,y=320,width=120,height=30)
        #forgetpass button
        forgotbtn=Button(frame,text="Forgot Password",command=self.forgot_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black")
        #forgotbtn.pack(padx=10,pady=350)
        forgotbtn.place(x=10,y=350,width=180,height=35)
    def Login(self):
        if self.user.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","all field required")
        else:
            conn=sqlite3.connect("Manage.db")
            cursor = conn.execute("Select * from User where username='%s' and password='%s'"%(self.user.get(),self.password.get()))
            conn.commit()
            if len(cursor.fetchall())>0:
                self.new_window=Toplevel(self.root)
                self.app=Summary(self.new_window)               
            else:
               messagebox.showerror("Error","Inavalid Username and Password")            
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    def forgot_window(self):
        self.new_window1=Toplevel(self.root)
        self.app=Forgot(self.new_window1)
if __name__=="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()      