from HomePage import*
import mysql.connector as sql
from tkinter.ttk import Button
from tkinter import *
from tkinter import messagebox 
from functools import partial
from PIL import ImageTk,Image


def homepage():
    global window
    window=Tk()
    #window
    window.title('Medicare')
    #getting screen width and height of display
    width= window.winfo_screenwidth() 
    height= window.winfo_screenheight()
    #setting tkinter window size
    window.geometry("%dx%d" % (width, height))
    window.configure(bg='#008080')

    #logo
    global img1
    img1= ImageTk.PhotoImage(Image.open('logo1.png'))
    panel = Label(window, image = img1)
    panel.place(x=5, y=5)

    #number
    img3= ImageTk.PhotoImage(Image.open('num1.png'))
    panel = Label(window, image = img3)
    panel.place(x=1000, y=5)

    #background picture
    img2 = ImageTk.PhotoImage(Image.open('backgroundpic1.png'))
    panel = Label(window, image = img2)
    panel.place(x=0, y=150)

    #buttons
    btn1=Button(window, text="HOME", fg='white', bg='#3A3B3C', height='2')
    btn1.place(x=95, y=100)

    btn2=Button(window, text="AVAILABILITY", fg='white', bg='#3A3B3C',height='2')
    btn2.place(x=145, y=100)

    btn3=Button(window, text="PACKAGES", fg='white', bg='#3A3B3C',height='2')
    btn3.place(x=233, y=100)

    btn4=Button(window, text="APPOINMENTS", fg='white', bg='#3A3B3C',height='2')
    btn4.place(x=307, y=100)

    btn5=Button(window, text="DONATIONS",command= donations,fg='white', bg='#3A3B3C',height='2')
    btn5.place(x=405, y=100)


    window.mainloop()

def donations():
    
    window.destroy()
    donationcode()




def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

def donationcode():

        def mysqlpythondon():
            #mysql python connector
            mycon=sql.connect(host="localhost",user="root",passwd="Shelshar@04", database="project")
            if mycon.is_connected():
                print("Successfully Conected to database")
            else:
                print("Access denied")
            cursor=mycon.cursor()
            st="insert into donations values('{}','{}','{}','{}')".format(name.get(),address.get(),accountno.get(),amount.get())
            cursor.execute(st)
            mycon.commit()
            st="select * from donations"
            cursor.execute(st)
            data=cursor.fetchall()
            for row in data:
                print(row)
            messagebox.showinfo("showinfo", "Donation Successful")
            tkWindow.destroy()

            mycon.close()

            homepage()

        #window
        tkWindow = Tk()  
        tkWindow.geometry('500x350')  
        tkWindow.title('Medicare')
        tkWindow.configure(bg='#008080')
        #getting screen width and height of display
        #width= tkWindow.winfo_screenwidth() 
        #height= tkWindow.winfo_screenheight()
        #setting tkinter window size
        #tkWindow.geometry("%dx%d" % (width, height))

        # heading label
        nameLabel = Label(tkWindow, text=" Make Donation").place(x=10,y=10)
        #name label and entry box
        nameLabel = Label(tkWindow, text="Name").place(x=10,y=50)
        name = StringVar()
        nameEntry = Entry(tkWindow, textvariable=name).place(x=80,y=50)  

        #address label and entry box
        addressLabel = Label(tkWindow,text="Address").place(x=10,y=100) 
        address = StringVar()
        addressEntry = Entry(tkWindow, textvariable=address).place(x=80,y=100) 

        #accountno label and entry box
        accountnoLabel = Label(tkWindow,text="Account Number").place(x=10,y=150) 
        accountno = StringVar()
        accountnoEntry = Entry(tkWindow, textvariable=accountno).place(x=120,y=150) 

        #amount label and entry box
        amountLabel = Label(tkWindow,text="Amount ").place(x=10,y=200) 
        amount  = StringVar()
        amountEntry = Entry(tkWindow, textvariable=amount ).place(x=80,y=200) 

        #pay button
        payButton = Button(tkWindow, text="Donate",command=mysqlpythondon).place(x=150,y=250)

        #main loop
        tkWindow.mainloop()

