import os 
 
def file_name(file_dir):
  L=[] 
  for root,dirs, files in os.walk(file_dir):  
    #print(root) #当前目录路径 
    #print(dirs) #当前路径下所有子目录
    #print(files) #当前路径下所有非目录子文件
    for file in files:
      if os.path.splitext(file)[1]=='.txt':
        L.append(os.path.join(file))
  return L
def Add(str):
  f=open("C:/Users/ASUS/ansel/Filters/密码本/"+str+".txt","w+",encoding="gbk")
  print("请输入账号和密码")
  for i in range(2):
    str1=input()
    f.write(str1)
    f.write('\n')
  print("输入完成")
  f.close()
def ReadAll():
  a=file_name("C:/Users/ASUS/ansel/Filters/密码本")
  #print(a[0])
  for x in a:
    print(x)
    f=open("C:/Users/ASUS/ansel/Filters/密码本/"+x,'r',encoding="gbk")
    b=f.read()
    #for xi in b:
      #print(xi)
    print(b)
    print()
def ChangeTXT():
  file_name = input("请输入文件名（xxx）：")
  f=open("C:/Users/ASUS/ansel/Filters/密码本/"+file_name+".txt",'r',encoding="gbk")
  lines = f.read()
  print(lines)
  f.close()
  f=open("C:/Users/ASUS/ansel/Filters/密码本/"+file_name+".txt",'w',encoding="gbk")
  print("请输入新的账号和密码")
  for i in range(2):
    str1=input()
    f.write(str1)
    f.write('\n')
  print("输入完成")
  f.close()
def NewTXT():
  str_1=input("请输入文件名（xxx）：")
  if str_1:
    print("输入成功")
    Add(str_1)
ReadAll()
b='Y'
b=input("是否退出[Y/N]:")
while b=='N':
  str_mode=input("请选择需要进行的操作（更改或新建）[C/N]:")
  if str_mode=='C':
    ChangeTXT()
  else:
    NewTXT()
  b=input("是否退出[Y/N]:")