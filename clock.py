# Import Required Library
from tkinter import *
import datetime
import time
import tkinter
from token import OP
import winsound
from threading import *
from anyio import current_time
from playsound import playsound
import os

root = Tk()

root.geometry("400x200")

def Threading():
    t1=Thread(target=alarm)
    t1.start()

def Threading2():
    t2 = Thread(target=stop)
    t2.start()



def alarm():
    while True:
        set_alarm = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        if current_time == set_alarm:
           print("wake up wake up")
           playsound('audio.mp3')

Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root,text="Set Alarm", font=("Helvetica 20 bold")).pack()
#Label(root,text="Stop", font=("Helvetica 20 bold")).pack(pady=20)

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

b1 = tkinter.Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading)
b1.pack(side = tkinter.BOTTOM)

b2 = tkinter.Button(root,text="Stop",font=("Helvetica 15"),command=Threading2)
b2.pack(side = tkinter.TOP)
def stop():
    os._exit(os.X_OK)



root.mainloop()



