from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import csv


class result_cls:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Result ")
        self.root.geometry("1200x450+80+80")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(0, 0)

        # ====title===
        title = Label(
            self.root,
            text="Add Students Result",
            padx=30,
            compound=LEFT,
            # image=self.logo_dash,
            font=("goudy old style", 20, "bold"),
            bg="#6E3E70",
            fg="#FFDCC9",
        ).place(x=10, y=12, width=1180, height=50)
        # -----------variables-------------------------------------------------
        self.var_rollno = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_fullmarks = StringVar()
        self.rollno_list = []
        self.fetch_rollno()

        # ----------------select student , entry, search button------------------------------------
        lbl_rollno = Label(
            self.root,
            text="Select Student",
            font=("goudy old style", 18, "bold"),
            bg="white",
        ).place(x=30, y=80)

        self.entry_rollno = ttk.Combobox(
            self.root,
            textvariable=self.var_rollno,
            font=("goudy old style", 18, "bold"),
            justify=CENTER,
            values=self.rollno_list,
        )
        self.entry_rollno.place(x=200, y=80, width=200)
        self.entry_rollno.set("Select")
        
        self.search_btn = ImageTk.PhotoImage(file="img/search.png")
        self.btn5 = Button(self.root, image=self.search_btn,bd=0,bg="white",cursor='hand2',
            command=self.search,
        )
        self.btn5.place(x=420, y=80)
        lbl_clear=Label(self.root, text="Search", bg="white",font=("goudy old style", 14, "bold")).place(x=455, y=80)


        # ----------------------name , entry, -------------------------------
        lbl_name = Label(
            self.root, text="Name", font=("goudy old style", 18, "bold"), bg="white"
        ).place(x=30, y=130)

        entry_name = Entry(
            self.root,
            textvariable=self.var_name,
            font=("goudy old style", 18, "bold"),
            state="readonly",
            bg="#bca0dc",
        ).place(x=200, y=130, width=330)

        # -----------------course--entrty---------------------------
        lbl_course = Label(
            self.root,
            text="Course",
            font=("goudy old style", 18, "bold"),
            bg="white",
        ).place(x=30, y=180)

        entry_course = Entry(
            self.root,
            textvariable=self.var_course,
            font=("goudy old style", 18, "bold"),
            state="readonly",
            bg="#bca0dc",
        ).place(x=200, y=180, width=330)

        # -------------marks--entry-------------------------------------
        lbl_marks = Label(
            self.root,
            text="Marks",
            font=("goudy old style", 18, "bold"),
            bg="white",
        ).place(x=30, y=230)

        entry_marks = Entry(
            self.root,
            textvariable=self.var_marks,
            font=("goudy old style", 18, "bold"),
            bg="#bca0dc",
        ).place(x=200, y=230, width=330)

        # ------------obtain--marks------------------------------
        lbl_full_marks = Label(
            self.root,
            text="Full Marks",
            font=("goudy old style", 18, "bold"),
            bg="white",
        ).place(x=30, y=280)

        entry_full_marks = Entry(
            self.root,
            textvariable=self.var_fullmarks,
            font=("goudy old style", 18, "bold"),
            bg="#bca0dc",
        ).place(x=200, y=280, width=330)

        # ------------save--clear--button-------------------

        
        self.submit_btn = ImageTk.PhotoImage(file="img/submit.png")
        self.btn1 = Button(self.root, image=self.submit_btn,bd=0,bg="white",cursor='hand2',
            command=self.add_result,
        )
        self.btn1.place(x=250, y=350)
        lbl_clear=Label(self.root, text="Submit", bg="white",font=("goudy old style", 15, "bold")).place(x=230,y=400)

        self.clear_btn = ImageTk.PhotoImage(file="img/clear.png")
        self.btn4 = Button(self.root, image=self.clear_btn,bd=0,bg="white",cursor='hand2',
            command=self.clear,
        )
        self.btn4.place(x=350, y=350, height=40)
        lbl_clear=Label(self.root, text="Clear Entry", bg="white",font=("goudy old style", 15, "bold")).place(x=330,y=400)
        
        # ----------background--image------------------------------------------

        self.bg_img = Image.open("img\MDU_Result.jpg")
        self.bg_img = self.bg_img.resize((600, 360))  # Resize if needed
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.bg_label = Label(self.root, image=self.bg_img)
        self.bg_label.place(x=580, y=70)

    # ---------fetch--data--function ----------------
    def fetch_rollno(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            cur.execute("select rollno from student")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.rollno_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    # ---------search--function---------------------
    def search(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:

            cur.execute(
                "SELECT  name, course from student WHERE rollno=?",
                (self.var_rollno.get(),),
            )
            row = cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    # ------------add-result-----------------------------
    def add_result(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror(
                    "Error", " Name should not be empty", parent=self.root
                )
            else:
                cur.execute(
                    "select * from result where rollno=? and course=?",
                    (self.var_rollno.get(), (self.var_course.get())),
                )
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "Result Already Exists", parent=self.root
                    )
                else:
                    per = round((int(self.var_marks.get()) * 100) / int(self.var_fullmarks.get()), 2
                    )
                    cur.execute(
                        "insert into result (rollno,name,course,marks_ob,full_marks,per) values(?,?,?,?,?,?)",
                        (
                            self.var_rollno.get(),
                            self.var_name.get(),
                            self.var_course.get(),
                            self.var_marks.get(),
                            self.var_fullmarks.get(),
                            str(per),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Result Added Successfully", parent=self.root
                    )

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # -----------clear---function--------
    def clear(self):
        self.var_rollno.set("select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks.set(""),
        self.var_fullmarks.set(""),
#-----------------------------------------------------------
    

# --------------------------------
if __name__ == "__main__":
    root = Tk()
    obj = result_cls(root)
    root.mainloop()
