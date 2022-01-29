import matplotlib.pyplot as plt
#plt.plot([1,2,3,4],[1,4,9,16])
x=[1,2,3,4]
y=[]#y为一个list元素
for xi in x:
  yi=xi*2
  y.append(yi)
plt.plot(x,y)
plt.show()