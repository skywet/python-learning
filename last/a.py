#python tkinter image

from tkinter import *

__author__ = {'name' : 'Hongten',
              'mail' : 'hongtenzone@foxmail.com',
              'blog' : 'http://www.cnblogs.com/',
              'QQ': '648719819',
              'created' : '2013-09-20'}


def main():
    filename = '9982.gif'
    root = Tk()
    img = PhotoImage(file=filename)
    label = Label(root, image=img)
    label.pack()
    root.mainloop()

main()
