import sqlite3
import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
class Register:
    def __init__(self,root):      
        #Hinh nen
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        self.bg=ImageTk.PhotoImage(file=r"image/Anh2.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
         #Variable Stringvar:     
        # Main frame
        frame = Frame(self.root,bg="white")  
        frame.place(x=510,y=150,width=440,height=550)
        register_lbl=Label(frame,text="REGISTER",font=("times new roman",20,"bold"),borderwidth=0,bg="white",fg="red")
        register_lbl.place(x=20,y=20)
        #user name      
        uname=Label(frame,text="User Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        uname.place(x=20,y=60)
        self.txt_uname=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txt_uname.place(x=20,y=85,width=400,height="25")
       
        #Contact and Email     
        contact=Label(frame,text="Contact",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=20,y=130)
        self.txt_contact=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=20,y=155,width=400,height=25)
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=20,y=200)
        self.txt_Email=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txt_Email.place(x=20,y=225,width=400,height=25)
       
        #Security        
        security=Label(frame,text="Security",font=("times new roman",15,"bold"),fg="black",bg="white")
        security.place(x=20,y=270)
        self.txt_security=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txt_security.place(x=20,y=295,width=400,height=25)
        
        #Pass Word and Confirm Password
        
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=20,y=340)
        self.txt_password=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txt_password.place(x=20,y=365,width=400,height=25)
        
        confirm_password=Label(frame,text="Confirm password",font=("times new roman",15,"bold"),fg="black",bg="white")
        confirm_password.place(x=20,y=410)
        self.txt_confirm_password=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txt_confirm_password.place(x=20,y=435,width=400,height=25)
       
        #checkbutton
        
        self.var_check=BooleanVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agrees the terms & conditions",font=("times new roman",12,"bold"),fg="black",bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=20,y=470)
        
        #button
        img=Image.open("image/dangki.png")
        img=img.resize((110,40),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        btn1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,bg="white",fg="black")
        btn1.place(x=10,y=500)
        #login now()
        img_now=Image.open("image/Loginnow.jpg")
        img_now=img_now.resize((140,60),Image.ANTIALIAS)
        self.photoimage_now=ImageTk.PhotoImage(img_now)
        btnnow=Button(frame, image=self.photoimage_now,command=self.return_login,borderwidth=0,bg="white",fg="black")
        btnnow.place(x=270,y=500)
        #Function declaration
        
    def register_data(self):
        if self.txt_uname.get()== "" or self.txt_contact.get()=="" or self.txt_Email.get()=="Select" or self.txt_security.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Errow","All fields are required",parent=self.root)
        elif self.txt_password.get()!=self.txt_confirm_password.get():
            messagebox.showerror("Error","Password and Confirm Password phai giong nhau",parent=self.root)
        elif self.var_check.get()==False:
            messagebox.showerror("Error","Vui long dong y dieu khoan va dieu kien",parent=self.root)
        else:
            conn=sqlite3.connect("Manage.db")
            conn.execute("insert into User values('%s','%s','%s','%s','%s')"%(self.txt_uname.get(),self.txt_contact.get(),self.txt_Email.get(),self.txt_security.get(),self.txt_password.get()))    
            conn.commit()
            messagebox.showinfo("Success","Dang ki hoan thanh",parent=self.root)   

    def return_login(self):
        self.root.destroy()   

if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()