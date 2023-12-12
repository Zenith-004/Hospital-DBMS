from tkinter import *
import mysql.connector as sql
from tkinter import messagebox 

#add record
def packagesinput():
    
    #mysql part
    mycon=sql.connect(host="localhost",user="root",passwd="Shelshar@04", database="project")
    if mycon.is_connected():
        print("Successfully Conected to database")
    else:
        print("Access denied")
    cursor=mycon.cursor()
    st="insert into packages values('{}','{}','{}','{}')".format(username.get(),name.get(),entry.get(),quantity.get())
    cursor.execute(st)
    mycon.commit()
    st="select * from  packages"
    cursor.execute(st)
    data=cursor.fetchall()
    for row in data:
        print(row)
    messagebox.showinfo("showinfo", "Booking Successful")
    tkWindow.destroy()



#window
tkWindow = Tk()  
tkWindow.geometry('500x400')  
tkWindow.title('Medicare Appointments')
tkWindow.configure(bg='#008080')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name:").place(x=10,y=50)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).place(x=80,y=50)  


#name label and text entry box
nameLabel = Label(tkWindow, text="Name:").place(x=10,y=90)
name = StringVar()
nameEntry = Entry(tkWindow, textvariable=name).place(x=80,y=90)

headinglabel=Label(tkWindow, text="Please choose from the menu below:").place(x=10,y=130)
oneLabel = Label(tkWindow, text="1- Oxygen Cylinders, Covid-19 kit, N95 Masks, Steam Inhaler, Sanitizers").place(x=10,y=160)
twoLabel = Label(tkWindow, text="2- Covid-19 kit, N95 Masks, Steam Inhaler").place(x=10,y=190)
threeLabel = Label(tkWindow, text="3- N95 Masks, Sanitizers ").place(x=10,y=220)

#entry label and text entry box
entryLabsel = Label(tkWindow, text="Package number: ").place(x=10,y=270)
entry = StringVar()
entryEntry = Entry(tkWindow, textvariable=entry).place(x=120,y=270)

#quantity label and text entry box
quantityLabsel = Label(tkWindow, text="Quantity: ").place(x=10,y=300)
quantity  = StringVar()
quantityEntry = Entry(tkWindow, textvariable=quantity ).place(x=120,y=300)


#Enter the command 
button_submit=Button(tkWindow,text="Book",command= packagesinput).place(x=200,y=330) 




tkWindow.mainloop()
