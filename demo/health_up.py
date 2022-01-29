import time
from pymouse import *
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()
#click_list=[[325,750],[25,100],[100,100],[600,120],[600,200],[680,590],[680,590]]
open_list = [[325,750],[25,530],[120,490],[800,490]]
click_list = [[900,500],[900,600],[800,680]]
close_list = [[1110,10],[690,10]]
input_strs=["http://api.njust.edu.cn/healthReport/healthReport.html#/index"]

if __name__ == "__main__":
    for pos in open_list:
         m.click(pos[0],pos[1],1)
         time.sleep(1)
    m.scroll(-100,0)
    time.sleep(1)
    for pos in click_list:
         m.click(pos[0],pos[1],1)
         time.sleep(1)
    time.sleep(1)
    for pos in close_list:
         m.click(pos[0],pos[1],1)
         time.sleep(1)
'''
    for i in range(0):
        k.press_key(k.down_key)
        time.sleep(0.02)
        k.release_key(k.down_key)
        time.sleep(0.02)
    for stri in "http://api.njust.edu.cn/healthReport/healthReport.html#/index":
        k.tap_key(character=stri, n=1, interval=0.02)
        time.sleep(0.02)
    k.press_key(k.enter_key)
    time.sleep(0.02)
    k.release_key(k.enter_key)
    k.press_key(k.enter_key)
    time.sleep(0.02)
    k.release_key(k.enter_key)
    #k.press_key(k.enter_key)
'''