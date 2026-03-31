from tkinter import *
from tkinter import messagebox
import tkinter as tk
a=Tk()
a.config(bg="red")
lb1=Label(a,text="TICKET BOOKING",font="Arial 20 bold",bg="red")
lb1.grid(row=0,column=1)
lb2=Label(a,text="FROM STATION",font="Arial 20 bold",bg="red")
lb2.grid(row=1,column=0)
lb3=Label(a,text="TO STATION",font="Arial 20 bold",bg="red")
lb3.grid(row=2,column=0)
lb4=Label(a,text="TICKETS",font="Arial 20 bold",bg="red")
lb4.grid(row=3,column=0)
fs=[ "Miyapur", "JNTU College", "KPHB Colony", "Kukatpally", "Balanagar",
    "Moosapet", "Bharat Nagar", "Erragadda", "ESI Hospital", "SR Nagar",
    "Ameerpet", "Punjagutta", "Irrum Manzil", "Khairatabad", "Lakdi-ka-pul",
]
click=StringVar()
click.set("FROM Station")
d1=OptionMenu(a,click,*fs)
d1.grid(row=1,column=1)
ts=[ "Assembly", "Nampally", "Gandhi Bhavan", "Osmania Medical College",
    "MG Bus Station", "Malakpet", "New Market", "Musarambagh", "Dilsukhnagar",
    "Chaitanyapuri", "Victoria Memorial", "LB Nagar"]
click2=StringVar()
click2.set("select")
d2=OptionMenu(a,click2,*ts )
d2.grid(row=2,column=1)
tk=[1,2,3,4,5,6,7,8,9,10]
click3=StringVar()
click3.set("select")
d3=OptionMenu(a,click3,*tk)
d3.grid(row=3,column=1)
lb5=Label(a,text="do u need cab",font="Arial 20 bold",bg="red")
lb5.grid(row=4,column=0)
def yes():
    lb6=Label(a,text="cab destination",font="Arial 20 bold",bg="red")
    lb6.grid(row=5,column=0)
    e1=Entry(a,width=20)
    e1.grid(row=5,column=1)
    def book():
        s1=click.get()
        s2=click2.get()
        t=int(click3.get())
        mbill=t*20  
        cbill=150
        total=mbill+cbill
        messagebox.showinfo("","metro from "+s1+" to "+s2+" for "+str(t)+" passengers is "+str(mbill)+"\n cab fare is "+str(cbill)+"\n total bill is "+str(total))
    b3=Button(a,text="book", command=book)
    
    b3.grid(row=6,column=1)

b1=Button(a,text="yes",command=yes)
b1.grid(row=4,column=1)
def no():
    s1=click.get()
    s2=click2.get()
    t=int(click3.get())
    mbill=t*20  
    messagebox.showinfo("","metro from "+s1+" to "+s2+" for "+str(t)+" passengers is "+str(mbill))
    
b2=Button(a,text="no", command=no)
b2.grid(row=4,column=2)
a.mainloop()
