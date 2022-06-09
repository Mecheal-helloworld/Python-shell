from numpy import *
import numpy as np

m=14
x0=ones((m,1))
x1=arange(0,m).reshape(m,1)
x=hstack((x0,x1))

y=np.array([2.000,2.500,2.900,3.147,4.515,4.903,5.365,5.704,6.853,7.971,8.561,10.000,11.280,12.900]).reshape(m,1)
alpha=0.01

#loss函数
def loss(theta, X, Y):
    a = dot(X, theta) - Y  #dot 矩阵相乘 (h(x)-y)
    return (1 / (2*m)) * dot(a.transpose(), a)

# 定义代价函数对应的梯度函数
def gradient_function(theta, X, Y):
    a = dot(X, theta) - Y
    return (1/m)*dot(X.transpose(), a)

# 梯度下降迭代
def gradient_descent(X, Y, alpha):
    theta = array([1, 1]).reshape(2, 1)
    gradient = gradient_function(theta, X, Y)
    while not all(abs(gradient) <= 1e-6):
        theta = theta - alpha * gradient
        gradient = gradient_function(theta, X, Y)
    return theta

#结果
out = gradient_descent(x, y, alpha)

print('结果是:', out)

def plot(x, y, theta):
    import matplotlib.pyplot as plt
    ax = plt.subplot(111)
    ax.scatter(x, y, s=30, c="red", marker="s")
    plt.xlabel("X")
    plt.ylabel("Y")
    x = arange(0, 15, 1)
    y = theta[0] + theta[1]*x
    pre=theta[0] + theta[1]*14
    ax.plot(x, y)
    plt.show()
    return pre

i=plot(x1,y, out)
print('预测2014的房价是:',i)