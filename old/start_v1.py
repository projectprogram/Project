#Import modules
import pymysql
from time import strftime
from tkinter import *
from tkinter.ttk import *

#Sending the message
def bericht():
    #Retrieve information from Entry
    msgentry = entry.get()
    #Failsafe is entry < 140 characters
    if len(msgentry) > 140:
        print('Bericht mag maximaal 140 karakters bevatten')
    #If message < 140 char
    else:
        #Timestamp
        datetime = strftime("%Y-%m-%d %H:%M:%S")
        # Open database connection
        db = pymysql.connect(host='localhost', port=3306, user='ruben', passwd='walnoot', db='py')
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        try:
            v = (msgentry, datetime)
            # Execute the SQL command
            cursor.execute("INSERT INTO py_table(`message`,`datetime`) VALUES (%s,%s)", v)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        # disconnect from server
        db.close()

# GUI Buildup
root = Tk()
root.title("Uw Feedback")
root.state('zoomed')

#label GUI
label = Label(root,text='Enter Message:')
label.grid(row=0,column=0)
label.pack()

#Entry GUI
entrytext = StringVar()
entry = Entry(root, textvariable=entrytext)
entry.pack()

# Button GUI
buttontext = StringVar()
buttontext.set("Verstuur")

#Button execute
Button(root, textvariable=buttontext, command=bericht).pack()

#Run the mainloop TKInter
root.mainloop()
