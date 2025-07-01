from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, messagebox
from itertools import cycle
from course import Course  # importing the course file for course window
from student import Student_cls  # importing the student file for student window
from result import result_cls  # importing the result file for result window
from view_result import view_result_cls  # importing the view result file for show
import os


class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("MDU Rohtak")
        self.root.geometry("1370x690+-10+0")
        self.root.config(bg="#9670c7")
        self.root.resizable(0, 0)

        # ===icons===
        self.logo_dash = ImageTk.PhotoImage(file="img/mdu_logo.png")

        # ====title===
        title = Label(
            self.root,
            text="Department of Computer Science & Applications 🔬",
            padx=10,
            compound=LEFT,
            image=self.logo_dash,
            font=("goudy old style", 21, "bold"),
            # bg="#FEC1A2",
            bg="#ce9bce",
            # fg="#6E3E70",
            fg="#391b49",
        ).place(x=0, y=0, relwidth=1, height=80)

        lbl = Label(
            title,
            text="MDU✍️",
            font=("goudy old style", 20, "bold"),
            bg="#ce9bce",
            fg="#391b49",
        ).place(x=15, y=15)
        # =====menu+===
        menu_frame = LabelFrame(
            self.root,
            text="Menu",
            font=("goudy old style", 15),
            bg="#391b49",
            fg="#FFDCC9",
        )
        menu_frame.place(x=20, y=70, width=1340, height=80)
        # bg="#6E3E70"

        # ===buttons===

        course_btn = Button(
            menu_frame,
            text=" Course ",
            font=("goudy old style", 18, "bold"),
            bg="#FFDCC9",
            fg="#391b49",
            cursor="hand2",
            justify=CENTER,
            bd=3,
            relief=RAISED,
            #    activebackground="red",
            command=self.add_course,
        ).place(x=20, y=5, width=200, height=40)
        student_btn = Button(
            menu_frame,
            text="Student ",
            font=("goudy old style", 18, "bold"),
            bg="#FEC1A2",
            fg="#391b49",
            cursor="hand2",
            bd=3,
            relief=RAISED,
            command=self.add_student,
        ).place(x=240, y=5, width=200, height=40)

        result_btn = Button(
            menu_frame,
            text="Add Result",
            font=("goudy old style", 18, "bold"),
            bg="#FBA6A1",
            fg="#391b49",
            cursor="hand2",
            bd=3,
            relief=RAISED,
            command=self.add_result,
        ).place(x=460, y=5, width=200, height=40)
        view_btn = Button(
            menu_frame,
            text="View Result",
            font=("goudy old style", 18, "bold"),
            bg="#FBA6A1",
            fg="#391b49",
            cursor="hand2",
            bd=3,
            relief=RAISED,
            command=self.show_result,
        ).place(x=680, y=5, width=200, height=40)
        logout_btn = Button(
            menu_frame,
            text="Logout",
            font=("goudy old style", 18, "bold"),
            bg="#FEC1A2",
            fg="#391b49",
            cursor="hand2",
            bd=3,
            command=self.logout,
            relief=RAISED,
        ).place(x=900, y=5, width=200, height=40)
        exit_btn = Button(
            menu_frame,
            text="Exit",
            font=("goudy old style", 18, "bold"),
            bg="#FFDCC9",
            fg="#391b49",
            cursor="hand2",
            bd=3,
            relief=RAISED,
            command=self.exit_btn,
        ).place(x=1120, y=5, width=200, height=40)

        # ===Footer===
        footer = Label(
            self.root,
            text="Copyright © 2025 MDU ROHTAK. All right Reserved\nContact Us for any Technical issue: 86xxxxxx27, gauravrajput3xx1@gmail.com",
            font=("goudy old style", 12),
            bg="#262626",
            fg="white",
        )
        footer.pack(side=BOTTOM, fill=X)

        # ================ Slider Section =================
        self.slider_images = [
            # "img/dept_1.jpg",
            "img/2nd.png",
            # "img/3rd.png",
            # "img/4th.png",
            "img/6th.png",
            # "img/dept_2.jpg",
            # "img/dept_3.jpg",
            # "img/dept_4.jpg",
            # "img/dept_6.jpg",
            "img/dept_7.jpg",
            # "img/dept_8.jpg",
            "img/dept_10.jpg",
            "img/activity_center.jpg",
            "img/final.jpg",
            "img/secratery.JPG",
            "img/library_wallpaper.jpg",
        ]  # List of images
        self.current_image_index = 0  # Start with the first image

        # Load and display the first image
        self.bg_img = Image.open(self.slider_images[self.current_image_index])
        self.bg_img = self.bg_img.resize((950, 400))  # Resize if needed
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.bg_label = Label(self.root, image=self.bg_img)
        self.bg_label.place(x=435, y=190, height=400, width=910)

        # Start the slider
        self.update_slider()
        # -----------image section frame-------------------------
        img_frame = Frame(self.root, bd=2, relief=RIDGE).place(x=10, y=10)

        # ----------------------- right frame images section --------------------------
        self.gill_img = Image.open("img/gill.jpg")
        self.gill_img = self.gill_img.resize((110, 100))  # Resize if needed
        self.gill_img = ImageTk.PhotoImage(self.gill_img)

        self.gill_label1 = Button(
            self.root,
            image=self.gill_img,
            bd=2,
            relief=RAISED,
            command=lambda: self.show_profile_card(
                name="Dr. Nasib Sing Gill",
                image=self.gill_img,
                description="Designation : Professor, Department of Computer Science & Applications\n - Director, Centre for Distance and Online Education​\n -Director, Digital Learning Centre\n -Nodal Officer, Academic Bank of Credits",
                extra_info="Email: nasibsgill@gmail.com, nasib.gill@mdurohtak.ac.in\nPhone: +91-1262-293203\nMobile: +91-9050805136",
            ),
        )
        self.gill_label1.place(x=35, y=170)

        # self.gill_label1 = Label(self.root, image=self.gill_img, bd=2, relief=RAISED)
        # self.gill_label1.place(x=35, y=170)
        lbl_gill = Label(
            img_frame,
            text="Dr. Nasib Singh\n(Senior Prof.)",
            font=("goudy old style", 12, "bold"),
            bg="white",
            bd=2,
            relief=RAISED,
        ).place(x=35, y=270, width=115)
        # -----------------------------------------------------------------------

        self.gulliya_img = Image.open("img/gulliya.jpeg")
        self.gulliya_img = self.gulliya_img.resize((110, 100))  # Resize if needed
        self.gulliya_img = ImageTk.PhotoImage(self.gulliya_img)
        self.gulliya_label = Button(
            self.root,
            image=self.gulliya_img,
            bd=2,
            relief=RAISED,
            command=lambda: self.show_profile_card(
                name="Dr. Preeti Guliya",
                image=self.gulliya_img,
                description="Designation : Head of Department\n -Professor, Department of Computer  Science & Applications\n -Deputy Director, Centre for Distance and Online Education\n ",
                extra_info="Email: mdurohtak.ac.in\nPhone: +91-98xxxxxxx1\nRoom No: 101, CS Block",
            ),
        )
        self.gulliya_label.place(x=170, y=170)
        lbl_gulliya = Label(
            img_frame,
            text="Dr. Preeti Gulia\n (Head)",
            font=("goudy old style", 12, "bold"),
            bg="white",
            bd=2,
            relief=RAISED,
        ).place(x=170, y=270, width=115)
        # ----------------------------------------------------------------------------
        self.pooja_img = Image.open("img/pooja.jpeg")
        self.pooja_img = self.pooja_img.resize((110, 100))  # Resize if needed
        self.pooja_img = ImageTk.PhotoImage(self.pooja_img)
        self.pooja_label = Button(
            self.root,
            image=self.pooja_img,
            bd=2,
            relief=RAISED,
            command=lambda: self.show_profile_card(
                name="Dr. Pooja Mittal",
                image=self.pooja_img,
                description="Designation : Assistant Professor, Department of Computer Science & Applications",
                extra_info="Phone: +91-9468110000\nRoom No: 102, CS Block",
            ),
        )
        self.pooja_label.place(x=300, y=170)
        lbl_pooja = Label(
            img_frame,
            text="Dr. Pooja Mittal\n(Ass. Prof.)",
            font=("goudy old style", 12, "bold"),
            bg="white",
            bd=2,
            relief=RAISED,
        ).place(x=300, y=270, width=115)
        # -------------------------------------------------------------------------

        self.balu_img = Image.open("img/balu.jpg")
        self.balu_img = self.balu_img.resize((110, 100))  # Resize if needed
        self.balu_img = ImageTk.PhotoImage(self.balu_img)
        self.balu_label1 = Button(
            self.root,
            image=self.balu_img,
            bd=2,
            relief=RAISED,
            command=lambda: self.show_profile_card(
                name="Dr. Balkishan",
                image=self.balu_img,
                description="Designation : Assistant Professor, Department of Computer Science & Applications",
                extra_info="Email: mdurohtak.ac.in\nPhone: +91-98xxxxxxx1\nRoom No: 103, CS Block",
            ),
        )
        self.balu_label1.place(x=35, y=330)
        lbl_balu = Label(
            img_frame,
            text="Dr. Balkishan \n (Ass. Prof.)",
            font=("goudy old style", 12, "bold"),
            bg="white",
            bd=2,
            relief=RAISED,
        ).place(x=35, y=420, width=115)
        # -------------------------------------------------------------------------------
        self.amrinder_img = Image.open("img/amrindar.jpeg")
        self.amrinder_img = self.amrinder_img.resize((110, 100))  # Resize if needed
        self.amrinder_img = ImageTk.PhotoImage(self.amrinder_img)
        self.amrinder_label = Button(
            self.root,
            image=self.amrinder_img,
            bd=2,
            relief=RAISED,
            command=lambda: self.show_profile_card(
                name="Dr.Amrindar Kaur",
                image=self.amrinder_img,
                description="Designation : Assistant Professor, Department of Computer Science & Applications",
                extra_info="Email: mdurohtak.ac.in\nPhone: +91-98xxxxxxx1\nRoom No: 105, CS Block",
            ),
        )
        self.amrinder_label.place(x=170, y=330)
        lbl_amrinder = Label(
            img_frame,
            text="Dr.Amrinder\n(Ass. Prof.)",
            font=("goudy old style", 12, "bold"),
            bg="white",
            bd=2,
            relief=RAISED,
        ).place(x=170, y=420, width=115)
        # -----------------------------------------------------------------------------
        self.sandeep_img = Image.open("img/sandeep.jpeg")
        self.sandeep_img = self.sandeep_img.resize((110, 100))  # Resize if needed
        self.sandeep_img = ImageTk.PhotoImage(self.sandeep_img)
        self.sandeep_label = Button(
            self.root,
            image=self.sandeep_img,
            bd=2,
            relief=RAISED,
            command=lambda: self.show_profile_card(
                name="Dr.Sandeep Dalal ",
                image=self.sandeep_img,
                description="Designation : Assistant Professor, Department of Computer Science & Applications.",
                extra_info="Email: mdurohtak.ac.in\nPhone: +91-98xxxxxxx1\nRoom No: 104, CS Block",
            ),
        )
        self.sandeep_label.place(x=300, y=330)
        lbl_sandeep = Label(
            img_frame,
            text="Dr. Sandeep \n(Prof.)",
            font=("goudy old style", 12, "bold"),
            bg="white",
            bd=2,
            relief=RAISED,
        ).place(x=300, y=420, width=115)
        # ---------------------------------------------------------------------------------
        self.sukhi_img = Image.open("img/sukhvinder.jpg")
        self.sukhi_img = self.sukhi_img.resize((110, 100))  # Resize if needed
        self.sukhi_img = ImageTk.PhotoImage(self.sukhi_img)
        self.sukhi_label = Button(
            self.root,
            image=self.sukhi_img,
            bd=2,
            relief=RAISED,
            command=lambda: self.show_profile_card(
                name="Dr.Sukhvinder Singh Deora",
                image=self.sukhi_img,
                description="Designation : Assistant Professor, Department of Computer Science & Applications",
                extra_info="Email: nasib.singh@mdurohtak.ac.in\nPhone: +91-98xxxxxxx1\nRoom No: 101, CS Block",
            ),
        )
        self.sukhi_label.place(x=35, y=480)
        lbl_sukhi = Label(
            img_frame,
            text="Dr. Sukhvinder \n(Ass.Prof.)",
            font=("goudy old style", 12, "bold"),
            bg="white",
            bd=2,
            relief=RAISED,
        ).place(x=35, y=580, width=115)
        # ------------------------------------------------------------------------------
        self.gopal_img = Image.open("img/gopal.jpg")
        self.gopal_img = self.gopal_img.resize((110, 100))  # Resize if needed
        self.gopal_img = ImageTk.PhotoImage(self.gopal_img)
        self.gopal_label = Button(
            self.root,
            image=self.gopal_img,
            bd=2,
            relief=RAISED,
            command=lambda: self.show_profile_card(
                name="Dr.Gopal Singh ",
                image=self.gopal_img,
                description="Designation : Assistant Professor, Department of Computer Science & Applications",
                extra_info="Email: nasib.singh@mdurohtak.ac.in\nPhone: +91-1262-393205​\nRoom No: 101, CS Block",
            ),
        )
        self.gopal_label.place(x=170, y=480)
        lbl_gopal = Label(
            img_frame,
            text="Dr.Gopal Singh\n(Ass. Prof.)",
            font=("goudy old style", 12, "bold"),
            bg="white",
            bd=2,
            relief=RAISED,
        ).place(x=170, y=580, width=115)
        # -----------------------------------------------------------------------------------
        self.priti_img = Image.open("img/priti.jpg")
        self.priti_img = self.priti_img.resize((110, 100))  # Resize if needed
        self.priti_img = ImageTk.PhotoImage(self.priti_img)
        self.priti_label = Button(
            self.root,
            image=self.priti_img,
            bd=2,
            relief=RAISED,
            command=lambda: self.show_profile_card(
                name="Dr.Preeti Sharma ",
                image=self.priti_img,
                description="Senior Professor, specializing in Artificial Intelligence and expert in Data Mining.",
                extra_info="Email: nasib.singh@mdurohtak.ac.in\nPhone: +91-98xxxxxxx1\nRoom No: 101, CS Block",
            ),
        )
        self.priti_label.place(x=300, y=480)
        lbl_priti = Label(
            img_frame,
            text="Dr. Priti Sharma \n(Ass. Prof.)",
            font=("goudy old style", 12, "bold"),
            bg="white",
            bd=2,
            relief=RAISED,
        ).place(x=300, y=580, width=115)

    # =================== Slider Function ===================

    def update_slider(self):
        """Function to update slider image every 3 seconds."""
        self.current_image_index = (self.current_image_index + 1) % len(
            self.slider_images
        )  # Loop images
        new_image = Image.open(self.slider_images[self.current_image_index]).resize(
            (910, 400)
        )
        self.bg_img = ImageTk.PhotoImage(new_image)
        self.bg_label.config(image=self.bg_img)  # Update the image in the label
        self.root.after(
            3000, self.update_slider
        )  # Call function every 3 seconds (3000ms)

    # =================ADD WINDOWS FOR DIFFRENT BUTTONS =================
    def add_course(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = Course(self.new_window)

    def add_student(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = Student_cls(self.new_window)

    def add_result(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = result_cls(self.new_window)

    def show_result(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = view_result_cls(self.new_window)

    def export_results(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = view_result_cls(self.new_window)

    def exit_btn(self):
        result = messagebox.askyesno("Confirm", " Are you sure want to exit ? ")
        if result:
            root.destroy()
        else:
            pass

    def logout(self):
        op = messagebox.askyesno(
            "Confirm", "Do you really want to logout?", parent=self.root
        )
        if op == True:
            self.root.destroy()
            os.system("python log_in.py")

    def show_description(self, desc):
        messagebox.showinfo("Faculty Info", desc)

    def show_profile_card(self, name, image, description, extra_info):
        card = Toplevel(self.root)
        card.title(name)
        card.geometry("370x470+600+100")
        card.resizable(False, False)
        card.configure(bg="#fba6a1")  # Light Coral background

        # Card frame with soft rounded look
        card_frame = Frame(
            card,
            bg="#ffffff",
            bd=0,
            highlightbackground="#bc83a4",
            highlightthickness=2,
        )
        card_frame.place(relx=0.5, rely=0.5, anchor="center", width=340, height=440)

        # Image
        img_label = Label(card_frame, image=image, bg="#ffffff")
        img_label.image = image
        img_label.pack(pady=(15, 8))

        # Name
        name_label = Label(
            card_frame,
            text=name,
            font=("Poppins", 16, "bold"),
            bg="#ffffff",
            fg="#6e3e70",
        )
        name_label.pack(pady=(0, 6))

        # Divider line
        Frame(card_frame, bg="#bc83a4", height=2).pack(fill="x", padx=40)

        # Description
        desc_label = Label(
            card_frame,
            text=description,
            wraplength=300,
            font=("Segoe UI", 11),
            bg="#ffffff",
            fg="#3c3c3c",
            justify=LEFT,
        )
        desc_label.pack(pady=(12, 6), padx=15)

        # Extra Info
        extra_label = Label(
            card_frame,
            text=extra_info,
            wraplength=300,
            font=("Calibri", 10, "italic"),
            bg="#ffffff",
            fg="#6e3e70",
            justify=LEFT,
        )
        extra_label.pack(pady=(0, 16), padx=15)

        # Close button
        Button(
            card_frame,
            text="Close",
            command=card.destroy,
            font=("Helvetica", 10, "bold"),
            bg="#6e3e70",
            fg="white",
            activebackground="#bc83a4",
            activeforeground="white",
            relief=FLAT,
            padx=18,
            pady=5,
            cursor="hand2",
        ).pack()


# =============== Run the Application ===============
if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
