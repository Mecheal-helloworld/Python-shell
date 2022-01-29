import os
import sys
import re
import json
try:
  from xlrd import open_workbook
except:
  os.system(r"pip install xlrd")
try:
  from xlutils.copy import copy
except:
  os.system(r"pip install xlutils")
try:
  import xlwt
except:
  os.system(r"pip install xlwt")
def GetDesktopPath():
  return os.path.join(os.path.expanduser("~"),'Desktop')
def file_name(file_dir):
  L=[] 
  for root,dirs, files in os.walk(file_dir):  
    #print(root) #当前目录路径 
    #print(dirs) #当前路径下所有子目录
    #print(files) #当前路径下所有非目录子文件
    for file in files:
      if os.path.splitext(file)[1]=='.jpg':
        L.append(os.path.join(file))
  return L
year=input("请输入年份：")
rb=open_workbook(GetDesktopPath()+"\\"+'暂缓注册20200914.xls')
rs=rb.sheet_by_index(0)
nrows=rs.nrows
#for i in range(nrows):
  #print(rs.cell_value(i,1))
a=file_name(GetDesktopPath()+"\\"+year+"退学文件")
path=GetDesktopPath()+"\\"+year+"退学文件"
print(path)
count=1
for x in a:
  x1=x.strip(str(year)).rstrip('.jpg')
  x2=x1.rstrip(' ')
  x3=x2.rstrip('(2)')
  x4=x3.rstrip(' ')
  print(x4)
  for i in range(nrows):
    if(rs.cell_value(i,1)==x4):
      try:#if(os.access(path+"\\"+rs.cell_value(i,0)+x1+".jpg", os.F_OK)):
        os.rename(os.path.join(path,x),os.path.join(path,rs.cell_value(i,0)+x1+".jpg"))
      except:
        print("change error!")
    