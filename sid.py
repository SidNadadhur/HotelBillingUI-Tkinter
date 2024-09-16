from tkinter import *
from array import *
from tkinter import messagebox
w=Tk()
ca=array('l',[100,120,150,170,200,300])
ba=array('i',[0,0,0,0,0,0])
w.title("python project")
l1=Label(w,text="The Continental",bg="RED",font=("Algerian",23)).place(x=500,y=10)      
def bapan():
    l4=Label(w,text="veg Manchuria      100/-",font=("Calibri",15)).place(x=10,y=270)
    l5=Label(w,text="paneer Tikka         120/-",font=("Calibri",15)).place(x=10,y=310)
    l6=Label(w,text="veg biryani             200/-",font=("Calibri",15)).place(x=10,y=350)
    l22=Label(w,text="                                                                 ").place(x=10,y=395)
    l23=Label(w,text="                                                                 ").place(x=10,y=435)
    l24=Label(w,text="                                                                 ").place(x=10,y=475)
def notbapan():
    l25=Label(w,text="                                                                 ").place(x=10,y=275)
    l26=Label(w,text="                                                                 ").place(x=10,y=315)
    l27=Label(w,text="                                                                 ").place(x=10,y=355)
    l7=Label(w,text="chicken 65           150/-",font=("Calibri",15)).place(x=10,y=390)
    l8=Label(w,text="chilli chicken       170/-",font=("Calibri",15)).place(x=10,y=430)
    l9=Label(w,text="chicken biryani    300/-",font=("Calibri",15)).place(x=10,y=470)
def dongabapan():
    l10=Label(w,text="veg Manchuria      100/-",font=("Calibri",15)).place(x=10,y=270)
    l11=Label(w,text="paneer Tikka         120/-",font=("Calibri",15)).place(x=10,y=310)
    l12=Label(w,text="veg biryani            200/-",font=("Calibri",15)).place(x=10,y=350)
    l13=Label(w,text="chicken 65             150/-",font=("Calibri",15)).place(x=10,y=390)
    l14=Label(w,text="chilli chicken         170/-",font=("Calibri",15)).place(x=10,y=430)
    l15=Label(w,text="chicken biryani      300/-",font=("Calibri",15)).place(x=10,y=470)
def roll():
        global sp_no
        global p
        global m
        if(sp_no>1):
              messagebox.showerror("Error","You can roll only once")
        else:
              import random
              r23=random.randint(1,6)
              l43=Label(m,text=r23,font=100).place(x=50,y=100)
              if(r23%2==0):
                    l44=Label(m,text="Ah! Bad Luck",font=("Calibri",16)).place(x=150,y=95)
                    l46=Label(m,text="Your final bill is:"+str(p)).place(x=70,y=250)
                    sp_no=2
              else:
                    ub=Label(m,text="upgraded bill",font=("Calibri",21)).place(x=70,y=250)
                    l45=Label(m,text=p-(25*p)/100,font=150).place(x=280,y=260)
                    sp_no=2
def luck():
        global p
        global m
        m=Tk()
        m.title("wait and watch")
        l40=Label(m,text="roll the dice and get 25% off if the number is odd",font=("Calibri",15)).place(x=30,y=50)
        b4=Button(m,text="Roll",height=1,width=4,font=("Calibri",18),bg="green",command=roll).place(x=500,y=50)
