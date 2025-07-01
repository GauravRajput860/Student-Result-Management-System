from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os
import cv2


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("MDU Student Management System - Login")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)
        self.root.config(bg="#CFEAF2")

        main_bg = "img/bg2.png"
        self.bg_img = Image.open(main_bg)
        self.bg_img = self.bg_img.resize((1350, 700))  # Resize if needed
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.bg_label = Label(self.root, image=self.bg_img).place(
            x=0, y=0, relheight=1, relwidth=1
        )

        # ===== Login Frame =====
        self.frame = Frame(self.root, bg="white", bd=0)
        self.frame.place(x=800, y=0, width=600, height=700)

        # Title
        Label(
            self.frame,
            text="LOG IN HERE",
            font=("Times New Roman", 24, "bold"),
            fg="#203061",
            bg="white",
        ).place(x=150, y=270)

        vc_pic1 = "img/mdu__logo.jpg"  # Replace with your new icon
        img1 = Image.open(vc_pic1).resize((560, 103))
        self.vc_img = ImageTk.PhotoImage(img1)
        Label(self.frame, image=self.vc_img, bg="white").place(x=0, y=0)
        # User Icon
        admin_pic = "img/admin_log_in.png"  # Replace with your new icon
        img = Image.open(admin_pic).resize((200 - 80, 220 - 80))
        self.admin_img = ImageTk.PhotoImage(img)
        Label(self.frame, image=self.admin_img, bg="white").place(x=200, y=130)

        # Username Label & Entry
        Label(
            self.frame,
            text="Username",
            font=("Times New Roman", 16, "bold"),
            fg="#333333",
            bg="white",
        ).place(x=100, y=300 + 40)
        self.username_entry = Entry(
            self.frame,
            font=("Times New Roman", 15),
            bg="#ECE8DD",
            fg="#333333",
            bd=0,
            width=26,
        )
        self.username_entry.place(x=220, y=300 + 40, height=30)

        # Password Label & Entry
        
        Label(
            self.frame,
            text="Password",
            font=("Times New Roman", 16, "bold"),
            fg="#333333",
            bg="white",
        ).place(x=100, y=410)

        self.password_entry = Entry(
            self.frame,
            font=("Times New Roman", 15),
            bg="#ECE8DD",
            fg="#333333",
            bd=0,
            show="*",
            width=25,
        )
        self.password_entry.place(x=220, y=410, height=30)

        # Load Eye Images
        eye_open = Image.open("img/open_eye.png").resize((20, 20))
        eye_closed = Image.open("img/close_eye.png").resize((20, 20))
        self.eye_open_icon = ImageTk.PhotoImage(eye_open)
        self.eye_closed_icon = ImageTk.PhotoImage(eye_closed)

        self.show_password = False
        self.toggle_btn = Button(
            self.frame,
            image=self.eye_closed_icon,
            bg="#ECE8DD",
            bd=0,
            activebackground="#ECE8DD",
            cursor="hand2",
            command=self.toggle_password,
        )
        self.toggle_btn.place(x=450, y=410, height=30, width=30)

        # Login Button
        self.login_btn = Button(
            self.frame,
            text="LOGIN",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#203061",
            bd=0,
            cursor="hand2",
            command=self.log_in,
        )
        self.login_btn.place(x=100, y=500, width=380, height=40)

        

        # Forgot Password
        Button(
            self.frame,
            text="Forgot Password?",
            font=("Times New Roman", 12, "bold"),
            fg="red",
            bg="white",
            bd=0,
            cursor="hand2",
            command=self.forget_password,
        ).place(x=350, y=410 + 30)

        # Create Account
        Button(
            self.frame,
            text=" Create Account",  # ←
            font=("Times New Roman", 18, "bold"),
            fg="#228B22",
            bg="white",
            bd=0,
            cursor="hand2",
            command=self.register_window,
        ).place(x=200, y=550)

    def toggle_password(self):
        if self.show_password:
            self.password_entry.config(show="*")
            self.toggle_btn.config(image=self.eye_closed_icon)
            self.show_password = False
        else:
            self.password_entry.config(show="")
            self.toggle_btn.config(image=self.eye_open_icon)
            self.show_password = True

    def register_window(self):
        self.root.destroy()
        os.system("python register.py")

    def log_in(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif len(password) < 8:
            messagebox.showerror(
                "Error", "Password must be at least 8 characters long", parent=self.root
            )
        else:
            try:
                con = sqlite3.connect("srms.db")
                cur = con.cursor()
                cur.execute(
                    "SELECT * FROM employee WHERE email=? AND password=?",
                    (username, password),
                )
                row = cur.fetchone()
                con.close()
                if row is None:
                    messagebox.showerror(
                        "Error", "Invalid username or password", parent=self.root
                    )
                else:
                    messagebox.showinfo(
                        "Success", "Log In Successful", parent=self.root
                    )
                    self.show_processing()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}", parent=self.root)

    def show_processing(self):
        self.process_win = Toplevel(self.root)
        self.process_win.title("Processing...")
        self.process_win.geometry("350x150+500+300")
        self.process_win.config(bg="white")
        self.process_win.grab_set()

        Label(
            self.process_win,
            text="Please wait...",
            font=("Times New Roman", 15, "bold"),
            fg="#228B22",
            bg="white",
        ).pack(pady=10)

        progress = ttk.Progressbar(
            self.process_win, orient=HORIZONTAL, length=250, mode="determinate"
        )
        progress.pack(pady=10)
        progress.start(10)

        self.root.after(3000, self.open_dashboard)

    def open_dashboard(self):
        self.process_win.destroy()
        self.root.destroy()
        os.system("python dashboard.py")

    def forget_password(self):
        # ------- Reset Window -------
        reset_win = Toplevel(self.root)
        reset_win.title("Reset Password")
        reset_win.geometry("400x350+500+200")
        reset_win.config(bg="white")
        reset_win.grab_set()

        Label(
            reset_win,
            text="Forget Password",
            font=("Times New Roman", 20, "bold"),
            fg="#228B22",
            bg="white",
        ).place(x=110, y=20)

        # Email
        Label(
            reset_win, text="Email", font=("Times New Roman", 15), fg="gray", bg="white"
        ).place(x=50, y=80)
        email_entry = Entry(
            reset_win, font=("Times New Roman", 15), bg="#ECE8DD", bd=0, width=30
        )
        email_entry.place(x=50, y=110, height=30)

        # New Password
        Label(
            reset_win,
            text="New Password",
            font=("Times New Roman", 15),
            fg="gray",
            bg="white",
        ).place(x=50, y=150)
        new_pass_entry = Entry(
            reset_win,
            font=("Times New Roman", 15),
            bg="#ECE8DD",
            bd=0,
            show="*",
            width=30,
        )
        new_pass_entry.place(x=50, y=180, height=30)

        # Confirm Password
        Label(
            reset_win,
            text="Confirm Password",
            font=("Times New Roman", 15),
            fg="gray",
            bg="white",
        ).place(x=50, y=220)
        confirm_pass_entry = Entry(
            reset_win,
            font=("Times New Roman", 15),
            bg="#ECE8DD",
            bd=0,
            show="*",
            width=30,
        )
        confirm_pass_entry.place(x=50, y=250, height=30)

        # Reset Button
        Button(
            reset_win,
            text="Reset Password",
            font=("Arial", 15, "bold"),
            bg="#228B22",
            fg="white",
            bd=0,
            cursor="hand2",
            command=lambda: self.reset_password(
                email_entry, new_pass_entry, confirm_pass_entry, reset_win
            ),
        ).place(x=120, y=300, width=160, height=40)

    def reset_password(self, email_entry, new_pass_entry, confirm_pass_entry, win):
        email = email_entry.get().strip()
        new_pass = new_pass_entry.get().strip()
        confirm_pass = confirm_pass_entry.get().strip()

        if not email or not new_pass or not confirm_pass:
            messagebox.showerror("Error", "All fields are required", parent=win)
        elif len(new_pass) < 8:
            messagebox.showerror(
                "Error", "Password must be at least 8 characters long", parent=win
            )
        elif new_pass != confirm_pass:
            messagebox.showerror("Error", "Passwords do not match", parent=win)
        else:
            try:
                con = sqlite3.connect("srms.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM employee WHERE email=?", (email,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Email not found", parent=win)
                else:
                    cur.execute(
                        "UPDATE employee SET password=? WHERE email=?",
                        (new_pass, email),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Password reset successfully!", parent=win
                    )
                    win.destroy()
                con.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}", parent=win)


if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()
