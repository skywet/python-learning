#coding=utf-8
import os,sys,time,re
from shutil import copy2
import multiprocessing

def op():
    os.system(r'tree /F C:\\')

def get(find):
    i = 1
    a = os.popen(r'dir /b /s C:\\')
    f = open('out.txt','a',encoding='utf-8')
    f.write(a.read())
    f.close()
    z = open('out.txt','r',encoding='utf-8')
    for line in z:
        if re.search(find,line):
            os.mkdir('F:\\data')
            copy2(line,'F:\\data')

q = input('please input what you expect')

if __name__ == '__main__':
    pa = multiprocessing.Process(target=op,args=())
    pb = multiprocessing.Process(target=get,args=(str(q),))
    pa.start()
    pb.start()


