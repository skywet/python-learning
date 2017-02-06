#coding=utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

driver = webdriver.PhantomJS()
driver.get(r'http://www.swtk.cn')
sleep(3)
driver.find_element_by_name('uname').send_keys('skywet')
driver.find_element_by_name('upwd').send_keys('1101221wtyjack')
driver.find_element_by_class_name('sbmitys').click()
sleep(3)
driver.get(r'http://www.swtk.cn/team/member.php?tid=353')
driver.find_element_by_link_text('风中笑霸').click()
sleep(2)
qzx = driver.page_source
f=open('a.txt','a',encoding='utf-8')
f.write(qzx)
f.close()