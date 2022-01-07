def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mval.get()
        email = eval.get()
        address = aval.get()
        gender = gval.get()
        dob = dval.get()
        addtime = time.strftime("%H:%M:%S")
        adddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into studdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (id, name, mobile, email, address, gender, dob, adddate, addtime))
            con.commit()
            res = messagebox.askyesnocancel('notification',
                                            'Id{},Name{} added succefully .....want clean form'.format(id, name),
                                            parent=addroot)
            if (res == True):
                idval.set('')
                nameval.set('')
                mval.set('')
                eval.set('')
                aval.set('')
                gval.set('')
                dval.set('')
        except:
            messagebox.showerror('notification', 'id alredy exits try another', parent=addroot)
        strr = 'select * from studdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1] , i[2] ,i[3] ,i[4] ,i[5] ,i[6] ,i[7] ,i[8]]
            studenttable.insert('', END, values=vv)

    addroot = Toplevel(master=DataFrame)
    addroot.grab_set()
    addroot.title('STUDENT MANAGEMENT SYSTEM')
    addroot.config(bg='dark gray')
    label = Label(addroot, text='ADD STUDENT', bg='dark gray', font=('chiller', 38, 'bold'))
    label.place(x=550, y=10)
    idlabel = Label(addroot, text='Enter Id :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlabel.place(x=450, y=70)
    namelabel = Label(addroot, text='Enter Name :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelabel.place(x=450, y=130)
    mlabel = Label(addroot, text='Enter Mobile:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                   width=12, anchor='w')
    mlabel.place(x=450, y=190)
    elabel = Label(addroot, text='Enter Email:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                   width=12, anchor='w')
    elabel.place(x=450, y=250)
    alabel = Label(addroot, text='Enter address:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                   width=12, anchor='w')
    alabel.place(x=450, y=310)
    glabel = Label(addroot, text='Enter Gender:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                   width=12, anchor='w')
    glabel.place(x=450, y=370)
    dlabel = Label(addroot, text='Enter d.o.b:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                   width=12, anchor='w')
    dlabel.place(x=450, y=430)
    idval = StringVar()
    nameval = StringVar()
    mval = StringVar()
    eval= StringVar()
    aval = StringVar()
    gval = StringVar()
    dval = StringVar()
    identry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval, width=25)
    identry.place(x=700, y=70)
    nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval, width=25)
    nameentry.place(x=700, y=130)
    mentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=mval, width=25)
    mentry.place(x=700, y=190)
    eentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=eval, width=25)
    eentry.place(x=700, y=250)
    aentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=aval, width=25)
    aentry.place(x=700, y=310)
    gentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=gval, width=25)
    gentry.place(x=700, y=370)
    dentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dval, width=25)
    dentry.place(x=700, y=430)
    submibutton = Button(addroot, text='submit', font=('roman', 25, 'bold'), width=28, relief=RIDGE,
                         borderwidth=4, bd=6, bg='pink', activebackground='purple', activeforeground='yellow',
                         command=submitadd)
    submibutton.place(x=480, y=490)
    addroot.mainloop()


