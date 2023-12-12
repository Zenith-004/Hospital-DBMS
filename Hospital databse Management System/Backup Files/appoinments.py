from tkinter import *
import mysql.connector as sql
from functools import partial
from PIL import ImageTk,Image
from tkinter import messagebox 
def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

def mysqlpythonapp():
    #mysql python connector
    mycon=sql.connect(host="localhost",user="root",passwd="Shelshar@04", database="project")
    if mycon.is_connected():
        print("Successfully Conected to database")
    else:
        print("Access denied")
    cursor=mycon.cursor()
    st="insert into appointments values('{}','{}','{}','{}','{}')".format(username.get(),name.get(),age.get(),gender.get(),problems.get())
    cursor.execute(st)
    mycon.commit()
    st="select * from appointments"
    cursor.execute(st)
    data=cursor.fetchall()
    for row in data:
        print(row)
    messagebox.showinfo("showinfo", "Appointment Booked")
    tkWindow.destroy
    mycon.close()

#window
tkWindow = Tk()  
tkWindow.geometry('500x350')  
tkWindow.title('Medicare Appointments')
tkWindow.configure(bg='#008080')
#getting screen width and height of display
#width= tkWindow.winfo_screenwidth() 
#height= tkWindow.winfo_screenheight()
#setting tkinter window size
#tkWindow.geometry("%dx%d" % (width, height))

#heading label
headingLabel = Label(tkWindow, text="Book Appointment").place(x=10,y=5)
#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").place(x=10,y=50)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).place(x=80,y=50)  

#name label and text entry box
nameLabel = Label(tkWindow, text="Name").place(x=10,y=100)
name = StringVar()
nameEntry = Entry(tkWindow, textvariable=name).place(x=80,y=100)

#age label and entry box
ageLabel = Label(tkWindow,text="Age").place(x=10,y=150) 
age = StringVar()
addressEntry = Entry(tkWindow, textvariable=age).place(x=80,y=150) 

#gender label and entry box
genderLabel = Label(tkWindow,text="Gender").place(x=10,y=200) 
gender = StringVar()
genderEntry = Entry(tkWindow, textvariable=gender).place(x=80,y=200)

#problems label and entry box
problemsLabel = Label(tkWindow,text="What are your symptoms? Describe the problem:").place(x=10,y=250) 
problems  = StringVar()
problemsEntry = Entry(tkWindow, textvariable=problems ).place(x=300,y=250) 

#book appoinment button
appointmentButton = Button(tkWindow, text="Book Appointment",command=mysqlpythonapp).place(x=10,y=300)

#main loop
tkWindow.mainloop()
