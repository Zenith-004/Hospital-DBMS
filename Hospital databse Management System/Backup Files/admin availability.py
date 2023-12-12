import mysql.connector as sql
from tkinter import*
from tkinter import ttk
from tkinter import messagebox 


#mysql python connector
mycon=sql.connect(host="localhost",user="root",passwd="Shelshar@04", database="project")
if mycon.is_connected():
    print("Successfully Conected to database")
else:
    print("Access denied")
cursor=mycon.cursor()
st="select * from  availability"
cursor.execute(st)
data=cursor.fetchall()
for row in data:
    print(row)


# window
root= Tk()
root.title("tree view")
root.geometry("700x700")

tree=ttk.Treeview(root)

# Defining columns
tree['column']=("S.NO","UserName","Name","Required_beds")

# format our columns
tree.column("#0",width=0,stretch=NO)
tree.column("S.NO",anchor=W,width=140)
tree.column("UserName",anchor=W, width=120)
tree.column("Name", anchor=CENTER,width=100)
tree.column("Required_beds",anchor=W,width=140)



# create headings
tree.heading("S.NO",text="S.NO",anchor=W)
tree.heading("UserName",text="UserName", anchor=W)
tree.heading("Name",text="Name",anchor=CENTER)
tree.heading("Required_beds",text="Required_beds",anchor=W)


# add data
count=1
for record in data:
    tree.insert(parent='',index='end',text="", values=(count,record[0],record[1],record[2]))
    count= count+1
# pack to screen 
tree.pack(pady=20)


addframe=Frame(root)
addframe.pack(pady=20)


n1=Label(addframe,text="UserName")
n1.grid(row=0,column=0)

il=Label(addframe,text="Name")
il.grid(row=0,column=1)

tl=Label(addframe,text="Required_beds")
tl.grid(row=0,column=2)

UserNamebox=Entry(addframe)
UserNamebox.grid(row=1,column=0)

Namebox=Entry(addframe)
Namebox.grid(row=1,column=1)

Required_bedsbox=Entry(addframe)
Required_bedsbox.grid(row=1,column=2)




#add record
def addrecord():
    global count
    tree.insert(parent='',index='end',text="",iid=count, values=(count,UserNamebox.get(),Namebox.get(),Required_bedsbox.get()))

    mycon=sql.connect(host="localhost",user="root",passwd="Shelshar@04", database="project")
    if mycon.is_connected():
        print("Successfully Conected to database")
    else:
        print("Access denied")
    cursor=mycon.cursor()
    st="insert into availability values('{}','{}','{}')".format(UserNamebox.get(), Namebox.get(),Required_bedsbox.get())
    cursor.execute(st)
    mycon.commit()
    st="select * from  availability"
    cursor.execute(st)
    data=cursor.fetchall()
    for row in data:
        print(row)
    #clear the boxes
    UserNamebox.delete(0,END)
    Namebox.delete(0,END)
    Required_bedsbox.delete(0,END)
    
# select record
def selectrecord():
    #clear entery boxes
    UserNamebox.delete(0,END)
    Namebox.delete(0,END)
    Required_bedsbox.delete(0,END)

    #grab record number
    selected=tree.focus()
    #grab record values
    values = tree.item(selected,'values')
    
    #temp.config(text=values[1])

    #output to entery boxes
    UserNamebox.insert(0,values[1])
    Namebox.insert(0,values[2])
    Required_bedsbox.insert(0,values[3])
     

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
    st="update availability set name='{}', beds='{}' where username='{}'".format(Namebox.get(),Required_bedsbox.get(),UserNamebox.get())
    print(Namebox.get(),Required_bedsbox.get(),UserNamebox.get())
    cursor.execute(st)
    mycon.commit()
    st="select * from  availability"
    cursor.execute(st)
    data=cursor.fetchall()
    for row in data:
        print(row)

    #save new data
    tree.item(selected,text="",values=(count-1,UserNamebox.get(),Namebox.get(),Required_bedsbox.get()))

    #delete text in text boxes
    UserNamebox.delete(0,END)
    Namebox.delete(0,END)
    Required_bedsbox.delete(0,END)



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
    st="delete from availability where username='{}'".format(UserNamebox.get())
    print(Namebox.get(),Required_bedsbox.get(),UserNamebox.get())
    cursor.execute(st)
    mycon.commit()
    st="select * from  availability"
    cursor.execute(st)
    data=cursor.fetchall()
    for row in data:
        print(row)

    #selection of record to delete
    x=tree.selection()[0]
    tree.delete(x)

    #delete text in text boxes
    UserNamebox.delete(0,END)
    Namebox.delete(0,END)
    Required_bedsbox.delete(0,END)



    


    
    
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


temp=Label(root,text="")
temp.pack (pady=10)


root.mainloop()

