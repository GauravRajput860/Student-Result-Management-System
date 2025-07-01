# from tkinter import *
# from PIL import Image, ImageTk
# from tkinter import ttk
# from tkinter import messagebox
# import sqlite3
# import os

# class Login:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Registration Window")
#         self.root.geometry("1100x700+150+0")
#         self.root.resizable(0,0)
#         # =======Background Image ===============
#         main_bg = "img/login_bg.png"
#         self.bg_img = Image.open(main_bg)
#         self.bg_img = self.bg_img.resize((1100, 768))  # Resize if needed
#         self.bg_img = ImageTk.PhotoImage(self.bg_img)
#         self.bg_label = Label(self.root, image=self.bg_img).place(
#             x=0, y=0, relheight=1, relwidth=1
#         )

#         #         quot_lbl = Label(
#         #             self.root,
#         #             text=" Prof. Rajbir Singh \nThe purpose of \neducation is to replace \nan empty mind with \nan open one. - Malcolm Forbes ",
#         #             font=("goudy old style", 15, "bold"),
#         #             bg="lightyellow",
#         #             bd=4,
#         #             relief=RAISED,
#         #         ).place(x=120, y=400)

#         # ======login frame==========
#         frame1 = Frame(self.root, bg="white", bd=4, relief=RIDGE)
#         frame1.place(x=410, y=130, height=395, width=550)

#         title = Label(
#             frame1,
#             text="LOG IN HERE",
#             font=("times new roman", 20, "bold"),
#             bg="white",
#             fg="green",
#         ).place(x=180, y=10)
#         # ===========VC imgae========================
#         vc_pic = "img/admin_logo.png"
#         self.vc_img = Image.open(vc_pic)
#         self.vc_img = self.vc_img.resize((260, 299))  # Resize if needed
#         self.vc_img = ImageTk.PhotoImage(self.vc_img)
#         self.vc_label = Label(self.root, image=self.vc_img, bd=0, relief=RAISED).place(
#             x=250, y=180
#         )

#         # ======first name ,label,entry===============
#         username = Label(
#             frame1,
#             text="Username",
#             font=("times new roman", 15, "bold"),
#             bg="white",
#             fg="gray",
#         ).place(x=150, y=70)
#         self.username_entry = Entry(
#             frame1, bg="lightgray",  font=("times new roman", 15), width=30
#         )
#         self.username_entry.place(x=150, y=95)

#         # ========last name, entry,lable,entry=========

#         password = Label(
#             frame1,
#             text="Password",
#             font=("times new roman", 15, "bold"),
#             bg="white",
#             fg="gray",
#         ).place(x=150, y=150)
#         self.password_entry = Entry(
#             frame1, show="*",bg="lightgray", width=30, font=("times new roman", 15)
#         )
#         self.password_entry.place(x=150, y=175)

#         self.login_btn = ImageTk.PhotoImage(file="img/login_btn.png")
#         btn2 = Button(frame1, image=self.login_btn,bd=0,bg="white",cursor='hand2',command=self.log_in).place(
#             x=230, y=220,height=40
#         )

#         self.add_friend_btn = ImageTk.PhotoImage(file="img/create_acc_img.png")
#         btn3 = Button(
#             frame1, image=self.add_friend_btn, bd=0, bg="white", cursor="hand2",command=self.register_window
#         ).place(x=150, y=290)
#         self.create_acc = Label(
#             frame1,
#             text="← Create Account",
#             font=("times new roman", 20, "bold"),
#             fg="green",
#             bg="white",
#         ).place(x=200, y=300)

#         Button(frame1, text="Forget Password?", font=("times new roman", 12, "bold"), fg="red", bg="white", bd=0, cursor="hand2", command=self.forget_password).place(x=230, y=265)


#     def register_window(self):
#         self.root.destroy()
#         import register

#     def log_in(self):
#         username = self.username_entry.get()
#         password = self.password_entry.get()

#         if username == "" or password == "":
#          messagebox.showerror("Error", "All fields are required", parent=self.root)
#         elif len(password) < 8:
#          messagebox.showerror("Error", "Password must be at least 8 characters long", parent=self.root)

