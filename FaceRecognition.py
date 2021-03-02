import cv2
from tkinter import *
import os
from tkinter import filedialog,messagebox,Button
import tkinter as tk
from PIL import Image,ImageTk

root = Tk()
menubar = Menu(root)

def Browse():    
    global image_path
    image_path = filedialog.askopenfilename(
                initialdir = os.getcwd(),title = "Select Image File",
                filetypes=(("JPG FILE","*.jpg"),("PNG FILE","*.png"),("ALL FILE","*.*")))

    
    image = Image.open(image_path)
    image.thumbnail((700,400))
    image = ImageTk.PhotoImage(image)
    label.configure(image = image)
    label.image = image
            
def Detect():
    casc_path = "haarcascade_frontalface_default.xml"

    face_Cascade = cv2.CascadeClassifier(casc_path)

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    faces = face_Cascade.detectMultiScale(
        gray,
        scaleFactor = 1,
        minNeighbors = 5,
        minSize = (30,30),
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    Fd =("Found {0} faces".format(len(faces)))
    messagebox.showinfo("Detected",Fd)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Faces Found",image)
    cv2.waitKey(0)
    

label = Label(root)
label.pack()

file = Menu(menubar,tearoff=1)
file.add_command(label="Open",command=Browse)
file.add_command(label="Detect Faces",command=Detect)

file.add_separator()
file.add_command(label="Exit",command=lambda:exit())
menubar.add_cascade(label='File',menu=file)

root.config(menu = menubar)
root.geometry("700x400")
root.title("FaceDetection")
root.mainloop()