def button():
    global p
    s=Tk()
    s.title("Bill")
    l16=Label(s,text="Item",font=("Calibri",15)).place(x=10,y=10)
    l17=Label(s,text="price",font=("Calibri",15)).place(x=190,y=10)
    l18=Label(s,text="quantity",font=("Calibri",15)).place(x=360,y=10)
    l19=Label(s,text="q*p",font=("Calibri",15)).place(x=570,y=10)
    if(e1.get()!=""):
        l22=Label(s,text="veg manchuria",font=("Calibri",15)).place(x=10,y=50)
        l28=Label(s,text=ca[0]).place(x=200,y=60)
        l29=Label(s,text=int(e1.get())).place(x=400,y=60)
        ba1=Label(s,text=(ca[0]*int(e1.get()))).place(x=585,y=50)
        ba[0]=ca[0]*int(e1.get())
    if(e2.get()!=""):
        l23=Label(s,text="paneer Tikka",font=("Calibri",15)).place(x=10,y=100)
        l30=Label(s,text=ca[1]).place(x=200,y=100)
        l31=Label(s,text=int(e2.get())).place(x=400,y=100)
        ba2=Label(s,text=(ca[1]*int(e2.get()))).place(x=585,y=100)
        ba[1]=ca[1]*int(e2.get())
    if(e3.get()!=""):
        l24=Label(s,text="veg Biryani",font=("Calibri",15)).place(x=10,y=150)
        l32=Label(s,text=ca[2]).place(x=200,y=150)
        l33=Label(s,text=int(e3.get())).place(x=400,y=150)
        ba3=Label(s,text=(ca[2]*int(e3.get()))).place(x=585,y=150)
        ba[2]=ca[2]*int(e3.get())
    if(e4.get()!=""):
        l25=Label(s,text="chicken 65",font=("Calibri",15)).place(x=10,y=200)
        l34=Label(s,text=ca[3]).place(x=200,y=200)
        l35=Label(s,text=int(e4.get())).place(x=400,y=200)
        ba4=Label(s,text=(ca[3]*int(e4.get()))).place(x=585,y=200)
        ba[3]=ca[3]*int(e4.get())
    if(e5.get()!=""):
        l26=Label(s,text="chilli chicken",font=("Calibri",15)).place(x=10,y=250)
        l36=Label(s,text=ca[4]).place(x=200,y=250)
        l37=Label(s,text=int(e5.get())).place(x=400,y=250)
        ba5=Label(s,text=(ca[4]*int(e5.get()))).place(x=585,y=250)
        ba[4]=ca[4]*int(e5.get())
    if(e6.get()!=""):
        l27=Label(s,text="Chicken Biryani",font=("Calibri",15)).place(x=10,y=300)
        l38=Label(s,text=ca[5]).place(x=200,y=300)
        l39=Label(s,text=int(e6.get())).place(x=400,y=300)
        ba6=Label(s,text=(ca[5]*int(e6.get()))).place(x=585,y=300)
        ba[5]=ca[5]*int(e6.get())
    p=ba[0]+ba[1]+ba[2]+ba[3]+ba[4]+ba[5]
    pay=Label(s,text="Your bill",font=("Calibri",20)).place(x=350,y=400)
    bill=Label(s,text=p,font=("Calibri",22)).place(x=550,y=400)
    #w=Tk()
    b2=Button(s,text="want to try your luck?",height=1,width=30,bg="Yellow",command=luck).place(x=400,y=550)
r1=Radiobutton(w,text="bapan",value=1,font=("Calibri",14),command=bapan).place(x=350,y=100)
r2=Radiobutton(w,text="not bapan",value=2,font=("Calibri",14),command=notbapan).place(x=450,y=100)
r3=Radiobutton(w,text="donga bapan",value=3,font=("Calibri",14),command=dongabapan).place(x=580,y=100)
e1=Entry(w)
e1.place(x=250,y=270)
e2=Entry(w)
e2.place(x=250,y=310)
e3=Entry(w)
e3.place(x=250,y=350)
e4=Entry(w)
e4.place(x=250,y=390)
e5=Entry(w)
e5.place(x=250,y=430)
e6=Entry(w)
e6.place(x=250,y=470)
sp_no=1
p=0
m=None
b1=Button(w,text="pay bill",height=1,width=6,font=("Calibri",19),command=button).place(x=250,y=570)
l2=Label(w,text="Menu",font=("Calibri",19)).place(x=10,y=150)
w.mainloop()