def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mval.get()
        email = eval.get()
        address = aval.get()
        gender = gval.get()
        dob = dval.get()
        adddate = time.strftime("%d/%m/%Y")
        if(id !=''):
          strr='select * from studdata where id=%s'
          mycursor.execute(strr,(id))
          datas=mycursor.fetchall()
          studenttable.delete(*studenttable.get_children())
          for i in datas:
              vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
              studenttable . insert('', END, values=vv)
        elif (name != ''):
              strr = 'select * from studdata where name=%s'
              mycursor.execute(strr, (name))
              datas = mycursor.fetchall()
              studenttable.delete(*studenttable.get_children())
              for i in datas:
                  vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                  studenttable.insert('', END, values=vv)

        elif (mobile != ''):
              strr = 'select * from studdata where mobile=%s'
              mycursor.execute(strr, (mobile))
              datas = mycursor.fetchall()
              studenttable.delete(*studenttable.get_children())
              for i in datas:
                  vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                  studenttable.insert('', END, values=vv)

        elif (email != ''):
              strr = 'select * from studdata where email=%s'
              mycursor.execute(strr, (email))
              datas = mycursor.fetchall()
              studenttable.delete(*studenttable.get_children())
              for i in datas:
                  vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                  studenttable.insert('', END, values=vv)

        elif (address != ''):
              strr = 'select * from studdata where address=%s'
              mycursor.execute(strr, (address))
              datas = mycursor.fetchall()
              studenttable.delete(*studenttable.get_children())
              for i in datas:
                  vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                  studenttable.insert('', END, values=vv)

        elif (gender != ''):
              strr = 'select * from studdata where gender=%s'
              mycursor.execute(strr, (gender))
              datas = mycursor.fetchall()
              studenttable.delete(*studenttable.get_children())
              for i in datas:
                  vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                  studenttable.insert('', END, values=vv)

        elif (dob != ''):
              strr = 'select * from studdata where dob=%s'
              mycursor.execute(strr,(dob))
              datas = mycursor.fetchall()
              studenttable.delete(*studenttable.get_children())
              for i in datas:
                  vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                  studenttable.insert('', END, values=vv)

        elif (adddate != ''):
              strr = 'select * from studdata where adddate=%s'
              mycursor.execute(strr, (adddate))
              datas = mycursor.fetchall()
              studenttable.delete(*studenttable.get_children())
              for i in datas:
                  vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                  studenttable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataFrame)
    searchroot.grab_set()
    searchroot.title('STUDENT MANAGEMENT SYSTEM')
    searchroot.config(bg='light yellow')
    idlabel = Label(searchroot, text='Enter Id :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlabel.place(x=450, y=10)
    namelabel = Label(searchroot, text='Enter Name :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelabel.place(x=450, y=70)
    mlabel = Label(searchroot, text='Enter Mobile:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                   borderwidth=3, width=12, anchor='w')
    mlabel.place(x=450, y=130)
    elabel = Label(searchroot, text='Enter Email:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                   borderwidth=3, width=12, anchor='w')
    elabel.place(x=450, y=190)
    alabel = Label(searchroot, text='Enter address:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                   borderwidth=3, width=12, anchor='w')
    alabel.place(x=450, y=250)
    glabel = Label(searchroot, text='Enter Gender:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                   borderwidth=3, width=12, anchor='w')
    glabel.place(x=450, y=310)
    dlabel = Label(searchroot, text='Enter d.o.b:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                   borderwidth=3, width=12, anchor='w')
    dlabel.place(x=450, y=370)
    datelabel = Label(searchroot, text='Enter date:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    datelabel.place(x=450, y=440)
    idval = StringVar()
    nameval = StringVar()
    mval = StringVar()
    eval = StringVar()
    aval = StringVar()
    gval = StringVar()
    dval = StringVar()
    dateval = StringVar()
    identry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval, width=25)
    identry.place(x=700, y=10)
    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval, width=25)
    nameentry.place(x=700, y=70)
    mentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=mval, width=25)
    mentry.place(x=700, y=130)
    eentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=eval, width=25)
    eentry.place(x=700, y=190)
    aentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=aval, width=25)
    aentry.place(x=700, y=250)
    gentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=gval, width=25)
    gentry.place(x=700, y=310)
    dentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dval, width=25)
    dentry.place(x=700, y=370)
    dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval, width=25)
    dateentry.place(x=700, y=440)

    submibutton = Button(searchroot, text='search', font=('roman', 25, 'bold'), width=28, relief=RIDGE,
                         borderwidth=4, bd=6, bg='pink', activebackground='purple', activeforeground='yellow',
                         command=search)
    submibutton.place(x=480, y=500)
    searchroot.mainloop()


def deletestudent():
    cc=studenttable.focus()
    content=studenttable.item(cc)
    pp=content['values'][0]
    strr='delete from studdata where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','delete suceefully.....')
    strr = 'select *from studdata '
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)


