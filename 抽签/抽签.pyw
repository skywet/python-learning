#coding=utf-8
from tkinter import *
from random import randint
import re

f = open(r'name.txt','r',encoding='utf-8')
nl = re.split('\n',f.read())
line = len(nl)
i = randint(0,line)
name = nl[int(i)]
print(name)
root = Tk()

lab1 = Label(root,text='被抽到的人是',font=('微软雅黑',30,'bold'))
lab2 = Label(root,text=name,fg='red',font=('微软雅黑',50,'bold'))
but = Button(root,text='QUIT',fg='blue',command=root.quit)

lab1.pack()
lab2.pack()
but.pack()
root.mainloop()
root.destroy()
