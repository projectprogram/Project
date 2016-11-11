# Import modules
import pymysql
from time import strftime
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText

# Sending the message
def bericht():
    # Retrieve information from Entry
    msgentry = entry.get("1.0", 'end-1c')
    # Failsafe is entry < 140 characters
    if len(msgentry) > 140:
        print('Bericht mag niet meer dan 140 karakters bevatten')
    # If message < 140 characters
    else:
        # Timestamp
        datetime = strftime("%Y-%m-%d %H:%M:%S")
        # Open database connection
        db = pymysql.connect(host='localhost', port=3306, user='ruben', passwd='walnoot', db='py')
        # Prepare a cursor object using cursor() method
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

        # Disconnect from server
        db.close()

# GUI - Buildup
root = Tk()
root.title("Uw Bericht")
root.state('zoomed')

# GUI - Set Background Image
bgimage = PhotoImage(file="BackgroundNS.png")
bglabel = Label(root, image=bgimage)
bglabel.place(x=-0.5, y=-0.5, relwidth=1, relheight=1)

# GUI - Create frame to put widgets into
widgets = Frame(root)
widgets.pack(fill="none", expand=True)

# GUI - Create Input Box
entrytext = StringVar()
entry = ScrolledText(widgets, bg = "lightgray")
entry.pack()

# GUI - Create Button + Execute
buttontext = StringVar()
buttontext.set("Verstuur")
Button(widgets, textvariable=buttontext, command=bericht).pack(anchor=W)

# GUI - Run Mainloop TKInter
root.mainloop()
