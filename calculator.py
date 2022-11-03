from optparse import Option
from tkinter import *
from tkinter.ttk import Labelframe
import tkinter.font as font




window=Tk()
window.title("Calculator")
window.geometry('500x600')
window.configure(bg='#3297a8')
oldvalue=''

def button_click(num):
    global expression
    expression=expression + str(num)
    input_text.set(expression)
def button_clear():
    global expression
    expression=''
    input_text.set("")
def button_equal():
    global expression
    result=str(eval(expression))
    input_text.set(result)
    
expression=""

input_text=StringVar()

label=Frame(window,width=412,height=50,bg='white')
label.place(x=30,y=50)
input_field = Entry(label,font=('arial', 18, 'bold'), textvariable=input_text, width=30, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10,ipadx=12)

btns_frame = Frame(window, width=312, height=272.5,bg='#3297a8')
btns_frame.place(x=30,y=150)
button7= Button(btns_frame, font=('arial', 9, 'bold'),text = "7",cursor="hand2",width = 10, height = 3,fg="black" ,bd = 5, bg = "#c7c5c5",command= lambda: button_click('7')).grid(row = 1, column = 0,padx=10,pady=15 )
button8=Button(btns_frame,text='8',width=10,height=3,bd=5,bg="#c7c5c5",command= lambda: button_click('8')).grid(row=1,column=1,padx=10,pady=15 )
button9=Button(btns_frame,text='9',width=10,height=3,bd=5,bg="#c7c5c5",command= lambda: button_click('9')).grid(row=1,column=2,padx=10,pady=15 )
buttonplus=Button(btns_frame,text='+',width=10,height=3,bd=5,bg="#c7c5c5",command= lambda: button_click('+')).grid(row=1,column=3,padx=10,pady=15)
button4=Button(btns_frame,text='4',width=10,height=3,bd=5,bg="#c7c5c5",command= lambda: button_click('4')).grid(row=2,column=0,padx=10,pady=15)
button5=Button(btns_frame,text='5',width=10,height=3,bd=5,bg="#c7c5c5",command= lambda: button_click('5')).grid(row=2,column=1,padx=10,pady=15)
button6=Button(btns_frame,text='6',width=10,height=3,bd=5,bg="#c7c5c5",command= lambda: button_click('6')).grid(row=2,column=2,padx=10,pady=15)
buttonminus=Button(btns_frame,text='-',width=10,height=3,bd=5,bg="#c7c5c5",command= lambda: button_click('-')).grid(row=2,column=3,padx=10,pady=15)
button1=Button(btns_frame,text='1',width=10,height=3,bd=5,bg="#c7c5c5",command= lambda: button_click('1')).grid(row=3,column=0,padx=10,pady=15)
button2=Button(btns_frame,text='2',width=10,height=3,bd=5,bg="#c7c5c5",command= lambda: button_click('2')).grid(row=3,column=1,padx=10,pady=15)
button3=Button(btns_frame,text='3',width=10,height=3,bd=5,bg="#c7c5c5",command= lambda: button_click('3')).grid(row=3,column=2,padx=10,pady=15)
buttonmulti=Button(btns_frame,text='*',width=10,height=3,bd=5,bg="#c7c5c5",command= lambda: button_click('*')).grid(row=3,column=3,padx=10,pady=15)
buttonclear=Button(btns_frame,text='C',width=10,height=3,bd=5,bg="#c7c5c5",command= lambda: button_clear()).grid(row=4,column=0,padx=10,pady=15)
button0=Button(btns_frame,text='0',width=10,height=3,bd=5,bg="#c7c5c5",command= lambda: button_click('0')).grid(row=4,column=1,padx=10,pady=15)
buttonequal=Button(btns_frame,text='=',width=10,height=3,bd=5,bg="#c7c5c5",command= lambda: button_equal()).grid(row=4,column=2,padx=10,pady=15)
buttondivide=Button(btns_frame,text='/',width=10,height=3,bd=5,bg="#c7c5c5",command= lambda: button_click('/')).grid(row=4,column=3,padx=10,pady=15)


window.mainloop()