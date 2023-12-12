from tkinter import *
from tkinter import ttk
import mysql.connector as sql
from functools import partial
from tkinter import messagebox  
from PIL import ImageTk,Image



def adminusersscode():
    #mysql python connector
    mycon=sql.connect(host="localhost",user="root",passwd="Shelshar@04", database="project")
    if mycon.is_connected():
        print("Successfully Conected to database")
    else:
        print("Access denied")
    cursor=mycon.cursor()
    st="select * from login"
    cursor.execute(st)
    data=list(cursor.fetchall())
    for row in data:
        print(row)



    # window
    root= Tk()
    root.title("tree view")
    root.geometry("700x700")

    tree=ttk.Treeview(root)

    # Defining columns
    tree['column']=("S.NO","Username","Password")

    # format our columns
    tree.column("#0",width=0,stretch=NO)
    tree.column("S.NO",anchor=W,width=0,stretch=NO)
    tree.column("Username",anchor=W, width=120)
    tree.column("Password", anchor=W,width=140)


    # create headings
    tree.heading("S.NO",text="S.NO",anchor=W)
    tree.heading("Username",text="Username", anchor=W)
    tree.heading("Password",text="Password",anchor=CENTER)
    # add data
    global count
    count=1
    for record in data:
        tree.insert(parent='',index='end',text="", values=(count,record[0],record[1]))
        count= count+1
    # pack to screen 
    tree.pack(pady=20)


    addframe=Frame(root)
    addframe.pack(pady=20)


    n1=Label(addframe,text="Username")
    n1.grid(row=0,column=0)

    il=Label(addframe,text="Password")
    il.grid(row=0,column=1)


    Usernamebox=Entry(addframe)
    Usernamebox.grid(row=1,column=0)

    Passwordbox=Entry(addframe)
    Passwordbox.grid(row=1,column=1)




    #add record
    def addrecord():
        global count
        tree.insert(parent='',index='end',text="",iid=count, values=(count,Usernamebox.get(),Passwordbox.get()))

        #mysql part
        mycon=sql.connect(host="localhost",user="root",passwd="Shelshar@04", database="project")
        if mycon.is_connected():
            print("Successfully Conected to database")
        else:
            print("Access denied")
        cursor=mycon.cursor()
        st="insert into login values('{}','{}')".format(Usernamebox.get(),Passwordbox.get())
        cursor.execute(st)
        mycon.commit()
        st="select * from login"
        cursor.execute(st)
        data=cursor.fetchall()
        for row in data:
            print(row)
        messagebox.showinfo("showinfo", "SignUp Successful")
        #clear the boxes
        Usernamebox.delete(0,END)
        Passwordbox.delete(0,END)

    # update record
    def updaterecord():
        #grab record number
        selected=tree.focus()

        #mysql part
        mycon=sql.connect(host="localhost",user="root",passwd="Shelshar@04", database="project")
        if mycon.is_connected():
            print("Successfully Conected to database")
        else:
            print("Access denied")
        cursor=mycon.cursor()
        st="update login set password='{}' where username='{}'".format(Passwordbox.get(),Usernamebox.get())
        cursor.execute(st)
        mycon.commit()
        st="select * from  login"
        cursor.execute(st)
        data=cursor.fetchall()
        for row in data:
            print(row)

        #save new data
        tree.item(selected,text="",values =(count-1,Usernamebox.get(),Passwordbox.get()))

        #delete text in text boxes
        Usernamebox.delete(0,END)
        Passwordbox.delete(0,END)


    # select record
    def selectrecord():
        #clear entery boxes
        Usernamebox.delete(0,END)
        Passwordbox.delete(0,END)

        #grab record number
        selected=tree.focus()

        #grab record values
        values = tree.item(selected,'values')
        
        #temp.config(text=values[1])

        #output to entery boxes
        Usernamebox.insert(0,values[1])
        Passwordbox.insert(0,values[2])


    # delete record
    def deleterecord():
        #grab record number
        selected=tree.focus()

        #mysql part
        mycon=sql.connect(host="localhost",user="root",passwd="Shelshar@04", database="project")
        if mycon.is_connected():
            print("Successfully Conected to database")
        else:
            print("Access denied")
        cursor=mycon.cursor()
        st="delete from login where username='{}'".format(Usernamebox.get())
        cursor.execute(st)
        mycon.commit()
        st="select * from  login"
        cursor.execute(st)
        data=cursor.fetchall()
        for row in data:
            print(row)

        #selection of record to delete
        x=tree.selection()[0]
        tree.delete(x)

        #delete text in text boxes
        Usernamebox.delete(0,END)
        Passwordbox.delete(0,END)


        
        
    # buttons
    # add record
    addrecord= Button(root, text="Add record",command=addrecord)
    addrecord.pack(pady=10)

    delrecord= Button(root, text="Delete record",command=deleterecord)
    delrecord.pack(pady=10)

    selectrecord= Button(root, text="Select record",command=selectrecord)
    selectrecord.pack(pady=10)

    updaterecord= Button(root, text="Update record",command=updaterecord)
    updaterecord.pack(pady=10)

    #close
    def close():
        root.destroy()
        adminhomepage()
        
    close= Button(root, text="close",command=close)
    close.pack(pady=10)

    temp=Label(root,text="")
    temp.pack (pady=10)


    root.mainloop()

adminpackagescode()
