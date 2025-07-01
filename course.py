from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import csv
from tkinter import filedialog


class Course:
    def __init__(self, root):
        self.root = root
        self.root.title("Course")
        self.root.geometry("1200x490+80+80")
        self.root.config(bg="#FFDCC9")
        self.root.focus_force()
        self.root.resizable(0, 0)

        # ====title===
        title = Label(
            self.root,
            text="Manage Course Details",
            padx=10,
            compound=LEFT,
            # image=self.logo_dash,
            font=("goudy old style", 20, "bold"),
            bg="#6E3E70",
            # fg="#FFDCC9",
            fg="white",
            
        ).place(x=10, y=12, width=1180, height=38)
        # ==========variable for widget entry===========
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        # ========widget================
        lbl_course_name = Label(
            self.root,
            text="Course Name",
            font=("goudy old style", 15, "bold"),
            bg="#FFDCC9",
            # fg="#fec1a2"
        ).place(x=10, y=60)
        lbl_duration = Label(
            self.root, text="Duration", font=("goudy old style", 15, "bold"), bg="#FFDCC9"
        ).place(x=10, y=100)
        lbl_charges = Label(
            self.root, text="Charges", font=("goudy old style", 15, "bold"), bg="#FFDCC9"
        ).place(x=10, y=140)
        lbl_description = Label(
            self.root,
            text="Description",
            font=("goudy old style", 15, "bold"),
            bg="#FFDCC9",
        ).place(x=10, y=180)
        # ==========Entry fields ========
        self.entry_course_name = Entry(
            self.root,
            textvariable=self.var_course,
            font=("goudy old style", 15, "bold"),
            bg="#bca0dc",
        )
        self.entry_course_name.place(x=150, y=60, width=200)
        entry_duration = Entry(
            self.root,
            textvariable=self.var_duration,
            font=("goudy old style", 15, "bold"),
            bg="#bca0dc",
        ).place(x=150, y=100, width=200)
        entry_charges = Entry(
            self.root,
            textvariable=self.var_charges,
            font=("goudy old style", 15, "bold"),
            bg="#bca0dc",
        ).place(x=150, y=140, width=200)
        self.entry_description = Text(
            self.root, font=("goudy old style", 15, "bold"), bg="#bca0dc"
        )
        self.entry_description.place(x=150, y=180, width=500, height=200)
        # =================BUTTONs=====================

        # --------------------Export file button--------------------------
        self.login_btn = ImageTk.PhotoImage(file="img/export.png")
        btn2 = Button(
            self.root,
            image=self.login_btn,
            bd=0,
            bg="#FFDCC9",
            cursor="hand2",
            command=self.export_data,
        ).place(x=460, y=70)

        lbl_export = Label(self.root, text="Export Data",font=("goudy old style",12,"bold"), bg="#FFDCC9").place(
            x=465, y=150
        )

        # ====================add button =================================
        self.save_btn = ImageTk.PhotoImage(file="img/save3.png")
        self.btn1 = Button(
            self.root,
            image=self.save_btn,
            bd=0,
            bg="#FFDCC9",
            cursor="hand2",
            command=self.add,
        )
        self.btn1.place(x=180, y=400, height=40)
        lbl_save = Label(
            self.root,
            text="Save Course",
            bg="#FFDCC9",
            font=("goudy old style", 12, "bold"),
        ).place(x=165, y=440)

        self.update_btn = ImageTk.PhotoImage(file="img/update3.png")
        self.btn2 = Button(
            self.root,
            image=self.update_btn,
            bd=0,
            bg="#FFDCC9",
            cursor="hand2",
            command=self.update,
        )
        self.btn2.place(x=300, y=400, height=40)
        lbl_update = Label(
            self.root,
            text="Update Course",
            bg="#FFDCC9",
            font=("goudy old style", 12, "bold"),
        ).place(x=270, y=440)

        self.delete_btn = ImageTk.PhotoImage(file="img/delete.png")
        self.btn3 = Button(
            self.root,
            image=self.delete_btn,
            bd=0,
            bg="#FFDCC9",
            cursor="hand2",
            command=self.delete,
        )
        self.btn3.place(x=420, y=400, height=40)
        lbl_delete = Label(
            self.root,
            text="Delete Course",
            bg="#FFDCC9",
            font=("goudy old style", 12, "bold"),
        ).place(x=400, y=440)


        self.clear_btn = ImageTk.PhotoImage(file="img/clear.png")
        self.btn4 = Button(
            self.root,
            image=self.clear_btn,
            bd=0,
            bg="#FFDCC9",
            cursor="hand2",
            command=self.clear,
        )
        self.btn4.place(x=540, y=400, height=40)
        lbl_clear = Label(
            self.root,
            text="Clear Entry",
            bg="#FFDCC9",
            font=("goudy old style", 12, "bold"),
        ).place(x=520, y=440)

        # ==========Search panal================================
        self.var_search = StringVar()
        lbl_search = Label(
            self.root, text="Course", font=("goudy old style", 15, "bold"),bg="#FFDCC9"
        ).place(x=750, y=55)
        entry_search = Entry(
            self.root,
            textvariable=self.var_search,
            font=("goudy old style", 15, "bold"),
            bg="#FFDCC9",  # bca0dc
        )
        entry_search.place(x=820, y=55, width=255, height=28)

        self.search_btn = ImageTk.PhotoImage(file="img/search.png")
        self.btn5 = Button(
            self.root,
            image=self.search_btn,
            bd=0,
            bg="#FFDCC9",
            cursor="hand2",
            command=self.search,
        )
        self.btn5.place(x=1080, y=55)
        lbl_clear = Label(
            self.root, text="Search", bg="#FFDCC9",font=("goudy old style", 14, "bold")
        ).place(x=1120, y=55)

        self.search_frame = Frame(self.root, bd=2, relief=RIDGE)
        self.search_frame.place(x=750, y=100, height=380, width=440)

        # =====Tree view for table===================
        scrolly = Scrollbar(self.search_frame, orient=HORIZONTAL)
        scrollx = Scrollbar(self.search_frame, orient=VERTICAL)

        self.course_table = ttk.Treeview(
            self.search_frame,
            columns=("id", "name", "duration", "charges", "description"),
            xscrollcommand=scrolly.set,
            yscrollcommand=scrollx.set,
        )
        scrolly.pack(side=BOTTOM, fill=X)
        scrollx.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.course_table.yview)
        scrolly.config(command=self.course_table.xview)

        self.course_table.heading("id", text="Course Id")
        self.course_table.heading("name", text="Course Name ")
        self.course_table.heading("duration", text="Duration")
        self.course_table.heading("charges", text="Charges")
        self.course_table.heading("description", text="Description")
        self.course_table["show"] = "headings"
        self.course_table.column("id", width=60)
        self.course_table.column("name", width=100)
        self.course_table.column("duration", width=100)
        self.course_table.column("charges", width=100)
        self.course_table.column("description", width=200)
        self.course_table.pack(fill=BOTH, expand=1)
        self.course_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        # ============================focus on data for filling entry =====

    def get_data(self, ev):
        self.entry_course_name.config(state="readonly")
        r = self.course_table.focus()
        content = self.course_table.item(r)
        row = content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.entry_description.delete("1.0", END)
        self.entry_description.insert(END, row[4])

        # =========================add function for save button========================

    def add(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror(
                    "Error", "Course Name should not be empty", parent=self.root
                )
            else:
                cur.execute(
                    "select * from course where name=?", (self.var_course.get(),)
                )
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "Course Already Exists", parent=self.root
                    )
                else:
                    cur.execute(
                        "insert into course (name,duration,charges,description) values(?,?,?,?)",
                        (
                            self.var_course.get(),
                            self.var_duration.get(),
                            self.var_charges.get(),
                            self.entry_description.get("1.0", END),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Course Added Successfully", parent=self.root
                    )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # =============Show function for showing the data in the table==============
    def show(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course")
            rows = cur.fetchall()
            self.course_table.delete(
                *self.course_table.get_children()
            )  # Clear all items

            for row in rows:
                self.course_table.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()  # Close connection to avoid database lock issues

    # =======================================================================================
    # =================================UPDATE FUNCTION FOR UPDATE DATA =====================
    def update(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror(
                    "Error", "Select course from list ", parent=self.root
                )
            else:
                cur.execute(
                    "select * from course where name=?", (self.var_course.get(),)
                )
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Select course from list ", parent=self.root
                    )
                else:
                    cur.execute(
                        "update course set duration=?,charges=?, description=? where name=?",
                        (
                            self.var_duration.get(),
                            self.var_charges.get(),
                            self.entry_description.get("1.0", END),
                            self.var_course.get(),
                        ),
                    )
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Course updated Successfully", parent=self.root
                    )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    # ====================Clear Function for clear button to clear entry===================
    def clear(self):

        self.var_course.set(""),
        self.var_duration.set(""),
        self.var_charges.set(""),
        self.entry_description.delete("1.0", END),
        self.var_search.set("")
        self.entry_course_name.config(state=NORMAL)
        # self.show()

    # ==================Delete function for delete button ========================================
    def delete(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror(
                    "Error", "Select course from list", parent=self.root
                )
            else:
                cur.execute(
                    "SELECT * FROM course WHERE name=?", (self.var_course.get(),)
                )
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error", "Please select course from the list", parent=self.root
                    )
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you really want to delete?", parent=self.root
                    )
                    if op:
                        cur.execute(
                            "DELETE FROM course WHERE name=?", (self.var_course.get(),)
                        )
                        con.commit()
                        messagebox.showinfo(
                            "Success", "Course deleted successfully", parent=self.root
                        )
                        self.clear()
                        self.show()  # Correct indentation
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    # ====================== Search function for search button=====================
    def search(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            cur.execute(
                f"SELECT * FROM course where name LIKE '%{self.var_search.get()}%'"
            )
            rows = cur.fetchall()
            self.course_table.delete(
                *self.course_table.get_children()
            )  # Clear all items

            for row in rows:
                self.course_table.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    # =======================================================
    def export_data(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course")
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
                            "Course Id",
                            "Course Name",
                            "Duration",
                            "Charges",
                            "Description",
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

    # ---------------------------processing bar ----------------------
    def show_processing(self):
        """Show a processing animation before opening the dashboard"""
        self.process_win = Toplevel(self.root)
        self.process_win.title("Processing...")
        self.process_win.geometry("350x150+500+300")
        self.process_win.config(bg="white")
        self.process_win.grab_set()

        Label(
            self.process_win,
            text="Please wait...",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="green",
        ).pack(pady=10)

        progress = ttk.Progressbar(
            self.process_win, orient=HORIZONTAL, length=250, mode="determinate"
        )
        progress.pack(pady=20)
        progress.start(10)

        # Simulate processing time before opening the dashboard
        self.root.after(3000, self.root)


# ==========================================================================================
if __name__ == "__main__":
    root = Tk()
    obj = Course(root)
    root.mainloop()
