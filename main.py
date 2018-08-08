from tkinter import ttk
from tkinter import *
import sqlite3
import db_comm as db

conn = sqlite3.connect('app_manager.sqlite')
c = conn.cursor()


def destroy_window(root, name, email):

    db.register(name, email)
    root.destroy()


def newEntry():

    root = Tk()
    root.geometry('500x800')

    lname = Label(root, text='Your name')
    name = Entry(root)

    lp = Label(root, text='Position applied for')
    p = Entry(root)

    lc = Label(root, text='Company applied to')
    c = Entry(root)

    lr = Label(root, text='Resume submitted (filename only)')
    r = Entry(root)

    lcl = Label(root, text='Cover letter submitted')
    cl = Text(root, height=30, width=50)

    ln = Label(root, text='Notes about the application')
    n = Entry(root)

    ld = Label(root, text='Date Applied')
    d = Entry(root)

    b = Button(root, text='Submit', command=lambda: db.add_job(p.get(), d.get(), c.get(), r.get(), cl.get("1.0", END), n.get(), name.get()))
    e = Button(root, text='Exit', command=lambda: root.destroy())

    lname.pack(side=TOP)
    name.pack(side=TOP)
    lp.pack(side=TOP)
    p.pack(side=TOP)
    ld.pack(side=TOP)
    d.pack(side=TOP)
    lc.pack(side=TOP)
    c.pack(side=TOP)
    lr.pack(side=TOP)
    r.pack(side=TOP)
    lcl.pack(side=TOP)
    cl.pack(side=TOP)
    ln.pack(side=TOP)
    n.pack(side=TOP)
    b.pack(side=TOP)
    e.pack(side=TOP)

    root.mainloop()


def listWindow(name):

    root = Tk()
    root.geometry('400x500')
    root.title('Job Application Manager')

    def onDouble(id):

        root = Tk()
        root.geometry('400x500')

        x = db.retrieve_job(id)
        listypants = ['Position: ', '\nDate Applied: ', '\nCompany: ', '\nResume (file): ', '\nCover Letter: ', '\nNotes: ']

        for elements, items in zip(x[0:-2], listypants):

            labz = Label(root, text=items, bd=3)
            text = Label(root, text=elements, bd=3)
            labz.pack()
            text.pack()

        butt = Button(root, text='Delete post', command=lambda id=id: db.del_entry(id))
        butt.pack()

        root.mainloop()

    xy = db.retrieve_jobs(name)

    for x in xy:

        b = Radiobutton(root, text=x[0]+' at '+x[2], value=x[7], indicatoron=0, command= lambda id=x[7]: onDouble(id))
        b.pack()

    root.mainloop()


def intro():

    root = Tk()
    root.geometry('500x400')
    root.title('Job Application Manager')
    T = Label(root, text='Welcome to your personal Application Manager')

    T.pack(side=TOP)

    lname = Label(root, text="Enter your name")
    name = Entry(root)
    lname.pack(side=TOP)
    name.pack(side=TOP)

    lemail = Label(root, text="Enter your email")
    email = Entry(root)
    lemail.pack(side=TOP)
    email.pack(side=TOP)

    submit = Button(root, text='Submit', command=lambda: destroy_window(root, name.get(), email.get()))
    submit.pack()

    root.mainloop()


def main():

    root = Tk()
    root.geometry('500x400')
    root.title('Job Application Manager')

    b = Button(root,text='Settings', )
    b2 = Button(root, text='New Entry', command=newEntry)

    nl = Label(root, text='Find results for:')
    n = Entry(root)
    b3 = Button(root, text='Check', command=lambda: listWindow(n.get()))

    nl.place(x=200, y=50)
    n.insert(0, 'Your name')
    n.place(x=200, y=80)
    b3.place(x=300, y=80)

    b.place(x=0, y=0)
    b2.place(x=80, y=0)
    root.mainloop()


if __name__ == '__main__':
    # 'no' gives desired result here
    x = db.check_table('no')
    if not x:
        db.create_user_table()
        intro()
    else:
        # y = login()
        db.create_job_table()
        main()



