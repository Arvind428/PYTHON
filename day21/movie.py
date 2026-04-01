from tkinter import *
from tkinter import messagebox

a=Tk()
lb1=Label(a,text="Book My Show",font=("arail bold",20))
lb1.grid(column=1,row=0)
lb2=Label(a,text="Name",font=("arail bold",20))
lb2.grid(column=0,row=1)
lb3=Label(a,text="Movie",font=("arail bold",20))
lb3.grid(column=0,row=2)
lb4=Label(a,text="Tickets",font=("arail bold",20))
lb4.grid(column=0,row=3)
e1=Entry(a,width=15)
e1.grid(column=1,row=1)
option=["Peddi","KGF","RRR",]
v1=StringVar()
v1.set("select")
d1=OptionMenu(a,v1,*option)
d1.grid(column=1,row=2)
tickets=[1,2,3,4,5,6,7,8,9,10]
v2=IntVar()
v2.set("select")
d2=OptionMenu(a,v2,*tickets)
d2.grid(column=1,row=3)
def mt():
    t=int(v2.get())
    sm=v1.get()
    if sm=="Peddi":
        total=100*t
        messagebox.showinfo("","Hello"+e1.get()+"\n Your Total:"+str(total))
    elif sm=="KGF":
        total=250*t
        messagebox.showinfo("","Hello"+e1.get()+"\n Your Total:"+str(total))
    elif sm=="RRR":
        total=400*t
        messagebox.showinfo("","Hello"+e1.get()+"\n Your Total:"+str(total))
    else:
        messagebox.showerror("","Invalid")
b=Button(a,text="Book",command=mt)
b.grid(column=1,row=4)
a.mainloop()
