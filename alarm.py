from tkinter import *
import datetime
import time
import winsound
from playsound import playsound
'''
Tkinter: Python offers multiple choices for developing a GUI (Graphical User Interface). Out of all the GUI strategies, tkinter is that the most ordinarily used technique. It’s a customary Python interface to the Tk GUI toolkit shipped with Python.

Winsound: The winsound module provides access to the essential sound-playing machinery provided by Windows platforms. It includes functions and a number of other constants. Beep the PC’s speaker.

The playsound module contains only a single function named playsound().
It requires one argument: the path to the file with the sound we have to play. It can be a local file, or a URL.
There’s an optional second argument, block, which is set to True by default. We can set it to False for making the function run asynchronously.
It works with both WAV and MP3 files.
'''

def alarm(set_alarm):
    alarm_rang = False
    while True:
        time.sleep(1)#wait for 1 sec
        #print(set_alarm)
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")#get current date
        current_time = datetime.datetime.now().strftime("%H:%M:%S")#get current time
        if(not(alarm_rang)):
            print("NOW : ",current_date,current_time,"\t\tALARM at ",set_alarm)
        else:
            print("NOW : ",current_date,current_time)
        if current_time == set_alarm :#if both the time are exact
            print("Time to Wake Up")
            alarm_rang = True
            #playsound("/grabbybow.mp3")#not working
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            #winsound.PlaySound("Music.wav",winsound.SND_ASYNC)
            return


#stores the time of alarm in string format and passes it to the alarm function
def get_alarm_time(hour, minute,second):
    h,m,s = hour.get(),minute.get(),second.get()
    if (0 <= int(h) <= 24 and 0 <= int(m) <= 60 and int(s) in range(0,61)):
        if(len(h)) == 1 : h = '0'+h
        if(len(m)) == 1 : m = '0'+m
        if(len(s)) == 1 : s = '0'+s
        set_alarm = f"{h}:{m}:{s}"
        #set_alarm = f"{hour.get()}:{minute.get()}:{second.get()}"
        alarm(set_alarm)
        return
    else:
        print("\n\nInvalid time....Try again..........")

'''
The logic of our alarm clock has been implemented below.

Now the GUI part of the alarm clock is to be implemented using tkinter
'''
def show_clock():
    window = Tk()#creates a default window 
    window.title("⏰The Pleasant Alarm⏰")#naming the window
    window.geometry("400x160")#length x height of window
    window.config(bg="#33FF91")
    
    #window.resizable(width=False,height=False)#prevent user to resize
    time_format=Label(window, text= "Remember to set time in 24 hour format!", fg="white",bg="#922B21",font=("Arial",15)).place(x=20,y=120)
    addTime = Label(window,text = "Hour\tMin\tSec",font=60,fg="white",bg="black").place(x = 210)
    setYourAlarm = Label(window,text = "Set Time for Alarm: ",fg="white",bg="#922B21",relief = "solid",font=("Helevetica",15,"bold")).place(x=10, y=40)
    '''
    .place(x,y) determine the cordinated where the text is to placed
    '''
    hour = StringVar()
    minute = StringVar()
    second = StringVar()
     
    hourTime= Entry(window,textvariable = hour,bg = "#48C9B0",width = 4,font=(20)).place(x=210,y=40)
    minTime= Entry(window,textvariable = minute,bg = "#48C9B0",width = 4,font=(20)).place(x=270,y=40)
    secTime = Entry(window,textvariable = second,bg = "#48C9B0",width = 4,font=(20)).place(x=330,y=40)
 
    submit = Button(window,text = "Set Your Alarm",fg="Black",bg="#D4AC0D",width = 15,command = lambda : get_alarm_time(hour, minute,second),font=(20)).place(x =100,y=80)
    
    window.mainloop()
    window.destroy();
    show_clock();

show_clock()

