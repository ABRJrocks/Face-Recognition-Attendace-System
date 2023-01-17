from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np #for creating grids

class trainData:
    def __init__ (self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        root.state('zoomed')
        #header Image 1
        headerImg = Image.open("Images/frsheader.png")
        headerImg = headerImg.resize((1920,200), Image.ANTIALIAS)
        self.firstImage = ImageTk.PhotoImage(headerImg)
        self.firstlbl = Label(self.root,image=self.firstImage)
        self.firstlbl.pack(fill=BOTH, expand=YES)

        # Main Image
        img = Image.open("Images/bg2.jpg")
        img = img.resize((1920,850), Image.ANTIALIAS)
        self.mainImage = ImageTk.PhotoImage(img)
        mainImgLbl = Label(self.root,image=self.mainImage)
        mainImgLbl.pack(fill=BOTH, expand=YES)

        titleLable = Label(self.root, text="Train Dataset", font=("time new roman", 32,"bold"), fg="red")
        titleLable.place(x = 0, y = 205, width=1920, height=50)

        #Button
        trainBtn = Button(self.root,command=self.trainData, text="Train Data", font = ("time new roman", 18, "bold"), bg="white", fg="Blue", width=16, borderwidth = 0, cursor="hand2")
        trainBtn.place(x = 910, y = 575, width=115, height=50)

############################# applying LBPH Algo ##########################

    def trainData(self):
        dataPath = ("Samples")
        #List Comprehension
        path = [os.path.join(dataPath,file) for file in os.listdir(dataPath)]
        
        facesList = []
        idList = []

        for images in path:
            img = Image.open(images).convert('L')   #Converting to Grayscale Image

            #Using Numpy to create arrays because it gives 88% better performance when creating arrays
            imageNp = np.array(img, np.uint8)
            id = int(os.path.split(images)[1].split('.')[1])
            facesList.append(imageNp)
            idList.append(id)
            cv2.imshow("Training Dataset", imageNp)
            cv2.waitKey(1) == 13
        idList == np.array(idList)

        ######### Training the classifier and Saving trained data in xml file #########

        classifier = cv2.face.LBPHFaceRecognizer_create()
        idList = np.array(idList)
        classifier.train(facesList, idList)

        classifier.write("classifierFile.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Dataset Trained Successfully!")



if __name__=="__main__":
    root=Tk()
    obj=trainData(root)
    root.mainloop()