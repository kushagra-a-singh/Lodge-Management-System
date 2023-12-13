from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
from tkcalendar import DateEntry

Username1 = "root"
password1 = "root"
con = mysql.connect(host="localhost",
                    user="root",
                    password="root",
                    database="LMS")
cursor = con.cursor()

def insert():
    NAME = e_NAME.get()
    PHN = e_PHN.get()
    ADHAR_NO = e_ADHAR_NO.get()
    NOP = e_NOP.get()
    CID = e_CID.get()
    COD = e_COD.get()
    ROOM_NO = e_ROOM_NO.get()
    TOT_COST = e_TOT_COST.get()
    MOP = e_MOP.get()
    PS = e_PS.get()

    con = mysql.connect(host="localhost",
                        user="root",
                        password="root",
                        database="LMS")
    cursor = con.cursor()
    cursor.execute("SELECT ROOM_TYPE,ROOM_STATUS FROM ROOMS WHERE ROOM_NO='" + ROOM_NO + "'")
    room_status = cursor.fetchone()

    if (
            NAME == "" or PHN == "" or ADHAR_NO == "" or NOP == "" or CID == "" or COD == "" or ROOM_NO == "" or TOT_COST == "" or MOP == "" or PS == ""):
        show()
        Messagebox.showinfo("Insert Status", "All Fields Are required")

    elif room_status[1] == "OCCUPIED":
        show()
        Messagebox.showerror("Room Error",
                             "Room is already occupied\nRoomNo=" + ROOM_NO + "\nRoomType=" + room_status[0])
        cursor.execute("SELECT ROOM_NO FROM ROOMS WHERE ROOM_TYPE=" + '"' + room_status[0] + '"')
        other_room = cursor.fetchall()

        if other_room == []:
            info_window = Toplevel()
            text_add = "No other " + room_status[0] + "rooms are available"
            Label(info_window, text=text_add, font=(16)).pack(side=TOP)
        else:
            info_window = Toplevel()
            text_add = "Other Rooms available in" + room_status[0] + "are"
            Label(info_window, text=text_add, font=(16)).pack(side=TOP)
            Button(info_window, text="Ok", command=info_window.destroy).pack(side=BOTTOM)

            for i in other_room:
                Label(info_window, text=i[0], font=(16)).pack(side=TOP)

    else:
        cursor.execute(
            "insert into hotel_management values('" + NAME + "','" + PHN + "','" + ADHAR_NO + "','" + NOP + "','" + CID + "','" + COD + "','" + ROOM_NO + "','" + TOT_COST + "','" + MOP + "','" + PS + "')")
        cursor.execute("commit")
        cursor.execute("update rooms set room_status=\'OCCUPIED\' WHERE ROOM_NO=" + ROOM_NO)
        cursor.execute("commit")
        e_NAME.delete(0, 'end')
        e_PHN.delete(0, 'end')
        e_ADHAR_NO.delete(0, 'end')
        e_NOP.delete(0, 'end')
        e_CID.delete(0, 'end')
        e_COD.delete(0, 'end')
        e_ROOM_NO.delete(0, 'end')
        e_TOT_COST.delete(0, 'end')
        e_MOP.delete(0, 'end')
        e_PS.delete(0, 'end')
        show()
        Messagebox.showinfo("Insert Status", "Inserted Successfully")

def delete():
    if (e_ROOM_NO.get() == ""):
        show()
        Messagebox.showinfo("Deleted Status", "ROOM NUMBER is compulsory for delete")
    else:
        con = mysql.connect(host="localhost", user=Username1, password=password1, database="LMS")
        cursor = con.cursor()

        cursor.execute("delete from hotel_management where ROOM_NUMBER='" + e_ROOM_NO.get() + "'")
        cursor.execute("commit")
        cursor.execute("update rooms set room_status=\'UNOCCUPIED\' WHERE ROOM_NO=" + e_ROOM_NO.get())
        cursor.execute("commit")
        b_DEL.config(command=delete)
        e_NAME.delete(0, 'end')
        e_PHN.delete(0, 'end')
        e_ADHAR_NO.delete(0, 'end')
        e_NOP.delete(0, 'end')
        e_CID.delete(0, 'end')
        e_COD.delete(0, 'end')
        e_ROOM_NO.delete(0, 'end')
        e_TOT_COST.delete(0, 'end')
        e_MOP.delete(0, 'end')
        e_PS.delete(0, 'end')
        show()
        Messagebox.showinfo("Delete Status", "Deleted Successfully")

