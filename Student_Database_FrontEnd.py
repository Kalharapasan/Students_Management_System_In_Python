import sqlite3
from tkinter import *
import tkinter.messagebox
import stdStudent_BackEnd  # Ensure this backend exists and is correct

class Student:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Management Systems")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")

        # ===================================================== Variables ====================================================
        self.StdId = StringVar()
        self.Firstname = StringVar()
        self.Surname = StringVar()
        self.DoB = StringVar()
        self.Age = StringVar()
        self.Gender = StringVar()
        self.Address = StringVar()
        self.Mobile = StringVar()

        # =================================================== Functions =========================================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.textStdID.delete(0, END)
            self.textFirstname.delete(0, END)
            self.textSurname.delete(0, END)
            self.textDoB.delete(0, END)
            self.textAge.delete(0, END)
            self.textGender.delete(0, END)
            self.textAddress.delete(0, END)
            self.textMobile.delete(0, END)

        def addData():
            if len(self.StdId.get()) != 0:
                stdStudent_BackEnd.addStdRec(
                    self.StdId.get(),
                    self.Firstname.get(),
                    self.Surname.get(),
                    self.DoB.get(),
                    self.Age.get(),
                    self.Gender.get(),
                    self.Address.get(),
                    self.Mobile.get()
                )
                studentlist.delete(0, END)
                studentlist.insert(END, (self.StdId.get(), self.Firstname.get(), self.Surname.get(), self.DoB.get(), self.Age.get(), self.Gender.get(), self.Address.get(), self.Mobile.get()))

        def displayData():
            studentlist.delete(0, END)
            for row in stdStudent_BackEnd.viewData():
                studentlist.insert(END, row, str(""))

        def deleteData():
            if len(self.StdId.get()) != 0:
                stdStudent_BackEnd.deleteRec(sd[0])
                displayData()

        def searchDatabase():
            studentlist.delete(0, END)
            for row in stdStudent_BackEnd.searchData(
                self.StdId.get(),
                self.Firstname.get(),
                self.Surname.get(),
                self.DoB.get(),
                self.Age.get(),
                self.Gender.get(),
                self.Address.get(),
                self.Mobile.get()
            ):
                studentlist.insert(END, row, str(""))

        def update():
            if len(self.StdId.get()) != 0:
                stdStudent_BackEnd.dataUpdate(
                    sd[0],
                    self.StdId.get(),
                    self.Firstname.get(),
                    self.Surname.get(),
                    self.DoB.get(),
                    self.Age.get(),
                    self.Gender.get(),
                    self.Address.get(),
                    self.Mobile.get()
                )
                displayData()

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.textStdID.delete(0, END)
            self.textStdID.insert(END, sd[1])
            self.textFirstname.delete(0, END)
            self.textFirstname.insert(END, sd[2])
            self.textSurname.delete(0, END)
            self.textSurname.insert(END, sd[3])
            self.textDoB.delete(0, END)
            self.textDoB.insert(END, sd[4])
            self.textAge.delete(0, END)
            self.textAge.insert(END, sd[5])
            self.textGender.delete(0, END)
            self.textGender.insert(END, sd[6])
            self.textAddress.delete(0, END)
            self.textAddress.insert(END, sd[7])
            self.textMobile.delete(0, END)
            self.textMobile.insert(END, sd[8])

        # ================================================== Frames =========================================================
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Student Database Management Systems", bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, bg="cadet blue")
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, bg="Ghost White", relief=RIDGE,
                                   font=('arial', 20, 'bold'), text="Student Info\n")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, bg="Ghost White", relief=RIDGE,
                                    font=('arial', 20, 'bold'), text="Student Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

        # =========================================== Labels and Entry Widgets ===============================================
        self.lblStdID = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Student ID:", padx=2, pady=2, bg="Ghost White")
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.textStdID = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=self.StdId, width=39)
        self.textStdID.grid(row=0, column=1)

        self.lblFirstname = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Firstname:", padx=2, pady=2, bg="Ghost White")
        self.lblFirstname.grid(row=1, column=0, sticky=W)
        self.textFirstname = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=self.Firstname, width=39)
        self.textFirstname.grid(row=1, column=1)

        self.lblSurname = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Surname:", padx=2, pady=2, bg="Ghost White")
        self.lblSurname.grid(row=2, column=0, sticky=W)
        self.textSurname = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=self.Surname, width=39)
        self.textSurname.grid(row=2, column=1)

        self.lblDoB = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Date of Birth:", padx=2, pady=2, bg="Ghost White")
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.textDoB = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=self.DoB, width=39)
        self.textDoB.grid(row=3, column=1)

        self.lblAge = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Age:", padx=2, pady=2, bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.textAge = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=self.Age, width=39)
        self.textAge.grid(row=4, column=1)

        self.lblGender = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Gender:", padx=2, pady=2, bg="Ghost White")
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.textGender = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=self.Gender, width=39)
        self.textGender.grid(row=5, column=1)

        self.lblAddress = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Address:", padx=2, pady=2, bg="Ghost White")
        self.lblAddress.grid(row=6, column=0, sticky=W)
        self.textAddress = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=self.Address, width=39)
        self.textAddress.grid(row=6, column=1)

        self.lblMobile = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Mobile:", padx=2, pady=2, bg="Ghost White")
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.textMobile = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=self.Mobile, width=39)
        self.textMobile.grid(row=7, column=1)

        # =========================================== Listbox and Scrollbar Widget ===========================================
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = Listbox(DataFrameRIGHT, width=41, height=16, font=('arial', 12, 'bold'),
                              yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=studentlist.yview)

        # =========================================== Buttons ===========================================
        self.btnAddData = Button(ButtonFrame, text="Add New", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                 command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                     command=displayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                   command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                    command=deleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                    command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                    command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                              command=iExit)
        self.btnExit.grid(row=0, column=6)

        displayData()


if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
