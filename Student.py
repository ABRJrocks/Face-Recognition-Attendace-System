from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        root.state('zoomed')
        self.imgID = 100
        ########################### Varibales #################################
        self.depVar = StringVar()
        self.courseVar = StringVar()
        self.yearVar = StringVar()
        self.semVar = StringVar()
        self.stdIDVar = StringVar()
        self.nameVar = StringVar()
        self.rollVar = StringVar()
        self.genderVar = StringVar()
        self.emailVar = StringVar()
        self.dobVar = StringVar()
        self.phoneVar = StringVar()
        self.addressVar = StringVar()

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
        titleLable = Label(self.root, text="Student Management System", font=("time new roman", 28, "bold"), fg="red")
        titleLable.place(x=0, y=220, width=1920, height=40)

        # Main Frame
        mainFrame = Frame(mainImgLbl, bd=2)
        mainFrame.place(x=15, y=40, width=1880, height=900)

        # ====================================================================================================================================================#
        # ====================================================================================================================================================#

        # Left Frame
        lFrame = LabelFrame(mainFrame, bd=2, relief=RIDGE, bg="white", text="Student Registration", fg="Blue",
                            font=("time new roman", 18, "bold"))
        lFrame.place(x=40, y=10, width=880, height=800)

        # Adding BG ImagelFImg
        lFImg = Image.open("Images/rgImg3.jpg")
        lFImg = lFImg.resize((880, 150), Image.ANTIALIAS)
        self.imgLeftFrame = ImageTk.PhotoImage(lFImg)
        lFImgLbl = Label(lFrame, image=self.imgLeftFrame)
        lFImgLbl.place(x=0, y=0, width=880, height=150)

        # Curent Course Frame
        courseFrame = LabelFrame(lFrame, bd=2, relief=RIDGE, bg="white", text="Course Information", fg="Blue",
                                 font=("time new roman", 16, "bold"))
        courseFrame.place(x=5, y=160, width=880, height=150)

        # Department
        depLbl = Label(courseFrame, text="Department", font=("time new roman", 16, "bold"), bg="white")
        depLbl.grid(row=0, column=0, padx=5, pady=10)
        depCombo = ttk.Combobox(courseFrame, textvariable=self.depVar, font=("time new roman", 12, "bold"), width=18,
state="readonly")
        depCombo["values"] = ("Select Department", "RSCI", "FRAHS", "RICAS", "RSBM", "Legal Studies",)
        depCombo.current(0)
        depCombo.grid(row=0, column=1, pady=10, sticky=W)
        # Course
        clbl = Label(courseFrame, text="Course", font=("time new roman", 16, "bold"), bg="white")
        clbl.grid(row=0, column=3, padx=10, pady=10)
        cCombo = ttk.Combobox(courseFrame, textvariable=self.courseVar, font=("time new roman", 12, "bold"), width=18,
                              state="readonly")
        cCombo["values"] = ("Select Course", "BSCS", "BSIT", "BA.LLB", "B.Com", "BBA", "BS Maths", "BS Physics")
        cCombo.current(0)
        cCombo.grid(row=0, column=4, pady=10, sticky=W)
        # Year
        ylbl = Label(courseFrame, text="Year", font=("time new roman", 16, "bold"), bg="white")
        ylbl.grid(row=1, column=0, padx=5, pady=10)
        yCombo = ttk.Combobox(courseFrame, textvariable=self.yearVar, font=("time new roman", 12, "bold"), width=18,
                              state="readonly")
        yCombo["values"] = ("Select Year", "2023-2027", "2023-2028")
        yCombo.current(0)
        yCombo.grid(row=1, column=1, pady=10, sticky=W)
        # Semester
        semLbl = Label(courseFrame, text="Semester", font=("time new roman", 16, "bold"), bg="white")
        semLbl.grid(row=1, column=3, padx=5, pady=10)
        semCombo = ttk.Combobox(courseFrame, textvariable=self.semVar, font=("time new roman", 12, "bold"), width=18,
                                state="readonly")
        semCombo["values"] = ("Select Semester", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        semCombo.current(0)
        semCombo.grid(row=1, column=4, pady=10, sticky=W)

        # Student Information Frame
        stuInfoFrame = LabelFrame(lFrame, bd=2, relief=RIDGE, bg="white", text="Student Information", fg="Blue",
                                  font=("time new roman", 16, "bold"))
        stuInfoFrame.place(x=5, y=310, width=880, height=500)

        # Student ID
        stuID = Label(stuInfoFrame, text="Student ID", font=("time new roman", 14, "bold"), bg="white")
        stuID.grid(row=0, column=0, padx=5, pady=10)
        stuEntry = ttk.Entry(stuInfoFrame, textvariable=self.stdIDVar, width=20, font=("time new roman", 14))
        stuEntry.grid(row=0, column=1, pady=10, sticky=W)
        # Student Name
        stuName = Label(stuInfoFrame, text="Name", font=("time new roman", 14, "bold"), bg="white")
        stuName.grid(row=0, column=2, padx=5, pady=10)
        stuNameEntry = ttk.Entry(stuInfoFrame, textvariable=self.nameVar, width=20, font=("time new roman", 14))
        stuNameEntry.grid(row=0, column=3, pady=10, sticky=W)
        # Student Gender
        gender = Label(stuInfoFrame, text="Gender", font=("time new roman", 14, "bold"), bg="white")
        gender.grid(row=1, column=0, padx=5, pady=10)
        genderCombo = ttk.Combobox(stuInfoFrame, textvariable=self.genderVar, font=("time new roman", 12, "bold"),
                                   width=18, state="readonly")
        genderCombo["values"] = ("Select Gender", "Male", "Female", "Other")
        genderCombo.current(0)
        genderCombo.grid(row=1, column=1, pady=10, sticky=W)
        # Student Roll No.
        rollNo = Label(stuInfoFrame, text="Roll No.", font=("time new roman", 14, "bold"), bg="white")
        rollNo.grid(row=1, column=2, padx=5, pady=10)
        rollEntry = ttk.Entry(stuInfoFrame, textvariable=self.rollVar, width=20, font=("time new roman", 14))
        rollEntry.grid(row=1, column=3, pady=10, sticky=W)
        # Email
        email = Label(stuInfoFrame, text="Email", font=("time new roman", 14, "bold"), bg="white")
        email.grid(row=2, column=0, padx=5, pady=10)
        emailEntry = ttk.Entry(stuInfoFrame, textvariable=self.emailVar, width=20, font=("time new roman", 14))
        emailEntry.grid(row=2, column=1, pady=10, sticky=W)
        # Phone No.
        pNo = Label(stuInfoFrame, text="Phone No.", font=("time new roman", 14, "bold"), bg="white")
        pNo.grid(row=2, column=2, padx=5, pady=10)
        pNoEntry = ttk.Entry(stuInfoFrame, textvariable=self.phoneVar, width=20, font=("time new roman", 14))
        pNoEntry.grid(row=2, column=3, pady=10, sticky=W)
        # Address
        address = Label(stuInfoFrame, text="Address", font=("time new roman", 14, "bold"), bg="white")
        address.grid(row=3, column=0, padx=5, pady=10)
        addressEntry = ttk.Entry(stuInfoFrame, textvariable=self.addressVar, width=20, font=("time new roman", 14))
        addressEntry.grid(row=3, column=1, pady=10, sticky=W)
        # DOB
        dob = Label(stuInfoFrame, text="DOB", font=("time new roman", 14, "bold"), bg="white")
        dob.grid(row=3, column=2, padx=5, pady=10)
        dobEntry = ttk.Entry(stuInfoFrame, textvariable=self.dobVar, width=20, font=("time new roman", 14))
        dobEntry.grid(row=3, column=3, pady=10, sticky=W)

        # Radio Buttons for Snaps
        self.radio1Var = StringVar()
        rdBtn1 = ttk.Radiobutton(stuInfoFrame, variable=self.radio1Var, text="Take Photo Sample", value="Yes")
        rdBtn1.grid(row=4, column=1, padx=5, pady=10)

        rdBtn2 = ttk.Radiobutton(stuInfoFrame, variable=self.radio1Var, text="No Photo Sample", value="No")
        rdBtn2.grid(row=4, column=2, padx=5, pady=10)

        # Buttons Frame
        btnFrame = Frame(stuInfoFrame, bd=2, relief=RIDGE, bg="white")
        btnFrame.place(x=0, y=250, width=880, height=100)

        # Save Button
        saveBtn = Button(btnFrame, command=self.addData, text="Save", font=("time new roman", 16, "bold"), bg="Blue",
                         fg="White", width=16)
        saveBtn.grid(row=0, column=0)
        # Update Button
        updateBtn = Button(btnFrame, command=self.updateData, text="Update", font=("time new roman", 16, "bold"),
                           bg="Blue", fg="White", width=16)
        updateBtn.grid(row=0, column=2, )
        # Delete Button
        delBtn = Button(btnFrame, command=self.deleteData, text="Delete", font=("time new roman", 16, "bold"),
                        bg="Blue", fg="White", width=16)
        delBtn.grid(row=0, column=3, )
        # Rest Button
        resetBtn = Button(btnFrame, command=self.resetData, text="Reset", font=("time new roman", 16, "bold"),
                          bg="Blue", fg="White", width=16)
        resetBtn.grid(row=0, column=4)

        # New Frame for 2 Buttons
        btnFrame2 = Frame(stuInfoFrame, bd=2, relief=RIDGE, bg="white")
        btnFrame2.place(x=0, y=300, width=880, height=50)

        # Add Photo Sample Button
        addPhotoBtn = Button(btnFrame2, command=self.generateDataset, text="Add Photo Sample",
                             font=("time new roman", 16, "bold"), bg="Blue", fg="White", width=33)
        addPhotoBtn.grid(row=0, column=0)

        # Update Photo Sample Button
        upPhotoBtn = Button(btnFrame2, command=self.update_snapshot, text="Update Photo Sample",
                            font=("time new roman", 16, "bold"), bg="Blue", fg="White", width=33)
        upPhotoBtn.grid(row=0, column=1)

        # ====================================================================================================================================================#
        # ====================================================================================================================================================#

        # Right Frame
        rFrame = LabelFrame(mainFrame, bd=2, relief=RIDGE, bg="white", text="Student Details", fg="Blue",
                            font=("time new roman", 18, "bold"))
        rFrame.place(x=960, y=10, width=880, height=800)

        # BG Image
        rFIMG = Image.open("Images/search.jpg")
        rFIMG = rFIMG.resize((880, 300), Image.ANTIALIAS)
        self.imgRightFrame = ImageTk.PhotoImage(rFIMG)

        rFImgLbl = Label(rFrame, image=self.imgRightFrame)
        rFImgLbl.place(x=0, y=0, width=880, height=300)

        # Stundent Search Frame
        stuDetFrame = LabelFrame(rFrame, bd=2, relief=RIDGE, bg="white", text="Search and View Student Details",
                                 fg="Blue", font=("time new roman", 16, "bold"))
        stuDetFrame.place(x=0, y=220, width=880, height=100)

        # Search
        searchLbl = Label(stuDetFrame, text="Search By", font=("time new roman", 18, "bold"), bg="Blue", fg="white")
        searchLbl.grid(row=0, column=0, padx=5, pady=10)

        self.searchComboSelect = StringVar()
        searchCombo = ttk.Combobox(stuDetFrame, textvariable=self.searchComboSelect,
                                   font=("time new roman", 12, "bold"), width=18, state="readonly")
        searchCombo["values"] = ("Select Option", "roll", "phone")
        searchCombo.current(0)
        searchCombo.grid(row=0, column=1, padx=5, pady=10)

        self.searchEntry = StringVar()

        # searchFieldLbl = Label(stuDetFrame,  font = ("time new roman", 14, "bold"), bg="white")
        # searchFieldLbl.grid(row = 0, column=2, padx=5, pady=10) 
        searchEntry = ttk.Entry(stuDetFrame, textvariable=self.searchEntry, width=18, font=("time new roman", 14))
        searchEntry.grid(row=0, column=2, padx=5, sticky=W, pady=10)

        # Search Button
        searchBtn = Button(stuDetFrame, command=self.searchData, text="Search", font=("time new roman", 16, "bold"),
                           bg="Blue", fg="White", width=10)
        searchBtn.grid(row=0, column=3, padx=5, pady=10)
        # Show All Button
        showAllBtn = Button(stuDetFrame, command=self.fetchData, text="Show All", font=("time new roman", 16, "bold"),
                            bg="Blue", fg="White", width=10)
        showAllBtn.grid(row=0, column=4, padx=5, pady=10)

        ###Table Frame###
        tableFrame = LabelFrame(rFrame, bd=2, relief=RIDGE, bg="white")
        tableFrame.place(x=0, y=330, width=880, height=400)

        # Scroll Bars
        scrollX = ttk.Scrollbar(tableFrame, orient=HORIZONTAL)
        scrollY = ttk.Scrollbar(tableFrame, orient=VERTICAL)

        self.detailsTable = ttk.Treeview(tableFrame, columns=(
        "dep", "crs", "Year", "sem", "ID", "Name", "Gender", "Roll", "Email", "Phone", "Address", "DOB", "PS"),
                                         xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)
        # Table
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)
        scrollX.config(command=self.detailsTable.xview)
        scrollY.config(command=self.detailsTable.yview)

        self.detailsTable.heading("dep", text="Department")
        self.detailsTable.heading("crs", text="Course")
        self.detailsTable.heading("Year", text="Year")
        self.detailsTable.heading("sem", text="Semester")
        self.detailsTable.heading("ID", text="Student ID")
        self.detailsTable.heading("Name", text="Name")
        self.detailsTable.heading("Gender", text="Gender")
        self.detailsTable.heading("Roll", text="Roll No")
        self.detailsTable.heading("Email", text="Email")
        self.detailsTable.heading("Phone", text="Phone No")
        self.detailsTable.heading("Address", text="Address")
        self.detailsTable.heading("DOB", text="DOB")
        self.detailsTable.heading("PS", text="Photo Status")
        self.detailsTable["show"] = "headings"

        # Setting Width
        self.detailsTable.column("dep", width=100)
        self.detailsTable.column("crs", width=100)
        self.detailsTable.column("Year", width=100)
        self.detailsTable.column("sem", width=100)
        self.detailsTable.column("ID", width=100)
        self.detailsTable.column("Name", width=100)
        self.detailsTable.column("Gender", width=100)
        self.detailsTable.column("Roll", width=100)
        self.detailsTable.column("Email", width=150)
        self.detailsTable.column("Phone", width=150)
        self.detailsTable.column("Address", width=200)
        self.detailsTable.column("DOB", width=100)
        self.detailsTable.column("PS", width=150)

        self.detailsTable.pack(fill=BOTH, expand=1)
        self.detailsTable.bind("<ButtonRelease>", self.getCursor)
        self.fetchData()

    # ====================================================================================================================================================#
    # ====================================================================================================================================================#

    #############Funtions################

    ####Sending Data To Database
    def addData(self):
        if self.depVar.get() == "Select Department" or self.addressVar.get() == "" or self.courseVar.get() == "Select Course" or self.yearVar.get() == "Select Year" or self.semVar.get() == "Select Semester" or self.stdIDVar.get() == "" or self.nameVar.get() == "" or self.genderVar.get() == "Select Gender" or self.rollVar.get() == "" or self.emailVar.get() == "" or self.phoneVar.get() == "" or self.dobVar.get() == "" or self.radio1Var.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="",
                                               database="face_recognition_system")
                conCursor = conn.cursor()
                conCursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.depVar.get(), self.courseVar.get(), self.yearVar.get(), self.semVar.get(),
                    self.stdIDVar.get(), self.nameVar.get(), self.genderVar.get(), self.rollVar.get(),
                    self.emailVar.get(), self.phoneVar.get(), self.addressVar.get(),
                    self.dobVar.get(), self.radio1Var.get()
                ))

                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo("Success", "Student Details are Added!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    ########Fetching Data from Database#########
    def fetchData(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="",
                                       database="face_recognition_system")
        conCursor = conn.cursor()
        conCursor.execute("select * from student")
        data = conCursor.fetchall()
        if len(data) != 0:
            self.detailsTable.delete(*self.detailsTable.get_children())
            for i in data:
                self.detailsTable.insert("", END, values=i)
        conn.close()

    ########### Get Cursor Funtion ##################
    def getCursor(self, event=""):
        cursorFocus = self.detailsTable.focus()
        content = self.detailsTable.item(cursorFocus)
        data = content["values"]
        self.depVar.set(data[0]),
        self.courseVar.set(data[1]),
        self.yearVar.set(data[2]),
        self.semVar.set(data[3]),
        self.stdIDVar.set(data[4]),
        self.nameVar.set(data[5]),
        self.genderVar.set(data[6]),
        self.rollVar.set(data[7]),
        self.emailVar.set(data[8]),
        self.phoneVar.set(data[9]),
        self.addressVar.set(data[10]),
        self.dobVar.set(data[11]),
        self.radio1Var.set(data[12])

    ######### Update Function ############

    def updateData(self):
        if self.depVar.get() == "Select Department" or self.addressVar.get() == "" or self.courseVar.get() == "Select Course" or self.yearVar.get() == "Select Year" or self.semVar.get() == "Select Semester" or self.stdIDVar.get() == "" or self.nameVar.get() == "" or self.genderVar.get() == "Select Gender" or self.rollVar.get() == "" or self.emailVar.get() == "" or self.phoneVar.get() == "" or self.dobVar.get() == "" or self.radio1Var.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to Update the Records?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="",
                                                   database="face_recognition_system")
                    conCursor = conn.cursor()
                    conCursor.execute(
                        "update student set dep=%s, course=%s, year=%s, sem=%s, name=%s, gender=%s, roll=%s, email=%s, phone=%s, address=%s, dob=%s, photo_sample=%s where Student_ID = %s",
                        (
                            self.depVar.get(), self.courseVar.get(), self.yearVar.get(), self.semVar.get(),
                            self.nameVar.get(), self.genderVar.get(), self.rollVar.get(),
                            self.emailVar.get(), self.phoneVar.get(), self.addressVar.get(),
                            self.dobVar.get(), self.radio1Var.get(), self.stdIDVar.get()
                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Data Successfully Updated!", parent=self.root)
                conn.commit()
                self.fetchData()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    ######### Delete Function ############
    def deleteData(self):
        if self.stdIDVar.get() == "":
            messagebox.showerror("Error", "Student ID is Requred", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Confirmation", "Do you want to delete this record?")
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="",
                                                   database="face_recognition_system")
                    conCursor = conn.cursor()
                    sql = "delete from student where Student_ID=%s"
                    val = (self.stdIDVar.get(),)
                    conCursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo("Success", "Successfully Deleted Record!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    ######### Reset Function ############
    def resetData(self):
        self.depVar.set("Select Department")
        self.courseVar.set("Select Course")
        self.yearVar.set("Select Year")
        self.semVar.set("Select Semester")
        self.genderVar.set("Selec   t Gender")
        self.stdIDVar.set("")
        self.nameVar.set("")
        self.rollVar.set("")
        self.emailVar.set("")
        self.phoneVar.set("")
        self.addressVar.set("")
        self.dobVar.set("")
        self.radio1Var.set("")

    ######### Search Data ##############

    def searchData(self):
        if self.searchComboSelect.get() == "Select Option" or self.searchEntry.get() == "":
            messagebox.showerror("Error", "Please Select Option and Enter Data")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="",
                                               database="face_recognition_system")
                conCursor = conn.cursor()
                conCursor.execute("select * from student where " + str(self.searchComboSelect.get()) + " LIKE '%" + str(self.searchEntry.get()) + "%'")
                data = conCursor.fetchall()
                if len(data) != 0:
                    self.detailsTable.delete(*self.detailsTable.get_children())
                    for i in data:
                        self.detailsTable.insert("", END, values=i)
                else:
                    messagebox.showinfo("Info", "No Student Found!", parent=self.root)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    ################# Snap Shots ###############

    def generateDataset(self):
        if self.depVar.get() == "Select Department" or self.addressVar.get() == "" or self.courseVar.get() == "Select Course" or self.yearVar.get() == "Select Year" or self.semVar.get() == "Select Semester" or self.stdIDVar.get() == "" or self.nameVar.get() == "" or self.genderVar.get() == "Select Gender" or self.rollVar.get() == "" or self.emailVar.get() == "" or self.phoneVar.get() == "" or self.dobVar.get() == "" or self.radio1Var.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="",
                                               database="face_recognition_system")
                conCursor = conn.cursor()
                conCursor.execute("select * from student")
                result = conCursor.fetchall()
                id = 0
                for x in result:
                    id += 1
                conCursor.execute(
                    "update student set dep=%s, course=%s, year=%s, sem=%s, name=%s, gender=%s, roll=%s, email=%s, phone=%s, address=%s, dob=%s, photo_sample=%s where Student_ID = %s",
                    (
                        self.depVar.get(), self.courseVar.get(), self.yearVar.get(), self.semVar.get(),
                        self.nameVar.get(), self.genderVar.get(), self.rollVar.get(),
                        self.emailVar.get(), self.phoneVar.get(), self.addressVar.get(),
                        self.dobVar.get(), self.radio1Var.get(), self.stdIDVar.get() == id + 1
                    ))
                conn.commit()
                self.fetchData()
                self.resetData()
                conn.close()
                ######### loading predefined data on face: frontal face file (opencv)#########
                faceClassifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def faceCapture(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = faceClassifier.detectMultiScale(gray, 1.3, 5)
                    # scaling Factor = 1.3
                    # Minimum Neighbor = 5
                    for (x, y, w, h) in faces:
                        faceCroped = img[y:y + h, x:x + w]
                        return faceCroped

                capture = cv2.VideoCapture(0)
                imgID = 0
                while TRUE:
                    ret, myFrame = capture.read()
                    if faceCapture(myFrame) is not None:
                        imgID += 1
                        face = cv2.resize(faceCapture(myFrame), (600, 600))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        fileName = "samples/user." + str(id) + "." + str(imgID) + ".jpg"
                        cv2.imwrite(fileName, face)
                        cv2.putText(face, str(imgID), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(imgID) == 100:
                        break
                capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating Datasets Completed Successfully!")

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

###################### UPDATE SNAP SHOTS ######################################

    def update_snapshot(self):
        if self.stdIDVar.get() == "":
            messagebox.showerror("Error", "Please enter Student ID first", parent=self.root)
        else:
            faceClassifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def faceCapture(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = faceClassifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    faceCroped = img[y:y + h, x:x + w]
                    return faceCroped

            capture = cv2.VideoCapture(0)
            while True:
                ret, myFrame = capture.read()
                if faceCapture(myFrame) is not None:
                    self.imgID += 1
                    face = cv2.resize(faceCapture(myFrame), (600, 600))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    fileName = "samples/user." + str(self.stdIDVar.get()) + "." + str(self.imgID) + ".jpg"
                    cv2.imwrite(fileName, face)
                    cv2.putText(face, str(self.imgID), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)
                if cv2.waitKey(1) == 13:
                    break
            capture.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Image captured and added successfully")


############### MAIN ################


if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()


#