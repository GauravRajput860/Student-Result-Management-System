from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from tkinter import filedialog
import csv


class Student_cls:
    def __init__(self, root):
        self.root = root
        self.root.title("Student")
        self.root.geometry("1200x490+80+80")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(0, 0)

        # ====title====================

        title = Label(
            self.root,
            text="Manage Student Details",
            padx=10,
            compound=LEFT,
            # image=self.logo_dash,
            font=("goudy old style", 20, "bold"),
            bg="#6E3E70",
            fg="#FFDCC9",
        ).place(x=10, y=12, width=1180, height=38)

        # ==========variable for widget entry=======================================================

        self.var_rollno = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_pincode = StringVar()
        self.var_addmission = StringVar()
        # ========widget===========================================================================

        # --------------left Column lables---------------
        lbl_rollno = Label(
            self.root,
            text="Roll No. ",
            font=("goudy old style", 15, "bold"),
            bg="white",
        ).place(x=10, y=60)
        lbl_name = Label(
            self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white"
        ).place(x=10, y=100)
        lbl_email = Label(
            self.root, text="Email", font=("goudy old style", 15, "bold"), bg="white"
        ).place(x=10, y=140)
        lbl_gender = Label(
            self.root, text="Gender", font=("goudy old style", 15, "bold"), bg="white"
        ).place(x=10, y=180)
        lbl_state = Label(
            self.root, text="State", font=("goudy old style", 15, "bold"), bg="white"
        ).place(x=10, y=220)
        lbl_address = Label(
            self.root,
            text="Address",
            font=("goudy old style", 15, "bold"),
            bg="white",
        ).place(x=10, y=270)
        # -------------right Column lables ----------------

        lbl_dob = Label(
            self.root,
            text="D.O.B ",
            font=("goudy old style", 15, "bold"),
            bg="white",
        ).place(x=340, y=60)

        lbl_contact = Label(
            self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="white"
        ).place(x=340, y=100)

        lbl_addmission = Label(
            self.root,
            text="Addmission",
            font=("goudy old style", 15, "bold"),
            bg="white",
        ).place(x=340, y=140)

        lbl_Course = Label(
            self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white"
        ).place(x=340, y=180)

        lbl_city = Label(
            self.root, text="City", font=("goudy old style", 15, "bold"), bg="white"
        ).place(x=250, y=220)

        lbl_pincode = Label(
            self.root, text="Pincode", font=("goudy old style", 15, "bold"), bg="white"
        ).place(x=450, y=220)

        # ==========Entry fields =============================================================
        self.course_list = []
        self.fetch_course()
        # -----------left entry---------------------
        self.entry_rollno = Entry(
            self.root,
            textvariable=self.var_rollno,
            font=("goudy old style", 15, "bold"),
            bg="#bca0dc",
            # bd=3,
            # relief=RAISED,
        )
        self.entry_rollno.place(x=120, y=60, width=200)
        self.entry_name = Entry(
            self.root,
            textvariable=self.var_name,
            font=("goudy old style", 15, "bold"),
            bg="#bca0dc",
        ).place(x=120, y=100, width=200)
        self.entry_email = Entry(
            self.root,
            textvariable=self.var_email,
            font=("goudy old style", 15, "bold"),
            bg="#bca0dc",
        ).place(x=120, y=140, width=200)

        self.entry_gender = ttk.Combobox(
            self.root,
            textvariable=self.var_gender,
            font=("goudy old style", 15, "bold"),
            justify=CENTER,
            values=("Select", "Male", "Female", "Other"),
        )
        self.entry_gender.place(x=120, y=180, width=200)
        self.entry_gender.current(0)

        self.entry_state = Entry(
            self.root,
            textvariable=self.var_state,
            font=("goudy old style", 15, "bold"),
            bg="#bca0dc",
        ).place(x=120, y=220, width=120)

        self.entry_address = Text(
            self.root, font=("goudy old style", 15, "bold"), bg="#bca0dc"
        )
        self.entry_address.place(x=120, y=270, width=530, height=120)

        # -------------Right Entry---------------------------

        self.entry_dob = Entry(
            self.root,
            textvariable=self.var_dob,
            font=("goudy old style", 15, "bold"),
            bg="#bca0dc",
        )
        self.entry_dob.place(x=450, y=60, width=200)

        self.entry_contact = Entry(
            self.root,
            textvariable=self.var_contact,
            font=("goudy old style", 15, "bold"),
            bg="#bca0dc",
        ).place(x=450, y=100, width=200)

        self.entry_addmission = Entry(
            self.root,
            textvariable=self.var_addmission,
            font=("goudy old style", 15, "bold"),
            bg="#bca0dc",
        ).place(x=450, y=140, width=200)

        self.entry_course = ttk.Combobox(
            self.root,
            textvariable=self.var_course,
            font=("goudy old style", 15, "bold"),
            justify=CENTER,
            values=(self.course_list),
        )
        self.entry_course.place(x=450, y=180, width=200)
        self.entry_course.set("Select")

        self.entry_city = Entry(
            self.root,
            textvariable=self.var_city,
            font=("goudy old style", 15, "bold"),
            bg="#bca0dc",
        ).place(x=300, y=220, width=120)

        self.entry_pincode = Entry(
            self.root,
            textvariable=self.var_pincode,
            font=("goudy old style", 15, "bold"),
            bg="#bca0dc",
        ).place(x=530, y=220, width=120)

        # =================BUTTONs============================================================


        self.save_btn = ImageTk.PhotoImage(file="img/save3.png")
        self.btn1 = Button(
            self.root,
            image=self.save_btn,
            bd=0,
            bg="white",
            cursor="hand2",
            command=self.add,
        )
        self.btn1.place(x=150, y=400, height=40)
        lbl_save = Label(
            self.root,
            text="Add Student",
            bg="white",
            font=("goudy old style", 12, "bold"),
        ).place(x=135, y=440)


        self.update_btn = ImageTk.PhotoImage(file="img/update3.png")
        self.btn2 = Button(
            self.root,
            image=self.update_btn,
            bd=0,
            bg="white",
            cursor="hand2",
            command=self.update,
        )
        self.btn2.place(x=280, y=400, height=40)
        lbl_update = Label(
            self.root,
            text="Update Student",
            bg="white",
            font=("goudy old style", 12, "bold"),
        ).place(x=250, y=440)


        self.delete_btn = ImageTk.PhotoImage(file="img/delete.png")
        self.btn3 = Button(
            self.root,
            image=self.delete_btn,
            bd=0,
            bg="white",
            cursor="hand2",
            command=self.delete,
        )
        self.btn3.place(x=420, y=400, height=40)
        lbl_delete = Label(
            self.root,
            text="Delete Record",
            bg="white",
            font=("goudy old style", 12, "bold"),
        ).place(x=400, y=440)


        self.clear_btn = ImageTk.PhotoImage(file="img/clear.png")
        self.btn4 = Button(
            self.root,
            image=self.clear_btn,
            bd=0,
            bg="white",
            cursor="hand2",
            command=self.clear,
        )
        self.btn4.place(x=540, y=400, height=40)
        lbl_clear = Label(
            self.root,
            text="Clear Entry",
            bg="white",
            font=("goudy old style", 12, "bold"),
        ).place(x=520, y=440)

        self.export_btn = ImageTk.PhotoImage(file="img/export.png")
        btn6 = Button(
            self.root,
            image=self.export_btn,
            bd=0,
            bg="white",
            cursor="hand2",
            command=self.export_data,
        ).place(x=20, y=360)

        lbl_export = Label(self.root, text="Export Data", bg="white").place(x=20, y=440)

        # ==========Search panal========================================

        self.var_search = StringVar()
        lbl_search = Label(
            self.root, text="Roll No", font=("goudy old style", 15, "bold"), bg="white"
        )
        lbl_search.place(x=750, y=55)

        entry_search = Entry(
            self.root,
            textvariable=self.var_search,
            font=("goudy old style", 15, "bold"),
            bg="#bca0dc",
            bd=3,
            relief=RAISED,
        )
        entry_search.place(x=830, y=55, width=240, height=30)

        # search_btn = Button(
        #     self.root,
        #     text="Search",
        #     font=("goudy old style", 15, "bold"),
        #     bg="#F39c12",
        #     fg="white",
        #     cursor="hand2",
        #     bd=3,
        #     relief=RAISED,
        #     command=self.search,
        # ).place(x=1080, y=55, width=110, height=30)

        self.search_btn = ImageTk.PhotoImage(file="img/search.png")
        self.btn5 = Button(
            self.root,
            image=self.search_btn,
            bd=0,
            bg="white",
            cursor="hand2",
            command=self.search,
        )
        self.btn5.place(x=1080, y=55)
        lbl_clear = Label(
            self.root, text="Search", bg="white", font=("goudy old style", 14, "bold")
        ).place(x=1120, y=55)

        self.search_frame = Frame(self.root, bd=5, relief=RAISED)
        self.search_frame.place(x=700, y=100, height=380, width=490)

        # =====Tree view for ====================================================================

        scrolly = Scrollbar(self.search_frame, orient=HORIZONTAL)
        scrollx = Scrollbar(self.search_frame, orient=VERTICAL)

        self.rollno_table = ttk.Treeview(
            self.search_frame,
            columns=(
                "rollno",
                "name",
                "email",
                "gender",
                "state",
                "dob",
                "contact",
                "addmission",
                "course",
                "address",
                "city",
                "pincode",
            ),
            xscrollcommand=scrolly.set,
            yscrollcommand=scrollx.set,
        )
        scrolly.pack(side=BOTTOM, fill=X)
        scrollx.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.rollno_table.yview)
        scrolly.config(command=self.rollno_table.xview)

        self.rollno_table.heading("rollno", text="Roll No.")
        self.rollno_table.heading("name", text="Name ")
        self.rollno_table.heading("email", text="Email")
        self.rollno_table.heading("gender", text="Gender")
        self.rollno_table.heading("state", text="State")
        self.rollno_table.heading("dob", text="DOB")
        self.rollno_table.heading("contact", text="Contact")
        self.rollno_table.heading("addmission", text="Addmission")
        self.rollno_table.heading("course", text="Course")
        self.rollno_table.heading("address", text="Address")
        self.rollno_table.heading("city", text="City")
        self.rollno_table.heading("pincode", text="Pincode")
        self.rollno_table["show"] = "headings"
        self.rollno_table.column("rollno", width=100)
        self.rollno_table.column("name", width=100)
        self.rollno_table.column("email", width=200)
        self.rollno_table.column("gender", width=100)
        self.rollno_table.column("state", width=100)
        self.rollno_table.column("dob", width=100)
        self.rollno_table.column("contact", width=100)
        self.rollno_table.column("addmission", width=100)
        self.rollno_table.column("course", width=200)
        self.rollno_table.column("city", width=100)
        self.rollno_table.column("pincode", width=100)
        self.rollno_table.column("address", width=200)
        self.rollno_table.pack(fill=BOTH, expand=1)
        self.rollno_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    # ============================focus on data for filling entry ===================

    def get_data(self, ev):
        self.entry_rollno.config(state="readonly")
        r = self.rollno_table.focus()
        content = self.rollno_table.item(r)
        row = content["values"]

        if row:
            self.var_rollno.set(row[0])  # Corrected index
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_state.set(row[4])
            self.var_dob.set(row[5])
            self.var_contact.set(row[6])
            self.var_addmission.set(row[7])
            self.var_course.set(row[8])
            self.entry_address.delete("1.0", END)
            self.entry_address.insert(END, row[9])
            self.var_city.set(row[10])
            self.var_pincode.set(row[11])

    # =========================add function for save button====================

    def add(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            if self.var_rollno.get() == "":
                messagebox.showerror(
                    "Error", "Roll No. should not be empty", parent=self.root
                )
            else:
                cur.execute(
                    "select * from student where rollno=?", (self.var_rollno.get(),)
                )
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "Roll No. Already Exists", parent=self.root
                    )
                else:
                    cur.execute(
                        "insert into student(rollno,name ,email  ,gender  ,state  ,dob  ,contact  ,addmission  ,course  ,address  ,city  ,   pincode  ) values(?,?,?,?,?,?,?,?,?,?,?,?)",
                        (
                            self.var_rollno.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_state.get(),
                            self.var_dob.get(),
                            self.var_contact.get(),
                            self.var_addmission.get(),
                            self.var_course.get(),
                            self.entry_address.get("1.0", END),
                            self.var_city.get(),
                            self.var_pincode.get(),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Student Added Successfully", parent=self.root
                    )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # =============Show function for showing the data in the table======================================

    def show(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()
            self.rollno_table.delete(
                *self.rollno_table.get_children()
            )  # Clear all items

            for row in rows:
                self.rollno_table.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()  # Close connection to avoid database lock issues

    # =====================================================================================================

    # ==================UPDATE FUNCTION FOR UPDATE DATA =====================
    def update(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            if self.var_rollno.get() == "":
                messagebox.showerror(
                    "Error", "Select Student from list ", parent=self.root
                )
            else:
                cur.execute(
                    "select * from student where rollno=?", (self.var_rollno.get(),)
                )
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Select Student from list ", parent=self.root
                    )
                else:
                    cur.execute(
                        "UPDATE student SET name=?, email=?, gender=?, state=?, dob=?, contact=?, addmission=?, course=?, address=?, city=?, pincode=? WHERE rollno=?",
                        (
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_state.get(),
                            self.var_dob.get(),
                            self.var_contact.get(),
                            self.var_addmission.get(),
                            self.var_course.get(),
                            self.entry_address.get("1.0", END),
                            self.var_city.get(),
                            self.var_pincode.get(),
                            self.var_rollno.get(),
                        ),
                    )
                con.commit()
                messagebox.showinfo(
                    "Success", "Student updated Successfully", parent=self.root
                )
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # ====================Clear Function for clear button to clear entry===============
    def clear(self):

        self.var_rollno.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("select"),
        self.var_dob.set(""),
        self.var_city.set(""),
        self.var_state.set(""),
        self.var_addmission.set(""),
        self.var_contact.set(""),
        self.var_pincode.set(""),
        self.var_course.set("select"),
        self.entry_address.delete("1.0", END),
        self.var_search.set("")
        self.entry_rollno.config(state=NORMAL)
        # self.show()

    # ==================Delete function for delete button ========================
    def delete(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            if self.var_rollno.get() == "":
                messagebox.showerror(
                    "Error", "Select rollno from list", parent=self.root
                )
            else:
                cur.execute(
                    "SELECT * FROM student WHERE rollno=?", (self.var_rollno.get(),)
                )
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error", "Please select rollno from the list", parent=self.root
                    )
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you really want to delete?", parent=self.root
                    )
                    if op:
                        cur.execute(
                            "DELETE FROM student WHERE rollno=?",
                            (self.var_rollno.get(),),
                        )
                        con.commit()
                        messagebox.showinfo(
                            "Success", "rollno deleted successfully", parent=self.root
                        )
                        self.clear()
                        self.show()  # Correct indentation
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    # ----------------------------fetch_course---------------------------------------------

    def fetch_course(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            cur.execute("select name from course")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    # ====================== Search function for search button===============================================

    def search(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:

            if self.var_search.get() == "":
                messagebox.showerror(
                    "Error", "Roll No. should not be empty", parent=self.root
                )
            else:
                cur.execute(
                    "SELECT * FROM student WHERE rollno=?", (self.var_search.get(),)
                )
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "No record found", parent=self.root)
                else:
                    self.rollno_table.delete(
                        *self.rollno_table.get_children()
                    )  # Clear previous data
                    self.rollno_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

        # =======================================================

    def export_data(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()

            if not rows:
                messagebox.showwarning(
                    "No Data", "No data found to export", parent=self.root
                )
                return

            file_path = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv")],
                title="Save file",
            )

            if file_path:
                with open(file_path, mode="w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        [
                            "Roll No",
                            "Name",
                            "Email",
                            "Gender",
                            "State",
                            "DOB",
                            "Contact",
                            "Addmission",
                            "Course",
                            "Address",
                            "City",
                            "Pincode",
                        ]
                    )  # Column headers
                    writer.writerows(rows)  # Writing data rows

                messagebox.showinfo(
                    "Success",
                    f"Data successfully exported to {file_path}",
                    parent=self.root,
                )

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()


# ============================================================================================
if __name__ == "__main__":
    root = Tk()
    obj = Student_cls(root)
    root.mainloop()