def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mval.get()
        email = eval.get()
        address = aval.get()
        gender = gval.get()
        dob = dval.get()
        time = timeval.get()
        date = dateval.get()
        strr='update studdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('notification','Id {} updated successfully....'.format(id),parent=updateroot)
        strr = 'select *from studdata '
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)
    updateroot = Toplevel(master=DataFrame)
    updateroot.grab_set()
    updateroot.title('STUDENT MANAGEMENT SYSTEM')
    updateroot.config(bg='light green')
    idlabel = Label(updateroot, text='Enter Id :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlabel.place(x=450, y=10)
    namelabel = Label(updateroot, text='Enter Name :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelabel.place(x=450, y=70)
    mlabel = Label(updateroot, text='Enter Mobile:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                   borderwidth=3, width=12, anchor='w')
    mlabel.place(x=450, y=130)
    elabel = Label(updateroot, text='Enter Email:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                   borderwidth=3, width=12, anchor='w')
    elabel.place(x=450, y=190)
    alabel = Label(updateroot, text='Enter address:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                   borderwidth=3, width=12, anchor='w')
    alabel.place(x=450, y=250)
    glabel = Label(updateroot, text='Enter Gender:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                   borderwidth=3, width=12, anchor='w')
    glabel.place(x=450, y=310)
    dlabel = Label(updateroot, text='Enter d.o.b:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                   borderwidth=3, width=12, anchor='w')
    dlabel.place(x=450, y=370)
    datelabel = Label(updateroot, text='Enter date:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    datelabel.place(x=450, y=440)
    timelabel = Label(updateroot, text='Enter time:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    timelabel.place(x=450, y=500)
    idval = StringVar()
    nameval = StringVar()
    mval = StringVar()
    eval = StringVar()
    aval = StringVar()
    gval = StringVar()
    dval = StringVar()
    dateval = StringVar()
    timeval = StringVar()
    identry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval, width=25)
    identry.place(x=700, y=10)
    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval, width=25)
    nameentry.place(x=700, y=70)
    mentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=mval, width=25)
    mentry.place(x=700, y=130)
    eentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=eval, width=25)
    eentry.place(x=700, y=190)
    aentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=aval, width=25)
    aentry.place(x=700, y=250)
    gentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=gval, width=25)
    gentry.place(x=700, y=310)
    dentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dval, width=25)
    dentry.place(x=700, y=370)
    dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval, width=25)
    dateentry.place(x=700, y=440)
    timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=timeval, width=25)
    timeentry.place(x=700, y=500)

    submibutton = Button(updateroot, text='update', font=('roman', 25, 'bold'), width=28, relief=RIDGE,
                         borderwidth=4, bd=6, bg='pink', activebackground='purple', activeforeground='yellow',
                         command=update)
    submibutton.place(x=480, y=550)
    cc=studenttable.focus()
    content=studenttable.item(cc)
    pp=content['values']
    if(len(pp)!=0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mval.set(pp[2])
        eval.set(pp[3])
        aval.set(pp[4])
        gval.set(pp[5])
        dval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])
    updateroot.mainloop()


def showstudent():
    strr = 'select *from studdata '
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)


def exstudent():
    ff=filedialog.asksaveasfilename()
    gg=studenttable.get_children()
    id,name,mobile,email,address,gender,dob,adddate,addtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content=studenttable.item(i)
        pp=content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),adddate.append(pp[7]),addtime.append(pp[8])
    dd=['Id','Name','Mobile','Email','Address','Gender','Dob','adddate','addtime']
    df=pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,adddate,addtime)),columns=dd)
    paths=r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notification','saved sucessfully......'.format(paths))
def exitstudent():
    res = messagebox.askyesnocancel('NOTIFICATION', 'Do you want to exit?')
    if (res == True):
        root.destroy()