def Update():
    NAME1 = e_NAME.get()
    PHN1 = e_PHN.get()
    ADHAR_NO1 = e_ADHAR_NO.get()
    NOP1 = e_NOP.get()
    CID1 = e_CID.get()
    COD1 = e_COD.get()
    ROOM_NO1 = e_ROOM_NO.get()
    TOT_COST1 = e_TOT_COST.get()
    MOP1 = e_MOP.get()
    PS1 = e_PS.get()

    if (
            NAME1 == "" or PHN1 == "" or ADHAR_NO1 == "" or NOP1 == "" or CID1 == "" or COD1 == "" or ROOM_NO1 == "" or TOT_COST1 == "" or MOP1 == "" or PS1 == ""):
        show()
        Messagebox.showinfo("Update Status", "All Fields Are required")
    else:
        cursor.execute(
            "update hotel_management set Name='" + NAME1 + "',Phone_number='" + PHN1 + "',Adhar_no='" + ADHAR_NO1 + "',Number_of_people='" + NOP1 + "',Checkin_date='" + CID1 + "',Checkout_date='" + COD1 + "',Room_Number='" + ROOM_NO1 + "',Total_Cost='" + TOT_COST1 + "',Mode_of_Payment='" + MOP1 + "',Payment_Status='" + PS1 + "' where Room_Number='" + ROOM_NO1 + "'")
        cursor.execute("commit")
        show()
        e_NAME.delete(0, 'end')
        e_PHN.delete(0, 'end')
        e_ADHAR_NO.delete(0, 'end')
        e_NOP.delete(0, 'end')
        e_CID.delete(0, 'end')
        e_COD.delete(0, 'end')
        e_ROOM_NO.delete(0, 'end')
        e_TOT_COST.delete(0, 'end')
        e_MOP.delete(0, 'end')
        e_PS.delete(0, 'end')

        show()
        Messagebox.showinfo("Update Status", "Update Successfully")

def get():
    if (e_ROOM_NO.get() == ""):
        show()
        Messagebox.showinfo("Fetch Status", "ROOM NUMBER is compulsory for fetching")
    else:
        cursor.execute("select * from hotel_management where ROOM_NUMBER='" + e_ROOM_NO.get() + "'")
        rows = cursor.fetchall()

        clear()
        for row in rows:
            e_NAME.insert(0, row[0])
            e_PHN.insert(0, row[1])
            e_ADHAR_NO.insert(0, row[2])
            e_NOP.insert(0, row[3])
            e_CID.insert(0, row[4])
            e_COD.insert(0, row[5])
            e_ROOM_NO.insert(0, row[6])
            e_TOT_COST.insert(0, row[7])
            e_MOP.insert(0, row[8])
            e_PS.insert(0, row[9])

def show():
    cursor.execute("select * from hotel_management")
    rows = cursor.fetchall()
    list1.delete(0, END) 

    insertData = "Name          RoomNo        AmountPaid"
    list1.insert(END, insertData)

    for row in rows:
        insertData = str(row[0]) + '        ' + str(row[6]) + '        ' + str(row[7])
        list1.insert(END, insertData)
    con.commit() 

def clear():
    e_NAME.delete(0, 'end')
    e_PHN.delete(0, 'end')
    e_ADHAR_NO.delete(0, 'end')
    e_NOP.delete(0, 'end')
    e_CID.delete(0, 'end')
    e_COD.delete(0, 'end')
    e_MOP.delete(0, 'end')
    e_ROOM_NO.delete(0, 'end')
    e_TOT_COST.delete(0, 'end')
    e_PS.delete(0, 'end')


root = Tk()
# layout
winbackground = "#25C3C6"  
labelbackground = "#ffc87c" 
textcolour = "black"
restbg = "white"

