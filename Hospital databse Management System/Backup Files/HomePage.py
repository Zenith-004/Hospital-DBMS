from donations import *
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox 


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



