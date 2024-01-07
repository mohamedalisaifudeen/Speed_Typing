from wonderwords import  RandomSentence
from tkinter import *
from tkinter import ttk
from datetime import datetime



root=Tk()

s=RandomSentence()
new=s.sentence()

print(new)

frame=ttk.Frame(root,padding=10)
frame.grid()
root.title("Speed Typer")

lb1=ttk.Label(frame,text=new,font=("arial",15,'bold'))
lb1.grid(column=2,row=1,pady=20,padx=20)

lb9=ttk.Label(frame,text="*Plase hit enter after filling",font=("arial",15,'bold'),foreground="red")
lb9.grid(column=2,row=6,pady=20,padx=20)

txt=ttk.Entry(frame,width=40,font=("arial",12,'bold'))
txt.grid(column=2,row=2)




cps=ttk.Label(frame,text="Cps",font=("arial",15,'bold'))
cps.grid(column=2,row=5,pady=10)

cps_txt=ttk.Label(frame,text="0.00",font=("arial",15,'bold'))
cps_txt.grid(column=3,row=5,pady=10)

wpm=ttk.Label(frame,text="Wpm",font=("arial",15,'bold'))
wpm.grid(column=2,row=4,pady=10)

wpm_txt=ttk.Label(frame,text="0.00",font=("arial",15,'bold'))
wpm_txt.grid(column=3,row=4,pady=10,padx=20)
seco=1
def sec():
    global seco
    seco+=1


def check_pass(event):
    global seco,wpm
    if (new.startswith(txt.get())):
        txt.config(foreground='green')


        if (txt.get()==new):
            s=round(len(txt.get())/seco,1)
            cps_txt.config(text=s)
            wpm_txt.config(text=s*(60/5))
        else:
            root.after(1000, sec)


    else:
        txt.config(foreground="red")




def reset():
    global new,seco
    new=s.sentence()
    txt.delete(0,END)
    lb1.config(text=new)
    seco=1
    cps_txt.config(text="0.00")
    wpm_txt.config(text="0.00")



txt.bind('<Any-KeyPress>', check_pass)

btre=ttk.Button(frame,text='Reset',width=30,command=reset)
btre.grid(column=2,row=3,pady=10)


root.mainloop()









