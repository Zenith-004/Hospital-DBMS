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
st="select * from donations"
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
tree['column']=("S.NO","Name","Address","Account No","Amount")

# format our columns
tree.column("#0",width=0,stretch=NO)
tree.column("S.NO",anchor=W,width=140)
tree.column("Name",anchor=W, width=120)
tree.column("Address", anchor=CENTER,width=100)
tree.column("Account No",anchor=W,width=140)
tree.column("Amount",anchor=W,width=140)


# create headings
tree.heading("S.NO",text="S.NO",anchor=W)
tree.heading("Name",text="Name", anchor=W)
tree.heading("Address",text="Address",anchor=CENTER)
tree.heading("Account No",text="Account No",anchor=W)
tree.heading("Amount",text="Amount",anchor=W)

# add data
count=1
for record in data:
    tree.insert(parent='',index='end',text="", values=(count,record[0],record[1],record[2],record[3]))
    count= count+1
# pack to screen 
tree.pack(pady=20)


addframe=Frame(root)
addframe.pack(pady=20)


n1=Label(addframe,text="Name")
n1.grid(row=0,column=0)

il=Label(addframe,text="Address")
il.grid(row=0,column=1)

tl=Label(addframe,text="Account No")
tl.grid(row=0,column=2)

tl=Label(addframe,text="Amount")
tl.grid(row=0,column=3)

namebox=Entry(addframe)
namebox.grid(row=1,column=0)

addressbox=Entry(addframe)
addressbox.grid(row=1,column=1)

accnobox=Entry(addframe)
accnobox.grid(row=1,column=2)

amountbox=Entry(addframe)
amountbox.grid(row=1,column=3)




#add record
def addrecord():
    global count
    tree.insert(parent='',index='end',text="",iid=count, values=(count,namebox.get(),addressbox.get(),accnobox.get(),amountbox.get()))

    #mysql part
    mycon=sql.connect(host="localhost",user="root",passwd="Shelshar@04", database="project")
    if mycon.is_connected():
        print("Successfully Conected to database")
    else:
        print("Access denied")
    cursor=mycon.cursor()
    st="insert into donations values('{}','{}','{}','{}')".format(namebox.get(),addressbox.get(),accnobox.get(),amountbox.get())
    cursor.execute(st)
    mycon.commit()
    st="select * from donations"
    cursor.execute(st)
    data=cursor.fetchall()
    for row in data:
        print(row)
    messagebox.showinfo("showinfo", "Donation Successful")
    #clear the boxes
    namebox.delete(0,END)
    addressbox.delete(0,END)
    accnobox.delete(0,END)
    amountbox.delete(0,END)

    
# buttons
# add record
addrecord= Button(root, text="Add record",command=addrecord)
addrecord.pack(pady=20)


root.mainloop()

