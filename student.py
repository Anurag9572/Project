from tkinter import*
from tkinter import ttk, messagebox
import tkinter as tk
from PIL import Image,ImageTk 
import mysql.connector
import cv2
import os


class Student:
    def __init__(self,root):    #root -> name of our root window
        self.root = root
        self.root.geometry("1400x750+0+0")    #hight and width of screen and '0+0' for initial of x and y axis
        self.root.title("Face Recognition System")


        # =========== variables ==========================

        self.var_dep = StringVar()
        self.var_sem = StringVar()
        self.var_year = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_sec = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()


        # first image
        img = Image.open(r'D:\FaceRecog_basedAtt_System\images\recg4.jpg')
        img = img.resize((460,110),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb = Label(self.root, image = self.photoimg)
        f_lb.place(x=0, y=0, width=460, height=110)


        img2 = Image.open(r'D:\FaceRecog_basedAtt_System\images\recg8.jpg')
        img2 = img2.resize((460,110),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb = Label(self.root, image = self.photoimg2)
        f_lb.place(x=460, y=0, width=460, height=110)


        img3 = Image.open(r'images\recg9.jpg')
        img3 = img3.resize((460,110),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lb = Label(self.root, image = self.photoimg3)
        f_lb.place(x=920, y=0, width=460, height=110)


        b_img = Image.open(r'images\bg_img.jpg')
        b_img = b_img.resize((1400,640),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(b_img)

        b_lb = tk.Label(self.root, image = self.photoimg4)
        b_lb.place(x=0, y=110, width=1400, height=640)

        title_lbl = Label(b_lb, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        main_frame = tk.Frame(root, bd=2, bg="white")
        main_frame.place(x=20, y=170, width=1330, height=540)

        # left label frame
        Lf_frame = tk.LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="Student Details", font=("times new roman", 12, "bold"))
        Lf_frame.place(x=10, y=10, width=640, height=500)

        img_lf = Image.open(r'images\recg5.jpg')
        img_lf = img_lf.resize((630,110),Image.LANCZOS)
        self.photoimg_lf = ImageTk.PhotoImage(img_lf)

        f_lb = Label(Lf_frame, image = self.photoimg_lf)
        f_lb.place(x=5, y=0, width=630, height=110)

        # current course
        cr_course_frame = LabelFrame(Lf_frame, bd=2, bg="white", relief=RIDGE,text="Current Course Information", font=("times new roman", 12, "bold"))
        cr_course_frame.place(x=10, y=110, width=620, height=120)

        #department
        dep_lbl = Label(cr_course_frame, bg="white", text="Department", font=("times new roman", 12, "bold"))
        dep_lbl.grid(row=0, column=0, padx=10)


        dep_combo = ttk.Combobox(cr_course_frame, textvariable=self.var_dep, font=("times new roman", 12), width=18, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Sci.", "IT", "AI/ML", "CSBS", "Electrical Eng.")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)


        #semester
        sem_lbl = Label(cr_course_frame, bg="white", text="Semester", font=("times new roman", 12, "bold"))
        sem_lbl.grid(row=0, column=2, padx=10, sticky=W)


        sem_combo = ttk.Combobox(cr_course_frame, textvariable=self.var_sem, font=("times new roman", 12), width=18, state="readonly")
        sem_combo["values"] = ("Select Semester", "1st Sem.", "2nd Sem.", "3rd Sem.", "4th Sem.", "5th Sem.", "6th Sem.", "7th Sem.", "8th Sem.")
        sem_combo.current(0)
        sem_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        #year
        yr_lbl = Label(cr_course_frame, bg="white", text="Year", font=("times new roman", 12, "bold"))
        yr_lbl.grid(row=1, column=0, padx=10, sticky=W)


        yr_combo = ttk.Combobox(cr_course_frame, textvariable=self.var_year, font=("times new roman", 12), width=18, state="readonly")
        yr_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        yr_combo.current(0)
        yr_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)


        # Class Student Information
        cls_std_frame = LabelFrame(Lf_frame, bd=2, bg="white", relief=RIDGE,text="Class Student Information", font=("times new roman", 12, "bold"))
        cls_std_frame.place(x=10, y=230, width=620, height=240)

        # student ID
        stdID_lbl = Label(cls_std_frame, bg="white", text="Student ID:", font=("times new roman", 12, "bold"))
        stdID_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        stdID_entry = ttk.Entry(cls_std_frame, textvariable=self.var_id, width=20, font=("times new roman", 12))
        stdID_entry.grid(row=0, column=1, pady=5, sticky=W)

        # student Name
        stdName_lbl = Label(cls_std_frame, bg="white", text="Student Name:", font=("times new roman", 12, "bold"))
        stdName_lbl.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        stdName_entry = ttk.Entry(cls_std_frame, textvariable=self.var_name, width=20, font=("times new roman", 12))
        stdName_entry.grid(row=0, column=3,  padx=2, pady=5, sticky=W)

        # Section
        sec_lbl = Label(cls_std_frame, bg="white", text="Section:", font=("times new roman", 12, "bold"))
        sec_lbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        sec_entry = ttk.Entry(cls_std_frame, textvariable=self.var_sec, width=20, font=("times new roman", 12))
        sec_entry.grid(row=1, column=1, pady=5, sticky=W)

        # Gender
        gdr_lbl = Label(cls_std_frame, bg="white", text="Gender:", font=("times new roman", 12, "bold"))
        gdr_lbl.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        gdr_entry = ttk.Entry(cls_std_frame, textvariable=self.var_gender, width=20, font=("times new roman", 12))
        gdr_entry.grid(row=1, column=3,  padx=2, pady=5, sticky=W)

        # Email
        email_lbl = Label(cls_std_frame, bg="white", text="Email:", font=("times new roman", 12, "bold"))
        email_lbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(cls_std_frame, textvariable=self.var_email, width=20, font=("times new roman", 12))
        email_entry.grid(row=2, column=1, pady=5, sticky=W)

        # Phone no.
        p_no_lbl = Label(cls_std_frame, bg="white", text="Phone no.:", font=("times new roman", 12, "bold"))
        p_no_lbl.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        p_no_entry = ttk.Entry(cls_std_frame, textvariable=self.var_phone, width=20, font=("times new roman", 12))
        p_no_entry.grid(row=2, column=3,  padx=2, pady=5, sticky=W)

        # radio buttons
        self.var_radio1 = StringVar()
        rad_btn1 = ttk.Radiobutton(cls_std_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        rad_btn1.grid(row=3, column=0, padx=10, pady=5)

        self.var_radio2 = StringVar()
        rad_btn2 = ttk.Radiobutton(cls_std_frame, variable=self.var_radio2, text="No Photo Sample", value="No")
        rad_btn2.grid(row=3, column=1, padx=10, pady=5)


        # Buttons Frame
        btn_frame = Frame(cls_std_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=135, width=600, height=70)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=16, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=16, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=16, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=16, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        take_pht_btn = Button(btn_frame, text="Take Photo Sample", command=self.generate_data, width=16, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        take_pht_btn.grid(row=1, column=1)

        update_pht_btn = Button(btn_frame, text="Update Photo Sample", width=16, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_pht_btn.grid(row=1, column=2)


        # Right label frame
        Rg_frame = tk.LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="Student Details", font=("times new roman", 12, "bold"))
        Rg_frame.place(x=670, y=10, width=640, height=500)

        img_rgt = Image.open(r'images\recg5.jpg')
        img_rgt = img_rgt.resize((630,110),Image.LANCZOS)
        self.photoimg_rgt = ImageTk.PhotoImage(img_rgt)

        s_lb = Label(Rg_frame, image = self.photoimg_rgt)
        s_lb.place(x=5, y=0, width=630, height=110)

        # ==================== Search System =========================
        # search_frame = LabelFrame(Rg_frame, bd=2, bg="white", relief=RIDGE,text="Search System", font=("times new roman", 12, "bold"))
        # search_frame.place(x=10, y=110, width=620, height=70)

        # search_lbl = Label(search_frame, bg="pink", text="Search By", font=("times new roman", 12, "bold"), fg="black")
        # search_lbl.grid(row=0, column=0, padx=2, pady=10, sticky=W)


        # search_combo = ttk.Combobox(search_frame, font=("times new roman", 12), width=18, state="readonly")
        # search_combo["values"] = ("Select", "Roll No", "Phone No")
        # search_combo.current(0)
        # search_combo.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        # search_entry = ttk.Entry(search_frame, width=18, font=("times new roman", 12))
        # search_entry.grid(row=0, column=2, padx=2, sticky=W)

        # search_btn = Button(search_frame, text="Search", width=12, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        # search_btn.grid(row=0, column=3, padx=2)

        # showALL_btn = Button(search_frame, text="Show All", width=12, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        # showALL_btn.grid(row=0, column=4, padx=2)
        

        # ==================== Table Frame =========================
        table_frame = Frame(Rg_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=120, width=620, height=340)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "sem", "year", "id", "name", "sec", "gender", "email", "phone"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("sec",text="Section")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone_No")
        self.student_table["show"] = "headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("sec",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


    # ================== function decleration =============================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_sem.get()=="Select Semester" or self.var_year.get()=="Select Year" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_sec.get()=="" or self.var_gender.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Aary@1234", database="face-recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                self.var_dep.get(),
                                                                                                self.var_sem.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_id.get(),
                                                                                                self.var_name.get(),
                                                                                                self.var_sec.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get()
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)


    
    # ======================= fetch data =======================================

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Aary@1234", database="face-recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()


    # ============================== get cursor ===========================================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_sem.set(data[1]),
        self.var_year.set(data[2]),
        self.var_id.set(data[3]),
        self.var_name.set(data[4]),
        self.var_sec.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_email.set(data[7]),
        self.var_phone.set(data[8])


    # =============================== update function =========================================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_sem.get()=="Select Semester" or self.var_year.get()=="Select Year" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_sec.get()=="" or self.var_gender.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Upadate = messagebox.askyesno("Update", "Want to update stutent details", parent=self.root)
                if Upadate>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Aary@1234", database="face-recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,semester=%s,year=%s,Name=%s,Section=%s,Gender=%s,Email=%s,Phone_no=%s where StudentID=%s", (

                                                                                                                                                self.var_dep.get(),
                                                                                                                                                self.var_sem.get(),
                                                                                                                                                self.var_year.get(),
                                                                                                                                                self.var_name.get(),
                                                                                                                                                self.var_sec.get(),
                                                                                                                                                self.var_gender.get(),
                                                                                                                                                self.var_email.get(),
                                                                                                                                                self.var_phone.get(),
                                                                                                                                                self.var_id.get()   
                                                                                                                                            ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)


    # ========================== delete function ===================================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error", "Student ID must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete Page", "Want to delete student", parent=self.root)
                if delete:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Aary@1234", database="face-recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where StudentID=%s"
                    value = (self.var_id.get(),)
                    my_cursor.execute(sql, value)

                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()    
                messagebox.showinfo("Deleted", "Student details successfully deleted", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)


    # ================================ reset function =======================================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_sem.set("Select Semester")
        self.var_year.set("Select Year")
        self.var_id.set("")
        self.var_name.set("")
        self.var_sec.set("")
        self.var_gender.set("")
        self.var_email.set("")
        self.var_phone.set("")


    # ============================ Generate data set or Take photo samples =================================
    def generate_data(self):
        if self.var_dep.get()=="Select Department" or self.var_sem.get()=="Select Semester" or self.var_year.get()=="Select Year" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_sec.get()=="" or self.var_gender.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Aary@1234", database="face-recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                my_result = my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id += 1
                my_cursor.execute("update student set Dep=%s,semester=%s,year=%s,Name=%s,Section=%s,Gender=%s,Email=%s,Phone_no=%s where StudentID=%s", (

                                                                                                                                                self.var_dep.get(),
                                                                                                                                                self.var_sem.get(),
                                                                                                                                                self.var_year.get(),
                                                                                                                                                self.var_name.get(),
                                                                                                                                                self.var_sec.get(),
                                                                                                                                                self.var_gender.get(),
                                                                                                                                                self.var_email.get(),
                                                                                                                                                self.var_phone.get(),
                                                                                                                                                self.var_id.get()==id+1  
                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ========================== load predefined data on frontal face from opencv ===========================
                cap = cv2.VideoCapture(1)
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                img_id =0

                path = "data/train"+str(id)
                os.makedirs(path)

                while(True):
                    ret, img = cap.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)


                    for(x,y,w,h) in faces:
                        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
                        img_id = img_id + 1
                        cv2.imwrite("data/train"+str(id)+"/user."+str(id)+"."+str(img_id)+".jpg", img[y:y+h, x:x+w])
                        cv2.imshow('frame', img)

                    if cv2.waitKey(1) == 13 or int(img_id)==300:
                        break
                    elif img_id > 300:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!", parent=self.root)
            except Exception as es:
                 messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)




if __name__ == "__main__":
    root = tk.Tk()
    obj = Student(root)
    root.mainloop()