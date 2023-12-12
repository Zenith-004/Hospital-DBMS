from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def adminhomepage():
    global window
    window=Tk()
    #window
    window.title('Admin Medicare')
    #setting tkinter window size
    window.geometry("600x300")
    window.configure(bg='teal')

    #heading label
    headingLabel = Label(window, text="ADMIN", fg='white', bg='#3A3B3C',height='3',width='7',font=("Arial", 15)).place(x=270,y=5)
    #buttons
    btn1=Button(window, text="HOME", fg='white', bg='#3A3B3C', height='2')
    btn1.place(x=95, y=100)

    btn2=Button(window, text="AVAILABILITY", fg='white', bg='#3A3B3C',height='2')
    btn2.place(x=145, y=100)

    btn3=Button(window, text="PACKAGES", fg='white', bg='#3A3B3C',height='2')
    btn3.place(x=233, y=100)

    btn4=Button(window, text="APPOINMENTS", fg='white', bg='#3A3B3C',height='2')
    btn4.place(x=307, y=100)

    btn5=Button(window, text="DONATIONS",fg='white', bg='#3A3B3C',height='2')
    btn5.place(x=405, y=100)


    window.mainloop()

#def donations():
    
    #window.destroy()
    #donationcode()

adminhomepage()