root.title("HOTEL MANAGEMENT")
root.configure(background=winbackground)
# syntax: Width x Height
root.state('zoomed')
# syntax: Width,Height
root.maxsize(1100, 70)
root.minsize(1100, 700)
# now start the text
TITLE = Label(root, text="HOTEL DOWNTOWN", font=("Algerian", 50), fg=textcolour, bg=labelbackground)
TITLE.place(x=360, y=14)
NAME = Label(root, text="NAME", font=("Bold 20"), fg=textcolour, bg=labelbackground)
NAME.place(x=10, y=100)
PHN = Label(root, text="PHONE NUMBER", font="Bold 20", fg=textcolour, bg=labelbackground)
PHN.place(x=10, y=150)
ADHAR_NO = Label(root, text="ADHAR NUMBER", font="Bold 20", fg=textcolour, bg=labelbackground)
ADHAR_NO.place(x=10, y=200)
NOP = Label(root, text="NUMBER OF PERSON", font="Bold 20", fg=textcolour, bg=labelbackground)
NOP.place(x=10, y=250)
CID = Label(root, text="Check-in Date", font="Bold 20", fg=textcolour, bg=labelbackground)
CID.place(x=10, y=300)
COD = Label(root, text="Check-out Date", font="Bold 20", fg=textcolour, bg=labelbackground)
COD.place(x=10, y=350)
ROOM_NO = Label(root, text="ROOM_NUMBER", font="Bold 20", fg=textcolour, bg=labelbackground)
ROOM_NO.place(x=10, y=400)
TOT_COST = Label(root, text="TOTAL_COST", font="Bold 20", fg=textcolour, bg=labelbackground)
TOT_COST.place(x=10, y=450)
MOP = Label(root, text="Mode Of Payment", font="Bold 20", fg=textcolour, bg=labelbackground)
MOP.place(x=10, y=500)
PS = Label(root, text="Payment Status", font="Bold 20", fg=textcolour, bg=labelbackground)
PS.place(x=10, y=550)

# ENTRY BOX
e_NAME = Entry(root, border=1, width="18", font=("Century Gothic", 20), fg=textcolour, bg=restbg)
e_NAME.place(x=305, y=100)
e_PHN = Entry(root, border=1, width="18", font=("Century Gothic", 20), fg=textcolour, bg=restbg)
e_PHN.place(x=305, y=150)
e_ADHAR_NO = Entry(root, border=1, width="18", font=("Century Gothic", 20), fg=textcolour, bg=restbg)
e_ADHAR_NO.place(x=305, y=200)
e_NOP = Entry(root, border=1, width="18", font=("Century Gothic", 20), fg=textcolour, bg=restbg)
e_NOP.place(x=305, y=250)
e_CID = DateEntry(root, border=1, selectmode='day', width="18", font=("Century Gothic", 19), fg=textcolour, bg=restbg)
e_CID.place(x=305, y=300)
e_COD = DateEntry(root, border=1, selectmode='day', width="18", font=("Century Gothic", 19), fg=textcolour, bg=restbg)
e_COD.place(x=305, y=350)
e_ROOM_NO = Entry(root, border=1, width="18", font=("Century Gothic", 20), fg=textcolour, bg=restbg)
e_ROOM_NO.place(x=305, y=400)
e_TOT_COST = Entry(root, border=1, width="18", font=("Century Gothic", 20), fg=textcolour, bg=restbg)
e_TOT_COST.place(x=305, y=450)
e_MOP = Entry(root, border=1, width="18", font=("Century Gothic", 20), fg=textcolour, bg=restbg)
e_MOP.place(x=305, y=500)
e_PS = Entry(root, border=1, width="18", font=("Century Gothic", 20), fg=textcolour, bg=restbg)
e_PS.place(x=305, y=550)

# BUTTONS
b_INSERT = Button(root, width=10, text="INSERT", font=("Century Gothic", 20), fg=textcolour, bg=restbg, relief=SOLID, highlightthickness=2, bd=1, command=insert)
b_INSERT.place(x=240, y=620)
b_UPDATE = Button(root, width=10, text="MODIFY", font=("Century Gothic", 20), fg=textcolour, bg=restbg, relief=SOLID, highlightthickness=2, bd=1, command=Update)
b_UPDATE.place(x=430, y=620)
b_DEL = Button(root, width=10, text="DELETE", font=("Century Gothic", 20), fg=textcolour, bg=restbg, relief=SOLID, highlightthickness=2, bd=1, command=delete)
b_DEL.place(x=620, y=620)
b_GET = Button(root, width=10, text="GET", font=("Century Gothic", 20), fg=textcolour, bg=restbg, relief=SOLID, highlightthickness=2, bd=1, command=get)
b_GET.place(x=810, y=620)
b_CLEAR = Button(root, width=10, text="CLEAR", font=("Century Gothic", 20), fg=textcolour, bg=restbg, relief=SOLID, highlightthickness=2, bd=1, command=clear)
b_CLEAR.place(x=50, y=620)

# LIST BOX
list1 = Listbox(root, font="Bold 20", height=15, width=32, highlightthickness=2, bd=1, fg=textcolour, bg=restbg)
list1.place(x=600, y=100)
show()
list1.update_idletasks()
root.mainloop()