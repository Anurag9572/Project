from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk 
import pandas as pd
import win32com.client as win32
from student import Student
from train_data import Train
from face_recognition import Recognition
import os

class Face_Recognition_System:
    def __init__(self,root):    #root -> name of our root window
        self.root = root
        self.root.geometry("1400x750+0+0")    #hight and width of screen and '0+0' for initial of x and y axis
        self.root.title("Face Recognition System")

        img = Image.open(r'D:\FaceRecog_basedAtt_System\images\fc_reg2.jpg')
        img = img.resize((1400,750),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb = Label(self.root, image = self.photoimg)
        f_lb.place(x=0, y=0, width=1400, height=750)


        title_lbl = Label(f_lb, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="lightblue", fg="red")
        title_lbl.place(x=0,y=0,width=1390,height=70)

        # Student Button
        img2 = Image.open(r'D:\FaceRecog_basedAtt_System\images\recg7.jpg')
        img2 = img2.resize((150,150),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1=tk.Button(root, image=self.photoimg2, command=self.student_details, cursor="hand2")
        b1.place(x=100, y=100, width=150, height=150)

        b1_1 = tk.Button(root, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 14, "bold"), bg="royalblue", fg="black")
        b1_1.place(x=100, y=250, width=150, height=30)

         # Detect face button
        img3 = Image.open(r'D:\FaceRecog_basedAtt_System\images\recg1.jpg')
        img3 = img3.resize((150,150),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b2=tk.Button(root, command=self.recog_face, image=self.photoimg3, cursor="hand2")
        b2.place(x=500, y=100, width=150, height=150)

        b2_2 = tk.Button(root, text="Face Detector", command=self.recog_face, cursor="hand2", font=("times new roman", 14, "bold"), bg="royalblue", fg="black")
        b2_2.place(x=500, y=250, width=150, height=30)

         # Train Data button
        img4 = Image.open(r'D:\FaceRecog_basedAtt_System\images\recg5.jpg')
        img4 = img4.resize((150,150),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b2=tk.Button(root, command=self.train_dataSet, image=self.photoimg4, cursor="hand2")
        b2.place(x=100, y=450, width=150, height=150)

        b2_2 = tk.Button(root, text="Train Data", command=self.train_dataSet, cursor="hand2", font=("times new roman", 14, "bold"), bg="royalblue", fg="black")
        b2_2.place(x=100, y=600, width=150, height=30)

         # Attendance button
        img5 = Image.open(r'images\attd.jpg')
        img5 = img5.resize((150,150),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2=tk.Button(root, command=self.mark_attendance, image=self.photoimg5, cursor="hand2")
        b2.place(x=500, y=450, width=150, height=150)

        b2_2 = tk.Button(root, command=self.mark_attendance, text="Attendance", cursor="hand2", font=("times new roman", 14, "bold"), bg="royalblue", fg="black")
        b2_2.place(x=500, y=600, width=150, height=30)


    # def open_img(self):
    #     os.startfile("data")
    # ================= functions buttons =================================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Student(self.new_window)

    
    def train_dataSet(self):
        self.new_window=Toplevel(self.root)
        self.app = Train(self.new_window)

    def recog_face(self):
        self.new_window=Toplevel(self.root)
        self.app = Recognition(self.new_window)

    def mark_attendance(self):
        csv = pd.read_csv('attendance.csv')
        csv.to_excel('attendance.xlsx', index=False)

        win32c = win32.constants
        excel = win32.gencache.EnsureDispatch('Excel.Application')
        excel.Visible = True
        wb = excel.Workbooks.Open(r'D:\FaceRecog_basedAtt_System\attendance.xlsx') 




if __name__ == "__main__":
    root = tk.Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()