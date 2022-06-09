import os
import matplotlib.pyplot as plt
try:
  import time
except:
  os.system(r"pip install time")
try:
  import numpy
except:
  os.system(r"pip install numpy")
def h_sita(sita,x):
  return numpy.transpose(sita)*x
def sita_star(X,y):
  return (numpy.transpose(X)*X).I*numpy.transpose(X)*y
x=[1]
x_result=[]
X=[]
for i in range(14):
  x_result.append(2000+i)
  x.append(2000+i)
  X.append(x)
  x=[1]
X=numpy.mat(X)
y=[2.000,2.500,2.900,3.147,4.515,4.903,5.365,5.704,6.853,7.971,8.561,10.000,11.280,12.900]
y_result=y
y=numpy.mat(y)
y=numpy.transpose(y)
sita_star=sita_star(X,y)
def draw(rx, ry, rsita):
  plt.xlabel("X")
  plt.ylabel("Y")
  plt.plot(rx,ry,"ro")
  rx.append(2014)
  print(rsita[0])
  ry1=rsita[0]+rsita[1]*rx
  plt.plot(rx,ry1)
  plt.show()
def print_result():
  x=[1]
  x.append(14)
  x=numpy.mat(x)
  x=numpy.transpose(x)
  sita_result=numpy.array(sita_star)
  print("我的模型的sita为：")
  print(sita_star)
  result=h_sita(sita_star,x)
  print(result)
  print("我的模型预测的2014年的房价为：",end="")
  print(result[0,0])
  draw(x_result,y_result,sita_result)
print_result()
print("感谢使用！")
time.sleep(0.5)