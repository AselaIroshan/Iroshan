from tkinter import *
import tkinter.font as font
 

root = Tk()
root.title("calculator")
root.minsize(435,500)
root.maxsize(435,500)
root.config(bg="gray15") 

number = []
calculation = None
ans = None
num1 = None
num2 = None
strnumber = []
dot = False



def numb_1():
    number.append(1)
    strnumber.append("1")
    
    s = ''.join(str(x) for x in strnumber)
    h.config(text=s)
    
def numb_2():
    number.append(2)
    strnumber.append("2")
    s = ''.join(str(x) for x in strnumber)
    h.config(text=s)


def numb_3():
    number.append(3) 
    strnumber.append("3")
    s = ''.join(str(x) for x in strnumber)
    h.config(text=s)

def numb_4():
    number.append(4)
    strnumber.append("4")
    s = ''.join(str(x) for x in strnumber)
    h.config(text=s)

def numb_5():
    number.append(5)
    strnumber.append("5")
    s = ''.join(str(x) for x in strnumber)
    h.config(text=s)
    
def numb_6():
    number.append(6)
    strnumber.append("6")
    s = ''.join(str(x) for x in strnumber)
    h.config(text=s)
    
def numb_7():
    number.append(7)
    strnumber.append("7")
    s = ''.join(str(x) for x in strnumber)
    h.config(text=s)
    
def numb_8():
    number.append(8)
    strnumber.append("8")
    s = ''.join(str(x) for x in strnumber)
    h.config(text=s)

def numb_9():
    number.append(9)
    strnumber.append("9")
    s = ''.join(str(x) for x in strnumber)
    h.config(text=s)
    
def numb_0():
    number.append(0)
    strnumber.append("0")
    s = ''.join(str(x) for x in strnumber)
    h.config(text=s)
    
def numb_sub():
    
    global number
    global num1
    global calculation
    strnumber.append("-")
    
    s = ''.join(str(x) for x in strnumber)
    h.config(text=s)
    calculation = "sub"
    sring = ""
    for i in number:
        sring+=str(i)
    num1 = int(sring)
    number.clear()



def numb_add():
    global calculation
    global num1 
    global number
    strnumber.append("+")
    s = ''.join(str(x) for x in strnumber)
    h.config(text=s)
    calculation = "add"
    sring = ""
    for i in number:
        sring+=str(i)
    num1 = int(sring)
    number.clear()

def numb_div():
    global num1
    global calculation
    strnumber.append("/")
    s = ''.join(str(x) for x in strnumber)
    h.config(text=s)
    calculation ="div"
    sring = ""
    for i in number:
        sring+=str(i)
    num1 = int(sring)
    number.clear()

def numb_mul():
    global num1
    global calculation
    strnumber.append("*")
    sring = ""
    s = ''.join(str(x) for x in strnumber)
    h.config(text=s)
    calculation ="mul"
    for i in  number:
        sring+=str(i)
    num1 = int(sring)
    number.clear()


def numb_dot():
    strnumber.append(".")
    s = ''.join(str(x) for x in strnumber)
    h.config(text=s)
    




def add (x,y):
    ans = num1 + num2
    h.config(text=ans)

def sub (x,y):
    ans = x -y
    h.config(text=ans)

def div (x,y):
    x = float(x)
    y = float(y)
    ans = x / y
    h.config(text=ans)

def mul (x,y):
    ans = x * y
    h.config(text=ans)


def numb_c():
    global num2
    sring = ""
    for i in number:
        sring+=str(i)
    num2 = int(sring)
    number.clear()
    
    if calculation =="sub":
        sub(num1,num2)
    
    elif calculation =="add":
        add(num1,num2)

    elif calculation =="mul":
        mul(num1,num2)

    elif calculation == "div":
        div(num1,num2)

h=Label(root,text="0",font=('TkFixedFont', 50),bg="gray15",fg="white")
h.place(x=20,y=0)


num_1=Button(root,text="1",command=numb_1,width=12,height=7,bg="gray20")
num_1.place(x=20,y=100)
num_2=Button(root,text="2",command=numb_2,width=12,height=7,bg="gray20")
num_2.place(x=120,y=100)
num_3=Button(root,text="3",command=numb_3,width=12,height=7,bg="gray20")
num_3.place(x=220,y=100)
num_4=Button(root,text="4",command=numb_4,width=12,height=7,bg="gray20")
num_4.place(x=20,y=200)
num_5=Button(root,text="5",command=numb_5,width=12,height=7,bg="gray20")
num_5.place(x=120,y=200)
num_6=Button(root,text="6",command=numb_6,width=12,height=7,bg="gray20")
num_6.place(x=220,y=200)
num_7=Button(root,text="7",command=numb_7,width=12,height=7,bg="gray20")
num_7.place(x=20,y=300)
num_8=Button(root,text="8",command=numb_8,width=12,height=7,bg="gray20")
num_8.place(x=120,y=300)
num_9=Button(root,text="9",command=numb_9,width=12,height=7,bg="gray20")
num_9.place(x=220,y=300)
num_0=Button(root,text="0",command=numb_0,width=12,height=7,bg="gray20")
num_0.place(x=120,y=400)
num_sub=Button(root,text="-",command=numb_sub,width=12,height=6,bg="gray20")
num_sub.place(x=320,y=200)
num_add=Button(root,text="+",command=numb_add,width=12,height=6,bg="gray20")
num_add.place(x=320,y=100)
num_div=Button(root,text="/",command=numb_div,width=12,height=7,bg="gray20")
num_div.place(x=320,y=300)
num_mul=Button(root,text="*",command=numb_mul,width=12,height=7,bg="gray20")
num_mul.place(x=320,y=400)
num_cal=Button(root,text="=",command=numb_c,width=12,height=7,bg="#6666CD")
num_cal.place(x=220,y=400)
num_dot=Button(root,text=".",command=numb_dot,width=12,height=7,bg="gray20")
num_dot.place(x=20,y=400)


root.mainloop()
