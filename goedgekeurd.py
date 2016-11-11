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
    sql = "SELECT * FROM py_table WHERE status = %s ORDER BY id DESC LIMIT 5" % (x)
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

            # Increment Frame
            ii += 1
    except:
        print("Error: unable to fecth data")
    # disconnect from server
    db.close()

#Run the approved_window function with param 0 to display all pending messages
approved_window(1)
#Main TkInter Execute
win.mainloop()
