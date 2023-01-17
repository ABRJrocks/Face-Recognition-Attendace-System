from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np #for creating grids

class faceRecog:
    def __init__ (self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face RecognitionSystem")
        root.state('zoomed')

        #Left Image
        leftImage = Image.open("Images/bg3.jpg")
        leftImage = leftImage.resize((1100,1050), Image.ANTIALIAS)
        self.firstImage = ImageTk.PhotoImage(leftImage)
        self.firstlbl = Label(self.root,image=self.firstImage)
        self.firstlbl.place(x=0, y=0)
        
        #Right Image
        rightImg = Image.open("Images/faceRecog.png")
        rightImg = rightImg.resize((950,1050), Image.ANTIALIAS)
        self.secondImage = ImageTk.PhotoImage(rightImg)
        self.secondLbl = Label(self.root,image=self.secondImage)
        self.secondLbl.place(x=1050, y=0)


        # #Title Label
        # titleLable = Label(self.root, text="Face Recognition", font=("time new roman", 28,"bold"), fg="red")
        # titleLable.place(x = 0, y = 0, width=1920, height=40)

        #Button
        trainBtn = Button(self.secondLbl,command=self.faceRecogFun, text="Recognize Face", font = ("time new roman", 18, "bold"), bg="white", fg="Red", width=16, cursor="hand2")
        trainBtn.place(x = 320, y = 930, width=300, height=70)


 ##################### Attendace ########################


    def markAttendace(self,stdID,name,dep):
        with open("attendance.CSV", "r+", newline="\n") as f:
            fileDataList = f.readlines()
            nameList = []
            for line in fileDataList:
                entry = line.split((","))
                nameList.append(entry[0])
            if ((stdID not in nameList) and (name not in nameList) and (dep not in nameList)):
                now = datetime.now()
                d1 = now.strftime("%Y-%m-%d")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{stdID},{name},{dep},{dtString},{d1},Present")






    ################# Face Recognition ###################

    def faceRecogFun(self):
        def createBoundry(img, classifier, scaleFactor, minNeighbors, color, text, trainedClf):
            facegrayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(facegrayImg, scaleFactor,minNeighbors)
            cordinates = []
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id, predict = trainedClf.predict(facegrayImg[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                #Fetching Data from Database
                conn = mysql.connector.connect(host="localhost", username = "root", password = "", database = "face_recognition_system")
                conCursor = conn.cursor() 

                conCursor.execute("select Student_ID from student where Student_ID=" + str(id))
                stdID = conCursor.fetchone()
                stdID = "+".join(stdID)

                conCursor.execute("select name from student where Student_ID=" + str(id))
                name = conCursor.fetchone()
                name = "+".join(name)
                
                conCursor.execute("select roll from student where Student_ID=" + str(id))
                roll = conCursor.fetchone()
                roll = "+".join(roll)
                
                conCursor.execute("select dep from student where Student_ID=" + str(id))
                dep = conCursor.fetchone()
                dep = "+".join(dep)



                if confidence > 75:
                    cv2.putText(img, f"Name: {name}", (x,y-70), cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Roll No: {roll}", (x,y-40), cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Department: {dep}", (x,y-20), cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.markAttendace(stdID,name,dep)

                else:
                      cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                      cv2.putText(img, "Unknown Face!", (x,y-15), cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                cordinates = [x,y,w,h]
            return cordinates

        def recognition(img, trainedClf,faceCascade):
                cordinates = createBoundry(img, faceCascade, 1.1,10,(255,255,255),"Face",trainedClf)
                return img
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        trainedClf = cv2.face.LBPHFaceRecognizer_create()
        trainedClf.read("classifierFile.xml")


        videoCap = cv2.VideoCapture(0)

        while True:
            ret, img = videoCap.read()
            img = recognition(img, trainedClf, faceCascade)
            cv2.imshow("Recognizing Face", img)
            
            if cv2.waitKey(1) == 13:
                break

        videoCap.release()
        cv2.destroyAllWindows()



if __name__=="__main__":
    root=Tk()
    obj=faceRecog(root)
    root.mainloop()