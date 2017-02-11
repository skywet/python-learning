#coding=utf-8
from datetime import datetime
import winsound
from tkinter import *

d1 = datetime.now()
d2 = datetime(2017,5,14)
delt = d2-d1
delta = int(str(delt)[0:3])

stri = str(delta)[-1]
if int(stri)==0:
   winsound.PlaySound('code.wav',winsound.SND_ASYNC)
    
root = Tk()
lab1 = Label(root,text='现在是：'+str(d1))
lab2 = Label(root,text='生物竞赛举行于2017/5/14')
lab3 = Label(root,text='剩余{s}天'.format(s=delta),font=('微软雅黑',30,'bold'))
but = Button(root,text='QUIT',fg='red',command=root.quit)

lab1.pack()
lab2.pack()
lab3.pack()
but.pack()
root.mainloop()
root.destroy()

