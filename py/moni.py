import pymouse,pykeyboard,os,sys
from pymouse import *
from pykeyboard import PyKeyboard
import time
m = PyMouse() 
k = PyKeyboard()
def hit(str_1):
  '''
  m.click(600,400,1)
  k.type_string(str_1)
  m.click(600,510,1)
  m.click(700,450,1)
  '''
  print(str_1)
#strs="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789.!@#$%^&*()_+"
strs=input()
def digui(l,mima):
  if l==0:
    hit(mima)
  else:
    for j in range(len(strs)):
      yuanmima=mima
      mima+=strs[j]
      digui(l-1,mima)
      mima=yuanmima
for i in range(3,6):
  st=""
  digui(i,st)