##################################################################################################################################################################
def Connectdb():
    def submitdb():
        global con, mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('notification', 'Data is incorrect please try again')
            return
        try:
            strr = 'create database ani'
            mycursor.execute(strr)
            strr = 'use ani'
            mycursor.execute(strr)
            strr = 'create table studdata(id int(20),name varchar(20),mobile varchar(20),email varchar(15),address varchar(50),gender varchar(20),dob varchar(30),date varchar(50),time varchar(60))'
            mycursor.execute(strr)

            messagebox.showinfo('notification', 'you are connected t database.....', parent=dbroot)
        except:
            strr = 'use ani'
            mycursor.execute(strr)
            messagebox.showinfo('notification', 'you are connected t database.....', parent=dbroot)
        dbroot.destroy()

    dbroot: Toplevel = Toplevel()
    dbroot.grab_set()

    dbroot.config(bg='sky blue')

    hostlabel = Label(dbroot, text="Enter Host : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3,
                      width=20, anchor='w')
    hostlabel.place(x=390, y=10)
    userlabel = Label(dbroot, text="Enter User :", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=20, anchor='w')
    userlabel.place(x=390, y=90)
    passwordlabel = Label(dbroot, text="Enter Password:", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                          borderwidth=3, width=20, anchor='w')
    passwordlabel.place(x=390, y=160)

    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot, font=('roman', 30, 'bold'), bd=5, textvariable=hostval)
    hostentry.place(x=800, y=10)
    userentry = Entry(dbroot, font=('roman', 30, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=800, y=90)
    passwordentry = Entry(dbroot, font=('roman', 30, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=800, y=160)

    submitbutton = Button(dbroot, text='submit', font=('roman', 25, 'bold'), width=28, relief=RIDGE,
                          borderwidth=4, bd=6, bg='pink', activebackground='purple', activeforeground='yellow',
                          command=submitdb)
    submitbutton.place(x=500, y=230)

    dbroot.mainloop()


import random

colors = ['red', 'blue', 'green', 'black']


def IntroLabelColorTik():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(500, IntroLabelTik)


def IntroLabelTik():
    global count, text
    if (count >= len(ss)):
        count = -1
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text + ss[count]
        SliderLabel.config(text=text)
    count += 1
    SliderLabel.after(100, IntroLabelTik)


######################################################################


from tkinter import *
from tkinter import Toplevel, messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import time
import pandas

root = Tk()
root.title("student managment sysytem")
root.config(bg="light blue")

DataFrame = Frame(root, bg="gold2", relief=GROOVE, borderwidth=5)
DataFrame.place(x=200, y=80, width=550, height=650)
frontlabel = Label(DataFrame, text='*************WELCOME*************', width=30, font=('arial', 22, ' italic bold'),
                   bg='gold2')
frontlabel.pack(side=TOP, expand=True)
addbutton = Button(DataFrame, text='1.ADD STUDENT', width=25, font=('chiller', 20, 'bold'), bd=6, bg='dark orange3',
                   activebackground='blue', activeforeground='yellow', relief=RIDGE, command=addstudent)
addbutton.pack(side=TOP, expand=True)

searchbutton = Button(DataFrame, text='2. SEARCH STUDENT', width=25, font=('chiller', 20, 'bold'), bd=6,
                      bg='dark orange3', activebackground='blue', activeforeground='yellow', relief=RIDGE,
                      command=searchstudent)
searchbutton.pack(side=TOP, expand=True)

deletebutton = Button(DataFrame, text='3. DELETE STUDENT', width=25, font=('chiller', 20, 'bold'), bd=6,
                      bg='dark orange3', activebackground='blue', activeforeground='yellow', relief=RIDGE,
                      command=deletestudent)
deletebutton.pack(side=TOP, expand=True)

updatebutton = Button(DataFrame, text='4. UPADATE STUDENT', width=25, font=('chiller', 20, 'bold'), bd=6,
                      bg='dark orange3', activebackground='blue', activeforeground='yellow', relief=RIDGE,
                      command=updatestudent)
updatebutton.pack(side=TOP, expand=True)

showbutton = Button(DataFrame, text='5.SHOW ALL STUDENT', width=25, font=('chiller', 20, 'bold'), bd=6,
                    bg='dark orange3', activebackground='blue', activeforeground='yellow', relief=RIDGE,
                    command=showstudent)
showbutton.pack(side=TOP, expand=True)

exbutton = Button(DataFrame, text='6. EXPORT DATA', width=25, font=('chiller', 20, 'bold'), bd=6, bg='dark orange3',
                  activebackground='blue', activeforeground='yellow', relief=RIDGE, command=exstudent)
exbutton.pack(side=TOP, expand=True)

exitbutton = Button(DataFrame, text='7.EXIT', width=25, font=('chiller', 20, 'bold'), bd=6, bg='dark orange3',
                    activebackground='blue', activeforeground='yellow', relief=RIDGE, command=exitstudent)
exitbutton.pack(side=TOP, expand=True)

ShowDataFrame = Frame(root, bg="gold2", relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=750, y=80, width=550, height=650)
style = ttk.Style()
style.configure('Treeview.Heading', font=('chiller', 20, 'bold'), foreground='blue')
style.configure('Treeview', font=('times', 15, 'bold'), foreground='black', background='cyan')
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
studenttable = Treeview(ShowDataFrame,
                        columns=('Id', 'Name', 'Mobile no', 'Email', 'Adrees', 'gender', 'd.o.b', 'date', 'time'),
                        yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id', text='Id')
studenttable.heading('Name', text='Name')
studenttable.heading('Mobile no', text='Mobile no')
studenttable.heading('Email', text='Email')
studenttable.heading('Adrees', text='Adrees')
studenttable.heading('gender', text='gender')
studenttable.heading('d.o.b', text='d.o.b')
studenttable.heading('date', text='date')
studenttable.heading('time', text='time')
studenttable['show'] = 'headings'
studenttable.column('Id', width=150)
studenttable.column('Name', width=150)
studenttable.column('Mobile no', width=150)
studenttable.column('Email', width=150)
studenttable.column('Adrees', width=150)
studenttable.column('gender', width=150)
studenttable.column('d.o.b', width=150)
studenttable.column('date', width=150)
studenttable.column('time', width=150)
studenttable.pack(fill=BOTH, expand=1)

ss = "Welcome to student managment sysytem"
count = 0
text = ''
SliderLabel = Label(root, text=ss, font=('chiller', 40, 'italic bold'), relief=RIDGE, borderwidth=4, width=35,
                    bg='cyan')
SliderLabel.place(x=390, y=0)

IntroLabelTik()

IntroLabelColorTik()

connectbutton = Button(root, text='connect to database', width=20, font=('chiller', 25, 'italic bold'), relief=RIDGE,
                       borderwidth=4, bd=6, bg='green', activebackground='red', activeforeground='yellow',
                       command=Connectdb)
connectbutton.place(x=610, y=730)

root.mainloop()
