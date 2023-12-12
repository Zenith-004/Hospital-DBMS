from tkinter import *
import mysql.connector as sql
from tkinter import messagebox 

#add record
def availability():
    
    #mysql part
    mycon=sql.connect(host="localhost",user="root",passwd="Shelshar@04", database="project")
    if mycon.is_connected():
        print("Successfully Conected to database")
    else:
        print("Access denied")
    cursor=mycon.cursor()
    st="insert into availability values('{}','{}','{}')".format(Submit_username.get(),Submit_name.get(),Submit_numberofbedsrequired.get())
    cursor.execute(st)
    mycon.commit()
    st="select * from  availability"
    cursor.execute(st)
    data=cursor.fetchall()
    for row in data:
        print(row)
    messagebox.showinfo("showinfo", "Booking Successful")
    Submit_username.delete(0,END)
    Submit_name.delete(0,END)
    Submit_numberofbedsrequired.delete(0,END)





ws = Tk()
ws.title('Medicare')
ws.config(bg='teal')

f = ('Times', 14)
var = StringVar()
var.set('male')




right_frame = Frame(
    ws, 
    bd=2, 
    bg='teal',
    relief=SOLID, 
    padx=10, 
    pady=10
    )

Label(
    right_frame, 
    text="Enter Username", 
    bg='#CCCCCC',
    font=f
    ).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Enter Name", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Number of beds required", 
    bg='#CCCCCC',
    font=f
    ).grid(row=5, column=0, sticky=W, pady=10)


Submit_username=Entry(
    right_frame,
    font=f
    )
    
Submit_name = Entry(
    right_frame, 
    font=f
    )


Submit_numberofbedsrequired=Entry(
    right_frame,
    font=f
    )

Submit_btn = Button(
    right_frame, 
    width=15, 
    text='Submit', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command= availability
)

Submit_username.grid(row=0, column=1, pady=10, padx=20)
Submit_name.grid(row=1, column=1, pady=10, padx=20)

Submit_numberofbedsrequired.grid(row=5, column=1, pady=10, padx=20)
Submit_btn.grid(row=8, column=1, pady=10, padx=20)
right_frame.pack()


ws.mainloop()
