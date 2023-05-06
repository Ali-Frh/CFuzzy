import os
import time,sys
import threading
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import messagebox
import subprocess
import stuff.funcs as funcs
import webbrowser

def doinshit():
    print("called")
    global doing
    global logging
    global server
    global RFrag
    toggle["state"] = "disabled"
    #time.sleep(1)
    if doing == True:
        toggle["text"] = "Start Server"
        server.terminate()
        doing = False
    else:
        doing = True
        server = subprocess.Popen(["python3","stuff/launcher.py",f"{svport.get()}",
        f"{cfip.get()}",
        f"{cfport.get()}",
        f"{l_fragment.get()}",
        f"{fragment_sleep.get()}",
        f"{my_socket_timeout.get()}",
        f"{first_time_sleep.get()}",
        f"{accept_time_sleep.get()}",
        f"{RFrag.get()}"])
        print("RF",RFrag.get())

## Saving Config
        global settings
        settings = {
            "svport":           f"{svport.get()}",
            "cfip":             f"{cfip.get()}",
            "cfport":           f"{cfport.get()}",
            "l_fragment":       f"{l_fragment.get()}",
            "fragment_sleep":   f"{fragment_sleep.get()}",
            "my_socket_timeout":f"{my_socket_timeout.get()}",
            "first_time_sleep": f"{first_time_sleep.get()}",
            "accept_time_sleep":f"{accept_time_sleep.get()}",
            "randfrag":         f"{RFrag.get()}"
        }

        funcs.save_settings(settings)




        toggle["text"] = "Stop Server"

    toggle["state"] = "normal"

server = False

# settings = {}
settings = funcs.load_settings()

# print(settings)

doing = False
root = Tk()
RFrag = BooleanVar()
RFrag.set(settings["randfrag"])
root.title("CFuzzy v1.0")
root.geometry("550x520")
#root['background']='#e4e4e4'
#root.configure(bg='blue')

Label(text="CFuzzy Server v1.1",font=('Times 20'),height=4).pack(side=TOP)


Label(text="Basic Configuration",font=('Times 15'),height=0).pack(side=TOP)

#row 1
row_1 = Frame(root)


svportlb = Label(row_1,text="Server Port:  ", height=1)
svportlb.grid(row=1,column=1)
svport = Entry(row_1,width=7)
svport.insert(INSERT, settings["svport"])
svport.grid(row=1,column=2)

#cfip
cflabel = Label(row_1,text="   CF IP:  ")
cflabel.grid(row=1,column=3)
cfip = Entry(row_1,width=15)
cfip.insert(INSERT, settings["cfip"])
cfip.grid(row=1,column=4)

#cfip
cfportlb = Label(row_1,text="   CF Port:  ",height=4)
cfportlb.grid(row=1,column=5)
cfport = Entry(row_1,width=7)
cfport.insert(INSERT, settings["cfport"])
cfport.grid(row=1,column=6)

row_1.pack(side=TOP)

Label(text="Advanced Configuration",font=('Times 15'),height=0).pack(side=TOP)
Label(text="Dont touch it if you dont know what you doing!",font=('Times 10'),height=2).pack(side=TOP)


row_2 = Frame(root)

l_fragmentlb = Label(row_2,text="L_Fragment:  ")
l_fragmentlb.grid(row=1,column=1)
l_fragment = Entry(row_2,width=4)
l_fragment.insert(INSERT, settings["l_fragment"])
l_fragment.grid(row=1,column=2)

fragment_sleep_lb = Label(row_2,text="   fragment_sleep:  ")
fragment_sleep_lb.grid(row=1,column=3)
fragment_sleep = Entry(row_2,width=4)
fragment_sleep.insert(INSERT, settings["fragment_sleep"])
fragment_sleep.grid(row=1,column=4)

my_socket_timeout_lb = Label(row_2,text="   my_socket_timeout:  ")
my_socket_timeout_lb.grid(row=1,column=5)
my_socket_timeout = Entry(row_2,width=4)
my_socket_timeout.insert(INSERT, settings["my_socket_timeout"])
my_socket_timeout.grid(row=1,column=6)

first_time_sleeplb = Label(row_2,text="first_time_sleep:  ",height=2)
first_time_sleeplb.grid(row=2,column=1)
first_time_sleep = Entry(row_2,width=4)
first_time_sleep.insert(INSERT, settings["first_time_sleep"])
first_time_sleep.grid(row=2,column=2)

accept_time_sleeplb = Label(row_2,text="   accept_time_sleep:  ",height=2)
accept_time_sleeplb.grid(row=2,column=3)
accept_time_sleep = Entry(row_2,width=4)
accept_time_sleep.insert(INSERT, settings["accept_time_sleep"])
accept_time_sleep.grid(row=2,column=4)

randfraglb = Label(row_2,text="   Random Fragments:  ",height=2)
randfraglb.grid(row=2,column = 5)
randfrag = Checkbutton(row_2,variable=RFrag, onvalue=True, offvalue=False)
randfrag.grid(row=2,column = 6)

row_2.pack(side=TOP)

spacer1 = Label(text="",height=2)
spacer1.pack(side = TOP)

ControlFrame = Frame(root)


toggle = Button(ControlFrame, text="Start Server", width=10, height=2, font=('Times 15'), command=doinshit)
toggle.pack(side=TOP)

ControlFrame.pack(side=TOP)


# Link to Repo for further issues and stuff.

def callback(url):
   webbrowser.open_new_tab(url)


link = Label(root, text="Project's Repo: https://github.com/Ali-Frh/CFuzzy",
font=('Helveticabold', 10), fg="blue", cursor="hand2", height="2")
link.pack(side=BOTTOM)
link.bind("<Button-1>", lambda e:
callback("https://github.com/Ali-Frh/CFuzzy"))


root.mainloop()
