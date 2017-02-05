#coding:utf-8
import re
import time

rt = time.localtime()
rm = rt[1]
f = open(r'ID.txt','r',encoding='utf-8')
for line in f:
    lst = re.split(r'[ \t]+',line)
    bd = lst[3]
    bm = re.split('/',bd)
    if int(rm)==int(bm[1]):
        dat = int(bm[2])-rt[2]
        print('ID:{ID}   姓名：{name}   生日：{birthday}  剩余时间：{date}'.format(ID=lst[0],name=lst[1],birthday=bd,date=dat))