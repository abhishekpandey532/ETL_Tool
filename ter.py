import Tkinter as tk
import os
import tkMessageBox

'''class Tuts:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        #tkMessageBox.showinfo("Window Title", 'Some Info')
        answer = tkMessageBox.askquestion('Question 1','Say')

        if answer == 'yes':
            print 'Cool'
        else:
            print "Not Cool"

        self.printButton = Button(frame, text="Print", command=self.printMessage, bg="red", bd=20)
        self.printButton.pack(side=LEFT)

        self.quitButton=Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

        #Toolbar

        insertButt = Button(frame, text="Insert Image")
        insertButt.pack(side=BOTTOM, padx=2, pady=2)
        printButt = Button(frame, text="Insert Image")
        printButt.pack(side=BOTTOM, padx=2, pady=2)

    def printMessage(self):
        os.system('metl')
        print "Woooow!!!!"

root = Tk()
b = Tuts(root)


root.mainloop()


'''



class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 1")
       label.pack(side="top", fill="both", expand=True)
       #5 transformation to be shown

       #bt = tk.Button(self,text="Run", command=self.Run)
       #bt.place(x=10,y=10)

       bt1 = tk.Button(self, text="CSV to XLS", command=self.CSV_to_XLS)
       bt1.place(x=200, y=80)

       bt1 = tk.Button(self, text="JSON to MySQL Database", command=self.JSON_to_MySql)
       bt1.place(x=400, y=80)

       bt1 = tk.Button(self, text="CSV to MySQL Database", command=self.CSV_to_MySql)
       bt1.place(x=200, y=130)

       bt1 = tk.Button(self, text="JSON to Text", command=self.JSON_to_Text)
       bt1.place(x=400, y=130)

       #bt1 = tk.Button(self, text="JSON to MySQL Database", command=self.Run)
       #bt1.place(x=50, y=10)



   def Run(self):
       print "Hello"
       os.system('metl exec.yml')
       tkMessageBox.showinfo("Language Changed")

   def CSV_to_XLS(self):
       print "Hello"
       os.system('metl CSV_to_XLS.yml')
       tkMessageBox.showinfo("File Made")

   def JSON_to_MySql(self):
       print "Hello"
       os.system('metl JSON_to_MySql.yml')
       tkMessageBox.showinfo("File Made")

   def CSV_to_MySql(self):
       print "Hello"
       os.system('metl CSV_to_MySql.yml')
       tkMessageBox.showinfo("File Made")

   def JSON_to_Text(self):
       print "Hello"
       os.system('metl JSON_to_Text.yml')
       tkMessageBox.showinfo("File Made")


class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")

       #country_code changes to country name ----- Yet to be done
       tbt1= tk.Button(self,text="Test_Test")
       tbt1.place(x=40, y=50)

       #We add 100 seats to each of our theatres
       #Search "Add" in the github tutorial
       tbt2 = tk.Button(self,text="Add 100 seats to theatre", command=self.add100seats)
       tbt2.place(x=240, y=50)
       # Concatenate a word to a value in the db--> Append SV,MV,LV:Large Value to the theatre name
       #Search "Set" in the github bfauldi
       tbt3 = tk.Button(self, text="Append First and Last Name", command=self.Append_Full_Name)
       tbt3.place(x=440, y=50)

       # We change M->Male and F->Female
       # tbt5 = N1_Source_Target_09_title_transform
       tbt4 = tk.Button(self, text="M-> Male , F->Female", command=self.M_Male)
       tbt4.place(x=40, y=80)

       #Convert the name to Title case i.e First character
       # tbt6=N1_Source_Target_09_title_transform
       tbt5 = tk.Button(self, text="Convert Name to Title Case", command=self.Title_Case)
       tbt5.place(x=240, y=80)
       #Drop by condition that if movie language is match by some random regex language
       # tbt7=See dropbycondition on github bfauldi
       tbt6 = tk.Button(self, text="Movie language change from Chinese to Korean", command=self.Change_Language)
       tbt6.place(x=440, y=80)

       # Drop by condition that if gender is NULL then remove it
       # tbt8= 04_filter_drop_by_condition
       tbt7 = tk.Button(self, text="Drop if gender is NULL", command=self.empty_gender)
       tbt7.place(x=40, y=110)

        #Change Full name to Title Case
       #tbt8 = tk.Button(self, text="Change Name to Title Case", command=self.ccodetoname)
       #tbt8.place(x=240, y=110)


       label.pack(side="top", fill="both", expand=True)

   def ccodetoname(self):
       print "Hello"
       os.system('metl exec.yml')

   def Change_Language(self):
       print "Hello"
       os.system('metl Change_Language.yml')
       tkMessageBox.showinfo("Language Changed")

   def Append_Full_Name(self):
       print "Hello_2"
       os.system('metl Append_Full_Name.yml')
       tkMessageBox.showinfo("Appended")

   def add100seats(self):
       print "Hello_1"
       os.system('metl Add_100_seats.yml')
       tkMessageBox.showinfo("Seats Added")

   def M_Male(self):
       print "Hello_1"
       os.system('metl M_Male.yml')
       tkMessageBox.showinfo("Done Sir/Ma'am")


   def Title_Case(self):
       print "Hello_1"
       os.system('metl Title_Case.yml')
       tkMessageBox.showinfo("Changed to Title_Case")


   def empty_gender(self):
       print "Hello_1"
       os.system('metl empty_gender.yml')
       tkMessageBox.showinfo("Rows Deleted")



class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")

       label.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=10, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        #b1 = tk.Button(buttonframe, text="Extract", command=p1.lift)
        #b2 = tk.Button(buttonframe, text="Transform", command=p2.lift)
        #b3 = tk.Button(buttonframe, text="Load", command=p3.lift)
        # b1 = tk.Button(buttonframe, text="Extract", command=p1.lift)

        b1 = tk.Button( text="Extract", command=p1.lift)
        b1.place(in_=buttonframe, x=250, y=2)

        b2 = tk.Button( text="Transform", command=p2.lift)
        b2.place(in_=buttonframe, x=320, y=2)

        b3 = tk.Button( text="Load", command=p3.lift)
        b3.place(in_=buttonframe, x=410, y=2)

        #b1.pack(side="left")
        #b2.pack(side="left")
        #b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()