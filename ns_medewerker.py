import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
from TwitterAPI import TwitterAPI

#TKInter Build
win = Tk()
win.title("Goedkeuren/Afkeuren Programma")
win.geometry('800x800-5+40')
content = ttk.Frame(win)
#Menu option failsafe
win.option_add('*tearOff', FALSE)
#Global button defining
buttons = {}

def approved_window(x):
    x = x
    iiii = 1
    global frame_int
    framez = Frame(win)
    framez.pack(fill=X)

    # Open database connection
    db = pymysql.connect(host='localhost', port=3306, user='ruben', passwd='walnoot', db='py')
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM py_table WHERE status = %s" % (x)
    if x == 3:
        sql = "SELECT * FROM py_table WHERE status = 0 or 1 or 2"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        ii = 2
        iii = 1

        global buttons
        for row in results:
            # Data retrieval
            id = row[0]
            message = row[1]
            datetime = row[2]
            status = row[3]
            # Now print fetched result
            print("id=%d,message=%s,datetime=%s" % \
                  (id, message, datetime))
            # Now add them to my tables
            lbl = 'lbl' + str(iii)
            btn = 'btn' + str(iiii)

            frame_int = Frame(win)
            frame_int.pack(fill=X, pady=10, padx=10)

            lbl = Label(frame_int, text="Message")
            lbl.grid(row=0, column=0, sticky=W)
            iii += 1
            lbl = 'lbl' + str(iii)

            lbl = Label(frame_int, text=id)
            lbl.grid(row=1, column=0, sticky=W, )
            iii += 1
            lbl = 'lbl' + str(iii)

            lbl = Label(frame_int, text=datetime)
            lbl.grid(row=2, column=0, sticky=W)
            iii += 1
            lbl = 'lbl' + str(iii)

            lbl = Label(frame_int, text=message, width=90)
            lbl.grid(row=0, column=1, sticky=W)
            iii += 1
            lbl = 'lbl' + str(iii)
            print (x)
            if status == 0:
                btn = Button(frame_int, text="Goedkeuren")
                buttons[btn] = id
                btn.bind("<Button-1>", goedkeuren)
                btn.grid(row=0, column=2, sticky=W)
                iiii += 1
                btn = 'btn' + str(iiii)

                btn = Button(frame_int, text="Afkeuren")
                buttons[btn] = id
                btn.bind("<Button-1>", afkeuren)
                btn.grid(row=1, column=2, sticky=W)
                iiii += 1
                btn = 'btn' + str(iiii)

            # Increment Frame
            ii += 1
    except:
        print("Error: unable to fecth data")
    # disconnect from server
    db.close()

# def menutop():
#     #Frame
#     frame1 = Frame(win)
#     frame1.pack(fill=X)
#
#     #Button 'All'
#     lbl = Button(frame1, text="All", command= lambda: approved_window(3))
#     lbl.grid(row=0, column=0, sticky=W)
#
#     #Button 'Pending'
#     lbl = Button(frame1, text="Pending", command= lambda: approved_window(0))
#     lbl.grid(row=0, column=1, sticky=W)
#
#     #Button 'Approved'
#     lbl2 = Button(frame1, text="Approved", command= lambda: approved_window(1))
#     lbl2.grid(row=0, column=2, sticky=W)
#
#     #Button 'Denied'
#     lbl3 = Button(frame1, text="Denied", command= lambda: approved_window(2))
#     lbl3.grid(row=0, column=3, sticky=W)

def goedkeuren( event ):

    global buttons
    idd = buttons[ event.widget ]
    # Open database connection
    db = pymysql.connect(host='localhost', port=3306, user='ruben', passwd='walnoot', db='py')
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "UPDATE py_table SET status = 1 WHERE id = '%d'" % (idd)
    sql2 = "SELECT * FROM py_table WHERE id = '%d'" % (idd)
    try:
        # Execute the SQL command
        cursor.execute(sql2)
        results = cursor.fetchall()
        for row in results:
            res = row[1]
        # Fetch all the rows in a list of lists.
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    api = TwitterAPI('neb8PfrfIGVejRn6ZiN8Vain0', 'EWXVvzXn0DNQeycLaUMobjk2eRssqOlY8LIkJnp5x4mGFG0fUf', '792390105138884608-4DVUjuP5sZX70wrRWjiDjohQRFQ9lrB', 'Y6GctTJEzT6c4Y48gGI8m2s6FGqFK2STjdu6BjVMGVVum')
    r = api.request('statuses/update', {'status':res})
    messagebox.showinfo('Bericht verstuurd', 'Uw bericht is succesvol verstuurd.')

def afkeuren(event):
    global buttons
    idd = buttons[ event.widget ]
    print(idd)
    # Open database connection
    db = pymysql.connect(host='localhost', port=3306, user='ruben', passwd='walnoot', db='py')
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql = "UPDATE py_table SET status = 2 WHERE id = '%d'" % (idd)
    try:
        print('y')
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        db.commit()
        print('y')
    except:
        db.rollback()

#Building the main menu buttons
# menutop()
#Run the approved_window function with param 0 to display all pending messages
approved_window(0)
#Main TkInter Execute
win.mainloop()