#         else:
#             try:
#                 con = sqlite3.connect(database="srms.db")
#                 cur = con.cursor()
#                 cur.execute("select * from employee where email=? and password=?",(self.username_entry.get(),self.password_entry.get()))
#                 row=cur.fetchone()
#                 if row==None:
#                     messagebox.showerror("Error", "Invalid USERNAME & PASSWORD", parent=self.root)
#                 else:
#                     messagebox.showinfo("Success", "Log In Successful", parent=self.root)
#                     self.show_processing() # option processing bar
#                     # self.root.destroy()
#                     # os.system("python dashboard.py")
#                 con.close()

#             except Exception as es:
#                 messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)

#     def show_processing(self):
#         """Show a processing animation before opening the dashboard"""
#         self.process_win = Toplevel(self.root)
#         self.process_win.title("Processing...")
#         self.process_win.geometry("350x150+500+300")
#         self.process_win.config(bg="white")
#         self.process_win.grab_set()

#         Label(self.process_win, text="Please wait...", font=("times new roman", 15, "bold"),
#               bg="white", fg="green").pack(pady=10)

#         progress = ttk.Progressbar(self.process_win, orient=HORIZONTAL, length=250, mode="determinate")
#         progress.pack(pady=20)
#         progress.start(10)

#         # Simulate processing time before opening the dashboard
#         self.root.after(3000, self.open_dashboard)

#     def open_dashboard(self):
#         """Close processing window and open the dashboard"""
#         self.process_win.destroy()
#         self.root.destroy()
#         os.system("python dashboard.py")


#     def forget_password(self):
#         """ Function to handle password reset """

#         def reset_password():
#             """ Function to update the password in the database """
#             email = email_entry.get()
#             new_pass = new_pass_entry.get()
#             confirm_pass = confirm_pass_entry.get()

#             if email == "" or new_pass == "" or confirm_pass == "":
#                  messagebox.showerror("Error", "All fields are required", parent=reset_win)
#             elif len(new_pass) < 8:
#                 messagebox.showerror("Error", "Password must be at least 8 characters long", parent=reset_win)
#             elif new_pass != confirm_pass:
#                  messagebox.showerror("Error", "Passwords do not match", parent=reset_win)
#             else:
#                 try:
#                     con = sqlite3.connect(database="srms.db")
#                     cur = con.cursor()
#                     cur.execute("SELECT * FROM employee WHERE email=?", (email_entry.get(),))
#                     row = cur.fetchone()
#                     if row is None:
#                         messagebox.showerror("Error", "Email not found", parent=reset_win)
#                     else:
#                         cur.execute("UPDATE employee SET passwrod=? WHERE email=?", (new_pass_entry.get(), email_entry.get()))
#                         con.commit()
#                         messagebox.showinfo("Success", "Password reset successfully!", parent=reset_win)
#                         reset_win.destroy()
#                     con.close()
#                 except Exception as es:
#                     messagebox.showerror("Error", f"Error due to {str(es)}", parent=reset_win)

#         # Create a new window for password reset
#         reset_win = Toplevel(self.root)
#         reset_win.title("Reset Password")
#         reset_win.geometry("400x350+500+200")
#         reset_win.config(bg="white")

#         Label(reset_win, text="Forget Password", font=("times new roman", 20, "bold"), fg="green", bg="white").place(x=100, y=20)

#         Label(reset_win, text="Email", font=("times new roman", 15), bg="white", fg="gray").place(x=50, y=70)
#         email_entry = Entry(reset_win, font=("times new roman", 15), bg="lightgray", width=30)
#         email_entry.place(x=50, y=100)

#         Label(reset_win, text="New Password", font=("times new roman", 15), bg="white", fg="gray").place(x=50, y=140)
#         new_pass_entry = Entry(reset_win, font=("times new roman", 15), bg="lightgray", width=30, show="*")
#         new_pass_entry.place(x=50, y=170)

#         Label(reset_win, text="Confirm Password", font=("times new roman", 15), bg="white", fg="gray").place(x=50, y=210)
#         confirm_pass_entry = Entry(reset_win, font=("times new roman", 15), bg="lightgray", width=30, show="*")
#         confirm_pass_entry.place(x=50, y=240)

#         Button(reset_win, text="Reset Password", font=("times new roman", 15, "bold"), bg="green", fg="white", command=reset_password).place(x=130, y=280, width=150)


# root = Tk()
# obj = Login(root)
# root.mainloop()
