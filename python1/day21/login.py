from tkinter import *
a=Tk()
a.title("Scient-Login")
lb1=Label(a,text="Student-Login",font=("Arial Bold",15))
lb1.grid(column=0,row=0)
lb2=Label(a,text="username")
lb2.grid(column=0,row=1)
lb3=Label(a,text="password")
lb3.grid(column=0,row=2)
e1=Entry(a,width=15)
e1.grid(column=1,row=1)
e2=Entry(a,width=15,show="***")
e2.grid(column=1,row=2)
def scient():
    un=e1.gettext()
    ps=e2.gettext()
    if un=="admin" and ps=="1234":
        messagebox.showinfo("","done!")
    else:
        messagebox.showerror("","Invalid")
b=Button(a,text="login")
b.grid(column=1,row=3)
a.mainloop()
