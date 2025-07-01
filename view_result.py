from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import csv
from tkinter import filedialog

class view_result_cls:
    def __init__(self, root):
        self.root = root
        self.root.title(" Result Panel ")
        self.root.geometry("1250x450+80+80")
        self.root.config(bg="#FFDCC9")
        self.root.focus_force()
        self.root.resizable(0, 0)

        # ====title===
        title = Label(
            self.root,
            text="View Students Result",
            padx=30,
            compound=LEFT,
            # image=self.logo_dash,
            font=("goudy old style", 18, "bold"),
            bg="#6E3E70",
            fg="white",
            # fg="#FBA6A1",
        ).place(x=10, y=15, width=1230, height=50)
        # ---------------variables----------------------
        self.var_search = StringVar()
        self.var_id = ""
        # -----------serach_by_rollno_---------------------------
        lbl_search = Label(
            self.root,
            text="Search by Roll No.",
            font=("goudy old style", 18, "bold"),
            bg="#FFDCC9",
        ).place(x=280, y=100)

        entry_search = Entry(
            self.root,
            textvariable=self.var_search,
            font=("goudy old style", 18, "bold"),
            #   state="readonly",
            bg="#bca0dc",
            fg='black'
        ).place(x=480, y=100, width=200)

        # --------------button---------------------
        self.certificate_btn = ImageTk.PhotoImage(file="img/certficate_icon.png")  # you can design a small certificate icon
        btn_certificate = Button(
    self.root,
    image=self.certificate_btn,
    bd=0,
    bg="#FFDCC9",
    cursor="hand2",
    command=self.show_certificate,
)
        btn_certificate.place(x=1050, y=70)

        lbl_certificate = Label(
    self.root,
    text="Show Certificate",
    font=("goudy old style", 12, "bold"),
    bg="#FFDCC9",
).place(x=1030, y=150)



        self.search_btn = ImageTk.PhotoImage(file="img/search.png")
        self.btn5 = Button(self.root, image=self.search_btn,bd=0,bg="#FFDCC9",cursor='hand2',
            command=self.search,
        )
        self.btn5.place(x=690, y=100)
        lbl_clear=Label(self.root, text="Search", bg="#FFDCC9",font=("goudy old style", 14, "bold")).place(x=730, y=100)

        self.clear_btn = ImageTk.PhotoImage(file="img/clear.png")
        self.btn4 = Button(self.root, image=self.clear_btn,bd=0,bg="#FFDCC9",cursor='hand2',
            command=self.clear,
        )
        self.btn4.place(x=700, y=360, height=40)
        lbl_clear=Label(self.root, text="Clear Entry", bg="#FFDCC9",font=("goudy old style", 14, "bold")).place(x=680,y=400)



        self.delete_btn = ImageTk.PhotoImage(file="img/delete.png")
        self.btn3 = Button(self.root, image=self.delete_btn,bd=0,bg="#FFDCC9",cursor='hand2',
            command=self.delete,
        )
        self.btn3.place(x=530, y=360, height=40)
        lbl_delete=Label(self.root, text="Delete Record", bg="#FFDCC9",font=("goudy old style", 14, "bold")).place(x=500,y=400)


        self.login_btn = ImageTk.PhotoImage(file="img/csv.png")
        btn2 = Button(
            self.root,
            image=self.login_btn,
            bd=0,
            bg="#FFDCC9",
            cursor="hand2",
            command=self.export_results,
        ).place(x=880, y=70)

        lbl_export = Label(self.root, text="Export All Results",font=("goudy old style",12,"bold"), bg="#FFDCC9").place(
            x=865, y=150
        )

        # --------------result_lables----------------------------------
        lbl_rollno = Label(
            self.root,
            text="Roll No.",
            font=("goudy old style", 18, "bold"),
            bg="#fba6a1",
            bd=2,
            relief=GROOVE,
        ).place(x=20, y=230, height=50, width=200)

        lbl_name = Label(
            self.root,
            text="Name",
            font=("goudy old style", 18, "bold"),
            bg="#fba6a1",
            bd=2,
            relief=GROOVE,
        ).place(x=220, y=230, height=50, width=200)

        lbl_course = Label(
            self.root,
            text="Course",
            font=("goudy old style", 18, "bold"),
            bg="#fba6a1",
            bd=2,
            relief=GROOVE,
        ).place(x=420, y=230, height=50, width=200)

        lbl_marks = Label(
            self.root,
            text=" Obtained Marks",
            font=("goudy old style", 18, "bold"),
            bg="#fba6a1",
            bd=2,
            relief=GROOVE,
        ).place(x=620, y=230, height=50, width=200)

        lbl_full_marks = Label(
            self.root,
            text="Total Marks",
            font=("goudy old style", 18, "bold"),
            bg="#fba6a1",
            bd=2,
            relief=GROOVE,
        ).place(x=820, y=230, height=50, width=200)

        lbl_per = Label(
            self.root,
            text="Percent",
            font=("goudy old style", 18, "bold"),
            bg="#fba6a1",
            bd=2,
            relief=GROOVE,
        ).place(x=1020, y=230, height=50, width=200)

        # -------------------lower labels ----------------------
        self.rollno = Label(
            self.root,
            font=("goudy old style", 18, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE,
        )
        self.rollno.place(x=20, y=280, height=50, width=200)

        self.name = Label(
            self.root,
            font=("goudy old style", 18, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE,
        )
        self.name.place(x=220, y=280, height=50, width=200)

        self.course = Label(
            self.root,
            font=("goudy old style", 18, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE,
        )
        self.course.place(x=420, y=280, height=50, width=200)

        self.marks = Label(
            self.root,
            font=("goudy old style", 18, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE,
        )
        self.marks.place(x=620, y=280, height=50, width=200)

        self.full_marks = Label(
            self.root,
            font=("goudy old style", 18, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE,
        )
        self.full_marks.place(x=820, y=280, height=50, width=200)

        self.per = Label(
            self.root,
            font=("goudy old style", 18, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE,
        )
        self.per.place(x=1020, y=280, height=50, width=200)
    # ---------------------------------
    def show_certificate(self):
        if self.rollno.cget("text") == "":
            messagebox.showerror("Error", "No result selected to show Certificate", parent=self.root)
            return

        self.cert_window = Toplevel(self.root)   # <- Made it self.cert_window for access inside other functions
        self.cert_window.title("Student Result Certificate")
        self.cert_window.geometry("600x600+400+50")
        self.cert_window.config(bg="white")
        self.cert_window.resizable(0, 0)

        title = Label(self.cert_window, text="Certificate of Achievement", font=("times new roman", 24, "bold"), bg="white", fg="#6E3E70")
        title.pack(pady=20)

        line = Label(self.cert_window, text="---------------------------------------------------------", font=("times new roman", 18), bg="white", fg="#6E3E70")
        line.pack()

        self.lbl_name = Label(self.cert_window, text=f"Presented to: {self.name.cget('text')}", font=("times new roman", 20, "bold"), bg="white")
        self.lbl_name.pack(pady=20)

        self.lbl_course = Label(self.cert_window, text=f"For successfully completing the course: {self.course.cget('text')}", font=("times new roman", 16), bg="white")
        self.lbl_course.pack(pady=10)

        self.lbl_marks = Label(self.cert_window, text=f"Marks Obtained: {self.marks.cget('text')} / {self.full_marks.cget('text')}", font=("times new roman", 16), bg="white")
        self.lbl_marks.pack(pady=10)

        self.lbl_per = Label(self.cert_window, text=f"Percentage: {self.per.cget('text')}", font=("times new roman", 16), bg="white")
        self.lbl_per.pack(pady=10)

        self.lbl_rollno = Label(self.cert_window, text=f"Roll Number: {self.rollno.cget('text')}", font=("times new roman", 16), bg="white")
        self.lbl_rollno.pack(pady=10)

        footer = Label(self.cert_window, text="Congratulations on your achievement!", font=("times new roman", 18, "italic"), bg="white", fg="#6E3E70")
        footer.pack(pady=30)

        # Buttons Frame
        btn_frame = Frame(self.cert_window, bg="white")
        btn_frame.pack(pady=10)

        print_btn = Button(btn_frame, text="Print", command=self.print_certificate, font=("goudy old style", 14, "bold"), bg="#27ae60", fg="white", cursor="hand2")
        print_btn.grid(row=0, column=0, padx=10)

        close_btn = Button(btn_frame, text="Close", command=self.cert_window.destroy, font=("goudy old style", 14, "bold"), bg="#e74c3c", fg="white", cursor="hand2")
        close_btn.grid(row=0, column=1, padx=10)
    # ------------------------------------------------
    
    
    def print_certificate(self):
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.pdfgen import canvas
            from reportlab.lib.units import inch
            import tempfile
            import os
            from tkinter.filedialog import asksaveasfilename

            # Create temporary PDF file
            temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
            temp_pdf_path = temp_pdf.name
            temp_pdf.close()

            c = canvas.Canvas(temp_pdf_path, pagesize=A4)
            width, height = A4

            # --------------- Draw Border -------------------
            c.setStrokeColorRGB(0.8, 0.5, 0.2)  # Golden color
            c.setLineWidth(8)
            c.rect(30, 30, width-60, height-60)

            # --------------- Add Logo ----------------------
            try:
                c.drawImage("img/university_logo.png", width/2 - 50, 670, width=100, height=100, preserveAspectRatio=True)
            except:
                pass  # In case logo not found, ignore.
            
            # --------------- Title ------------------------
            c.setFont("Helvetica-Bold", 30)
            c.setFillColorRGB(0.2, 0.3, 0.7)
            c.drawCentredString(width/2, height - 170 -40, "Certificate of Achievement")  # Reduced y by 20

            # ----------- Decorative Line ----------
            c.setLineWidth(1)
            c.line(100, height-180 -40, width-100, height-180 -40)  # Reduced y by 20

            # --------------- Recipient Name -----------------
            c.setFont("Helvetica", 18)
            c.setFillColorRGB(0,0,0)
            c.drawCentredString(width/2, height - 230 -40, "This is proudly presented to")  # Reduced y by 20

            c.setFont("Helvetica-Bold", 24)
            c.drawCentredString(width/2, height - 270 -40, self.name.cget("text"))  # Reduced y by 20

            # --------------- Course Name -------------------
            c.setFont("Helvetica", 18)
            c.drawCentredString(width/2, height - 310 -40, f"For completing the course")  # Reduced y by 20

            c.setFont("Helvetica-Bold", 20)
            c.drawCentredString(width/2, height - 340 -40, self.course.cget("text"))  # Reduced y by 20

           
            
           # --------------- Performance Paragraph -------------------
            # Prepare the values for the paragraph
            n=self.name.cget("text")
            roll = self.rollno.cget("text")
            course = self.course.cget("text")
            marks = self.marks.cget("text")
            full = self.full_marks.cget("text")
            percent = self.per.cget("text")

            
            lines = [
    f"Mr./Ms. {n} has successfully completed the {course}",
    f"course with excellence.They achieved a score of {marks} out of {full},",
    f"showcasing their hard work and determination with an impressive",
    f"overall percentage of {percent}%. They have proven their dedication.",
     "Throughout the duration of the course, they demonstrated",
    " outstanding, participation a strong grasp of the subject matter,  ",
    "and a sincere commitment to academic excellence."
]


            # Create a text object for the paragraph
            text = c.beginText(70, height - 400 - 40)  # 40 is your earlier vertical shift
            text.setFont("Times-Roman", 18)  # Italic font for emphasis
            text.setFillColorRGB(0.2,0.4,0.8)  # Soft blue color for the text
            text.setLeading(22)  # Line spacing

            # Add each line to the paragraph
            for line in lines:
                text.textLine(line)

            # Draw the text object onto the PDF
            c.drawText(text)

            # Optional: Add bold emphasis to specific parts of the paragraph
            c.setFont("Helvetica-Bold", 14)  # Switch to bold font for specific lines or words
            c.setFillColorRGB(0.8, 0.2, 0.2)  # Bold red color to highlight key points

            # Draw specific bold lines or words, such as the marks or percentage
            c.drawString(100, height - 470-130, f"Marks: {marks}/{full}")
            c.drawString(width - 200 , height - 470 -130, f"Percentage: {percent}%")

            # Return to original style after bold
            c.setFont("Helvetica-Oblique", 14)
            c.setFillColorRGB(0.2, 0.4, 0.8)  # Reset to original color

            # --------------- Badge Image ----------------------
            try:
                c.drawImage("img/medal2.png", 50, 718, width=100, height=100, preserveAspectRatio=True)  # Keep original position
            except:
                pass

            # --------------- Signature ------------------------
            try:
                c.drawImage("img/signature2.png", width-200, 80, width=150, height=50, preserveAspectRatio=True)  # Keep original position
            except:
                pass

            # Signature Text
            c.setFont("Helvetica-Oblique", 12)
            
            c.drawCentredString(width-130, 80, " Head of Dept.")  # Keep original position
            c.drawCentredString(width-130, 60, " Authorized Signature")  # Keep original position

            c.save()

            # --------------- Save PDF -------------------
            save_path = asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

            if save_path:
                os.rename(temp_pdf_path, save_path)  # Save the file to the chosen path
                messagebox.showinfo("Success", f"Certificate saved as {save_path}", parent=self.cert_window)
            else:
                os.remove(temp_pdf_path)  # Delete the temporary file if user cancels the save dialog

        except Exception as ex:
            messagebox.showerror("Error", f"Error during saving the certificate: {str(ex)}", parent=self.cert_window)


    # -------------serarch function-------------------------
    def search(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Roll no. should be required",parent=self.root)
            else:
                cur.execute(
                    "SELECT  * from result WHERE rollno=?", (self.var_search.get(),)
                )
                row = cur.fetchone()
                if row != None:
                    self.var_id = row[0]
                    self.rollno.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full_marks.config(text=row[5])
                    self.per.config(text=row[6])
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

        # ----------clear function -------------

    def clear(self):
        self.var_id = ""
        self.rollno.config(text=" ")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full_marks.config(text="")
        self.per.config(text="")
        self.var_search.set("")

    # ------------delete funtion -----------------------

    def delete(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            if self.var_id == "":
                messagebox.showerror("Error", "Select record first", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE rid=?", (self.var_id,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error", "Invalid student result", parent=self.root
                    )
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you really want to delete?", parent=self.root
                    )
                    if op:
                        cur.execute("DELETE FROM result WHERE rid=?", (self.var_id,))
                        con.commit()
                        messagebox.showinfo(
                            "Success", "Result deleted successfully", parent=self.root
                        )
                        self.clear()
                        # self.show()# Correct indentation
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def export_results(self):
        con = sqlite3.connect(database="srms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM result")
            rows = cur.fetchall()

            if not rows:
                messagebox.showwarning(
                "No Data", "No results found to export", parent=self.root
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
                    # Write column headers dynamically
                    headers = [description[0] for description in cur.description]
                    writer.writerow(headers)
                    writer.writerows(rows)

                messagebox.showinfo(
                "Success",
                f"Results successfully exported to {file_path}",
                parent=self.root,
            )

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()


if __name__ == "__main__":
    root = Tk()
    obj = view_result_cls(root)
    root.mainloop()
