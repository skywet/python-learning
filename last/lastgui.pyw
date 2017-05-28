#coding=utf-8
from datetime import datetime
from tkinter import *
import winsound

#倒计时逻辑模块
d1 = datetime.now()
d2 = datetime(2018,6,7)
delt = d2-d1
delta = int(str(delt)[0:3])

#基本倒计时显示
root = Tk()
root.title('高考倒计时')
lab0 = Label(root,text='御坂提示，高考',fg='#39C5BB',font=('微软雅黑',24,'bold'))
lab1 = Label(root,text='剩余{s}天'.format(s=delta),fg='#FF3366',font=('微软雅黑',30,'bold'))
but = Button(root,text='QUIT',fg='#66ccff',command=root.quit)

#倒计时御坂模块
filename = r'9982.gif'
img = PhotoImage(file=filename)
lab2 = Label(root,image=img)

#每十天御坂提示一次
stri = str(delta)[-1]
if int(stri)==0:
   winsound.PlaySound('code.wav',winsound.SND_ASYNC)

#运用grid进行排版
lab0.grid(row=1,column=1)
lab1.grid(row=2,column=1)
lab2.grid(row=1,column=4)
but.grid(row=2,column=4)
root.mainloop()
root.destroy()

