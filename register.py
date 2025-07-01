from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        # =======Background Image ===============
        main_bg = "img/bg_for_register.jpg"
        self.bg_img = Image.open(main_bg)
        self.bg_img = self.bg_img.resize((1350, 700))  # Resize if needed
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.bg_label = Label(self.root, image=self.bg_img).place(
            x=0, y=0, relheight=1, relwidth=1
        )
        
        # ======login frame==========
        frame1 = Frame(self.root, bg="white", bd=4, relief=RIDGE)
        frame1.place(x=385, y=130, height=395, width=700)

        title = Label(
            frame1,
            text="REGISTER HERE",
            font=("times new roman", 20, "bold"),
            bg="white",
            fg="green",
        ).place(x=10, y=10)
        # =========variables=====================

        # ======first name ,label,entry===============
        first_name = Label(
            frame1,
            text="First Name",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray",
        ).place(x=30, y=50)
        self.first_name_entry = Entry(
            frame1, bg="lightgray", font=("times new roman", 12), width=35
        )
        self.first_name_entry.place(x=30, y=75)

        # ========last name, entry,lable,entry=========

        last_name = Label(
            frame1,
            text="Last Name",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray",
        ).place(x=350, y=50)
        self.last_name_entry = Entry(
            frame1, bg="lightgray", width=35, font=("times new roman", 12)
        )
        self.last_name_entry.place(x=350, y=75)

        # ======email,label,entry===============
        email = Label(
            frame1,
            text="Email",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray",
        ).place(x=30, y=100)
        self.email_entry = Entry(
            frame1, bg="lightgray", font=("times new roman", 12), width=35
        )
        self.email_entry.place(x=30, y=125)

        # ========contact, entry,lable,entry=========

        contact = Label(
            frame1,
            text="Contact",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray",
        ).place(x=350, y=100)
        self.contact_entry = Entry(
            frame1, bg="lightgray", width=35, font=("times new roman", 12)
        )
        self.contact_entry.place(x=350, y=125)

        # ======question,label,entry===============
        question = Label(
            frame1,
            text="Security Question",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray",
        ).place(x=30, y=150)
        self.question_entry = ttk.Combobox(
            frame1,
            font=("times new roman", 12),
            width=33,
            state="readonly",
            justify=CENTER,
        )
        self.question_entry["values"] = (
            "Select",
            "Your Best Friend Name",
            "Your School Name",
            "Your Birth Place",
        )
        self.question_entry.current(0)
        self.question_entry.place(x=30, y=175)

        # ========answer, entry,lable,entry=========

        answer = Label(
            frame1,
            text="Answer",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray",
        ).place(x=350, y=150)
        self.answer_entry = Entry(
            frame1, bg="lightgray", width=35, font=("times new roman", 12)
        )
        self.answer_entry.place(x=350, y=175)

        # ======password,label,entry===============
        password = Label(
            frame1,
            
            text="Password",
            
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray",
        ).place(x=30, y=200)
        self.password_entry = Entry(
            frame1, show="*",bg="lightgray", font=("times new roman", 12), width=35
        )
        self.password_entry.place(x=30, y=225)

        # ========confirm_pass, entry,lable,entry=========

        confirm_pass = Label(
            frame1,
            text="Confirm Password",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray",
        ).place(x=350, y=200)
        self.confirm_pass_entry = Entry(
            frame1, bg="lightgray", width=35, font=("times new roman", 12)
        )
        self.confirm_pass_entry.place(x=350, y=225)

        # ==========checkbox for terms and conditions=============
        self.var_term=IntVar()
        self.term = Checkbutton(
            frame1,
            text="I Agree with Terms & Conditions.",
            variable=self.var_term,
            onvalue=1,
            offvalue=0,
            bg="white",
            font=("times new roman", 12),
        ).place(x=30, y=260)

        # =======Register button ==============================
        self.btn_img = ImageTk.PhotoImage(file="img/rg2.jpg")
        self.register_btn = Button(
            frame1,
            image=self.btn_img,
            bd=0,
            bg="white",
            cursor="hand2",
            command=self.register_data,
        ).place(x=220, y=320)

        self.login_btn = ImageTk.PhotoImage(file="img/login_btn.png")
        self.btn2 = Button(
            frame1, image=self.login_btn, bd=0, bg="white", cursor="hand2", command=self.login_window
        ).place(x=570, y=10, height=40)
        
    def clear(self):
        self.first_name_entry.delete(0,END)
        self.last_name_entry.delete(0,END)
        self.email_entry.delete(0,END)
        self.contact_entry.delete(0,END)
        self.question_entry.current(0)
        self.answer_entry.delete(0,END)
        self.password_entry.delete(0,END)
        self.confirm_pass_entry.delete(0,END)
        

    def login_window(self):
        root.destroy()
        os.system("python log_in.py")
    
    
    def register_data(self):
        if self.first_name_entry.get()=="" or self.email_entry.get()=="" or self.contact_entry.get()=="" or self.question_entry.get()=="Select" or self.answer_entry.get()=="" or self.password_entry.get()==" " or self.confirm_pass_entry.get()=="":
            messagebox.showerror("Error", "All fields required", parent=self.root)
        elif len(self.password_entry.get()) < 8:
             messagebox.showerror("Error", "Password must be at least 8 characters long", parent=self.root)
        elif self.confirm_pass_entry.get() != self.password_entry.get():
              messagebox.showerror("Error", "Password and Confirm Password should be same", parent=self.root)
        elif self.var_term.get()==0:
            messagebox.showerror("Error", "Please agree our term & conditions ")
        else:
            try:
                con = sqlite3.connect(database="srms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=?",(self.email_entry.get(),))
                row=cur.fetchone()
                if row!=None:
                    
                    messagebox.showerror("Error", "User already exist, Please try with another email !",parent=self.root)
                else:
                    cur.execute("insert into employee ( f_name,l_name,email,contact,question,answer,password) values(?,?,?,?,?,?,?)",
                                
                                (
                                    self.first_name_entry.get(),
                                    self.last_name_entry.get(),
                                    self.email_entry.get(),
                                    self.contact_entry.get(),
                                    self.question_entry.get(),
                                    self.answer_entry.get(),
                                    self.password_entry.get()
                                ))
                    con.commit() 
                    con.close()
                    messagebox.showinfo("Success", "Register Successfully")
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)}",parent=self.root)   

root = Tk()
obj = Register(root)
root.mainloop()
