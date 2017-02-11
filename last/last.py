#coding=utf-8
from datetime import datetime
import winsound
d1 = datetime.now()
d2 = datetime(2017,5,14)
delt = d2-d1
delta = int(str(delt)[0:3])
print('今天是{now}'.format(now=str(d1)))
print('生物竞赛是2017-05-14')
print('剩余'+str(delta)+'天')
winsound.PlaySound('code.wav',winsound.SND_ASYNC)
