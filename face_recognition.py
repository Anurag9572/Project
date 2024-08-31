from tkinter import*
from tkinter import ttk, messagebox
import tkinter as tk
from PIL import Image,ImageTk 
from time import strftime
from datetime import datetime

import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
import mysql.connector
import cv2
import numpy as np


class Recognition:
    def __init__(self,root):    #root -> name of our root window
        self.root = root
        self.root.geometry("1400x750+0+0")    #hight and width of screen and '0+0' for initial of x and y axis
        self.root.title("Face Recognition System")

        img = Image.open(r'images\bg_img.jpg')
        img = img.resize((1400,750),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb = Label(self.root, image = self.photoimg)
        f_lb.place(x=0, y=0, width=1400, height=750)


        img2 = Image.open(r'images\recg3.jpg')
        img2 = img2.resize((250,250),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1=tk.Button(root, image=self.photoimg2, cursor="hand2")
        b1.place(x=880, y=200, width=250, height=250)

        b1_1 = tk.Button(root, text="Face Recognition", command=self.face_recg, cursor="hand2", font=("times new roman", 20, "bold"), bg="darkgreen", fg="black")
        b1_1.place(x=880, y=450, width=250, height=50)


    # =========================attendance =========================================
    def mark_attendance(self, i, n, d, s):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (n not in name_list) and (d not in name_list) and (s not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{s},{dtString},{d1},Present")


    # ===================== face recognition ==============================
    def face_recg(self):

        # Load the pre-trained CNN model
        model = load_model('face_recognition_model.h5')

        # Function to preprocess the image for the CNN model
        def preprocess_image(image):
            image = cv2.resize(image, (224, 224))
            image = image.astype('float32') / 255.0
            image = np.expand_dims(image, axis=0)  # Add batch dimension
            return image

        # Function to predict the face using the CNN model
        def predict_face(model, image, threshold=0.6):
            processed_image = preprocess_image(image)
            predictions = model.predict(processed_image)
            max_index = np.argmax(predictions)
            max_confidence = predictions[0][max_index]
            if max_confidence < threshold:
                return "Unknown", max_confidence
            return max_index, max_confidence
        
        # Load the pre-trained face detector
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Initialize the video capture
        cap = cv2.VideoCapture(0)

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            
            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Detect faces in the frame
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                # Extract the face from the frame
                face = frame[y:y+h, x:x+w]
                
                # Predict the face
                label, confidence = predict_face(model, face)

                # Draw a rectangle around the face and label it
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                if label == "Unknown":
                    cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                else:
                    id = int(label) + 1
                    conn = mysql.connector.connect(host="localhost", username="root", password="Aary@1234", database="face-recognizer")
                    my_cursor = conn.cursor()

                    my_cursor.execute("select StudentID from student where StudentID="+str(id))
                    i = my_cursor.fetchone()
                    i = "+".join(i)

                    my_cursor.execute("select Name from student where StudentID="+str(id))
                    n = my_cursor.fetchone()
                    n = "+".join(n)

                    my_cursor.execute("select Dep from student where StudentID="+str(id))
                    d = my_cursor.fetchone()
                    d = "+".join(d)

                    my_cursor.execute("select Section from student where StudentID="+str(id))
                    s = my_cursor.fetchone()
                    s = "+".join(s)
                    
                    cv2.putText(frame, f'ID: {i}', (x, y-75), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                    cv2.putText(frame, f'Name: {n}', (x, y-55), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                    cv2.putText(frame, f'Department: {d}', (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                    cv2.putText(frame, f'Section: {s}', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                    self.mark_attendance(i, n, d, s)
            

            cv2.imshow('Face Recognition', frame)

            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = tk.Tk()
    obj = Recognition(root)
    root.mainloop()