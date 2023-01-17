from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Student import student
from trainData import trainData
from faceRecognizer import faceRecog
import os


class FaceRecog:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        root.state('zoomed')
        # header Image 1
        headerImg = Image.open("Images/frsheader.png")
        headerImg = headerImg.resize((1920, 200), Image.ANTIALIAS)
        self.firstImage = ImageTk.PhotoImage(headerImg)
        self.firstlbl = Label(self.root, image=self.firstImage)
        self.firstlbl.pack(fill=BOTH, expand=YES)

        # Main Image
        img = Image.open("Images/bg1.png")
        img = img.resize((1920, 800), Image.ANTIALIAS)
        self.mainImage = ImageTk.PhotoImage(img)
        mainImgLbl = Label(self.root, image=self.mainImage)
        mainImgLbl.pack(fill=BOTH, expand=YES)

        # adding title
        titleLable = Label(self.root, text="Face Attendance System", font=("time new roman", 28, "bold"), fg="red")
        titleLable.place(x=0, y=220, width=1920, height=40)

        ##############################Adding Buttons#########################################

        # Button 1 Student Database
        stuDataImg = Image.open("Images/stddata3.png")
        stuDataImg = stuDataImg.resize((220, 200), Image.ANTIALIAS)
        self.stuDataBtn = ImageTk.PhotoImage(stuDataImg)
        b1 = Button(mainImgLbl, image=self.stuDataBtn, cursor="hand2", command=self.studentDetails)
        b1.place(x=480, y=80, width=220, height=200)
        # Button Label Text
        b1_lbl = Button(mainImgLbl, text="Student Database", command=self.studentDetails, cursor="hand2",
                        font=("time new roman", 14, "bold"), fg="red")
        b1_lbl.place(x=480, y=280, width=220, height=40)

        # Button 2 Face Detector
        faceDetectImg = Image.open("Images/img8.jpg")
        faceDetectImg = faceDetectImg.resize((220, 200), Image.ANTIALIAS)
        self.faceDetectBtn = ImageTk.PhotoImage(faceDetectImg)
        b2 = Button(mainImgLbl, command=self.faceRecog, image=self.faceDetectBtn, cursor="hand2")
        b2.place(x=850, y=80, width=220, height=200)
        # Button Label Text
        b2_lbl = Button(mainImgLbl, command=self.faceRecog, text="Face Detection", cursor="hand2",
                        font=("time new roman", 14, "bold"), fg="red")
        b2_lbl.place(x=850, y=280, width=220, height=40)

        # Button 3 Train Database
        trainDataImg = Image.open("Images/trainData.png")
        trainDataImg = trainDataImg.resize((220, 200), Image.ANTIALIAS)
        self.trainDataBtn = ImageTk.PhotoImage(trainDataImg)
        b3 = Button(mainImgLbl, command=self.trainDataFun, image=self.trainDataBtn, cursor="hand2")
        b3.place(x=1200, y=80, width=220, height=200)
        # Button Label Text
        b3_lbl = Button(mainImgLbl, command=self.trainDataFun, text="Train Database", cursor="hand2",
                        font=("time new roman", 14, "bold"), fg="red")
        b3_lbl.place(x=1200, y=280, width=220, height=40)

        # Button 4 Photos Databse
        photosDataImg = Image.open("Images/photos2.jpg")
        photosDataImg = photosDataImg.resize((220, 200), Image.ANTIALIAS)
        self.photosDataBtn = ImageTk.PhotoImage(photosDataImg)
        b4 = Button(mainImgLbl, command=self.openImages, image=self.photosDataBtn, cursor="hand2")
        b4.place(x=700, y=350, width=220, height=200)
        # Button Label Text
        b4_lbl = Button(mainImgLbl, command=self.openImages, text="Pictures Database", cursor="hand2",
                        font=("time new roman", 14, "bold"), fg="red")
        b4_lbl.place(x=700, y=550, width=220, height=40)

        # Button 5 Exit
        exitImg = Image.open("Images/exit2.png")
        exitImg = exitImg.resize((220, 200), Image.ANTIALIAS)
        self.exitBtn = ImageTk.PhotoImage(exitImg)
        b5 = Button(mainImgLbl, image=self.exitBtn, cursor="hand2", command=root.destroy)
        b5.place(x=1000, y=350, width=220, height=200)
        # Button Label Text
        b5_lbl = Button(mainImgLbl, text="Exit", cursor="hand2", font=("time new roman", 14, "bold"), fg="red",
                        command=root.destroy)
        b5_lbl.place(x=1000, y=550, width=220, height=40)

    ###Function Buttons###
    def studentDetails(self):
        self.newWin = Toplevel(self.root)
        self.Window = student(self.newWin)

    def trainDataFun(self):
        self.newWin = Toplevel(self.root)
        self.Window = trainData(self.newWin)

    def faceRecog(self):
        self.newWin = Toplevel(self.root)
        self.Window = faceRecog(self.newWin)

    ######## Function to Open Images Folder #########

    def openImages(self):
        os.startfile("Samples")


if __name__ == "__main__":
    root = Tk()
    obj = FaceRecog(root)
    root.mainloop()
