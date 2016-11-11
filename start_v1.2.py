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
    if len(msgentry) == 0:
        # GUI - Set text if equal to 0 characters
        errorlabel.config(text=" U kunt geen lege berichten versturen.", foreground="Red")
    elif len(msgentry) > 140:
        # GUI - Set text if more than 140 characters
        errorlabel.config(text=" Uw bericht kan niet langer zijn dan 140 karakters.", foreground="Red")
    else:
        print(entry.get("1.0", 'end-1c'))
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
        # GUI - Set text to succes
        errorlabel.config(text=" Succesvol verstuurd.", foreground="Green")
        # Disconnect from server
        db.close()

# GUI - Buildup
root = Tk()
root.title("NS - Berichtenapp")
root.state('zoomed')

# GUI - Get screensize
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# GUI - Set Background Image
bgimage = PhotoImage(file="BackgroundNS.png")
bglabel = Label(root, image=bgimage)
bglabel.place(x=-0.5, y=-0.5, relwidth=1, relheight=1)

# GUI - Create frame to put widgets into
widgetsmain = Frame(root)
widgetsmain.place(x=(640), y=(340))

# GUI - Create Input Box
entrytext = StringVar()
entry = ScrolledText(widgetsmain, bg ="lightgray")
entry.pack()

# GUI - Create frame for Button, >140 Char text and counter
widgetssub = Frame(widgetsmain)
widgetssub.pack(anchor=W)

# GUI - Create empty label for messages to be put in
errorlabel = Label(widgetssub, text="")
errorlabel.pack(side=RIGHT)

# GUI - Create Button + Execute
buttontext = StringVar()
buttontext.set("Verstuur")
Button(widgetssub, textvariable=buttontext, command=bericht).pack(side=LEFT)

# GUI - Run Mainloop TKInter
root.mainloop()
