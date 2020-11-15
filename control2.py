from tkinter import *
import datetime
def control():
    file=open("usom.txt", "r")
    content=file.read()
    file.close()
    ip=entry1.get()
    today=datetime.datetime.now()
    if str (ip) in content:
        file=open("log.txt","a")
        slogan=str(ip)+"malware\nDate:"+str(today)+"\n"
        file.write(slogan)
        file.close()
        v.set("IP is malicious")
    else:
        file=open("log.txt","a")
        slogan= slogan=str(ip)+"is not malware\nDate:"+str(today)+"\n"
        file.write(slogan)
        file.close()
          v.set("IP is not malicious")
myApp=Tk()
myApp.title("Malicious IP Control App")
B=Button(myApp,text="Control",command=control)
B.place(x=80,y=80)
B.pack()
label_1=Label(top,text="Please write an IP Addres in order to control:")
label_1=Place(x=80,y=120)
label_1.pack()
entry_1=Entry(myApp)
entry_1.place(x=80,y=140)
entry_1.pack()
v=StringVar()
entry_2=Entry(top,textvariable=v)
entry_2.place(x=80,y=160)
entry_2.pack()