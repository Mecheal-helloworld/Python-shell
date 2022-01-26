import os
import sys
import json
from datetime import datetime
try:
  from xlrd import open_workbook
  from xlrd import xldate_as_tuple
except:
  os.system(r"pip install xlrd")
  from xlrd import open_workbook
  from xlrd import xldate_as_tuple
try:
  from xlutils.copy import copy
except:
  os.system(r"pip install xlutils")
  from xlutils.copy import copy
try:
  import xlwt
except:
  os.system(r"pip install xlwt")
  import xlwt
path='C:/Users/ASUS/Desktop'#input("请输入地址:")
name=input("请输入文件名:")
rb = open_workbook(path+"\\"+name+'.xls')
#rb=open_workbook('C:/Users/ASUS/Desktop/TPA011.xls')
rs = rb.sheet_by_index(1)
rd = rb.sheet_by_index(0)
nrows=rs.nrows
nrows2=rd.nrows
wb=copy(rb)
ws=wb.get_sheet(1)
ws.write(0,4,"评论时间+评论人+评论文本")
ws.write(0,5,"评论数")
lists=[]
for i in range(nrows2):
  lists+=[0]
  lists[i]=0
for i in range(nrows):
  a=rs.cell_value(i,1)
  b=rs.cell_value(i,2)
  c=rs.cell_value(i,3)
  try:
    a=a+","+b+","
  except:
    b=datetime(*xldate_as_tuple(b,0))
    b=b.strftime("%Y-%m-%d %H:%M:%S")
    b=b.strip(" 00:00:00")
    a=a+","+b+","
  try:
    a=a+c
  except:
    c="%.3f" % c
    a=a+c
  ws.write(i,4,a)
  if i!=0:
    m=rs.cell_value(i,0)
    m=int(m)
    lists[m]+=1
for i in range(nrows2):
  ws.write(i,5,lists[i])
wb.save(path+"\\"+name+'.xls')
#wb.save('C:/Users/ASUS/Desktop/TPC001.xls')