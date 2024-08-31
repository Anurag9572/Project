from tkinter import*
from tkinter import ttk, messagebox
import tkinter as tk
from PIL import Image,ImageTk 
import mysql.connector
import cv2
import os
import numpy as np

import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.optimizers import Adam



class Train:
    def __init__(self,root):    #root -> name of our root window
        self.root = root
        self.root.geometry("1400x750+0+0")    #hight and width of screen and '0+0' for initial of x and y axis
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="black", fg="lightgreen")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        img = Image.open(r'images\recg11.jpg')
        img = img.resize((1400,210),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb = Label(self.root, image = self.photoimg)
        f_lb.place(x=0, y=45, width=1400, height=210)


        img1 = Image.open(r'images\recg12.webp')
        img1 = img1.resize((1400,500),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb = Label(root, image = self.photoimg1)
        f_lb.place(x=0, y=255, width=1400, height=500)

        # ======= button ========================
        b1_1 = tk.Button(root, text="Train Data", command=self.train_classifier, cursor="hand2", font=("times new roman", 25, "bold"), bg="green", fg="black")
        b1_1.place(x=50, y=250, width=1300, height=50)



    # os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

    def train_classifier(self):
        # path
        data_dir = "data"

        # Define image dimensions and batch size
        IMG_HEIGHT = 224
        IMG_WIDTH = 224
        BATCH_SIZE = 25

        # Data augmentation
        datagen = ImageDataGenerator(
            rescale=1./255,
            validation_split=0.2
        )

        # Load training data
        train_generator = datagen.flow_from_directory(
            data_dir,
            target_size=(IMG_WIDTH, IMG_HEIGHT),
            batch_size=BATCH_SIZE,
            class_mode='categorical',
            subset='training'
        )

        # Load validation data
        validation_generator = datagen.flow_from_directory(
            data_dir,
            target_size=(IMG_WIDTH, IMG_HEIGHT),
            batch_size=BATCH_SIZE,
            class_mode='categorical',
            subset='validation'
        )

        # Define the CNN model
        def create_model(input_shape, num_classes):
            model = Sequential([
                Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
                MaxPooling2D(pool_size=(2, 2)),
                Conv2D(64, (3, 3), activation='relu'),
                MaxPooling2D(pool_size=(2, 2)),
                Conv2D(128, (3, 3), activation='relu'),
                MaxPooling2D(pool_size=(2, 2)),
                Flatten(),
                Dense(128, activation='relu'),
                Dropout(0.5),
                Dense(num_classes, activation='softmax')
            ])
            model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
            return model

        # Define the input shape and number of classes
        input_shape = (IMG_HEIGHT, IMG_WIDTH, 3)
        num_classes = train_generator.num_classes

        # Create the model
        model = create_model(input_shape, num_classes)

        # Print the model summary
        model.summary()


        # Train the model
        history = model.fit(
            train_generator,
            epochs=10,
            validation_data=validation_generator
        )

        # Save the model
        model.save('face_recognition_model.h5')

        # Evaluate the model
        val_loss, val_accuracy = model.evaluate(validation_generator)
        print(f'Validation Loss: {val_loss}')
        print(f'Validation Accuracy: {val_accuracy}')






if __name__ == "__main__":
    root = tk.Tk()
    obj = Train(root)
    root.mainloop()