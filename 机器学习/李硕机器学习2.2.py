
import numpy as np
import matplotlib.pyplot as plt
import math
import random
 
data_x = np.loadtxt("ex4Data/ex4x.dat")
data_y = np.loadtxt("ex4Data/ex4y.dat")

def sigmoids(x):
    return 1/(math.exp(-x)+1)

plt.axis([15, 65, 40, 90])
plt.xlabel("exam 1 score")
plt.ylabel("exam 2 score")
for i in range(data_y.size):
    if data_y[i] == 1:
        plt.plot(data_x[i][0], data_x[i][1], 'b+')
    else:
        plt.plot(data_x[i][0], data_x[i][1], 'bo')
 
mean = data_x.mean(axis=0)
variance = data_x.std(axis=0)
data_x = (data_x-mean)/variance
 
data_y = data_y.reshape(-1, 1)          # 拼接
temp = np.ones(data_y.size)
data_x = np.c_[data_x, temp]
 
learn_rate = 0.1
theda = np.zeros([3])
 
loss = 0
old_loss = 0
 
for i in range(data_y.size):
    if data_y[i] == 1:
        loss += math.log10(sigmoids(np.matmul(data_x[i], theda)))
    else:
        loss += math.log10(1-sigmoids(np.matmul(data_x[i], theda)))
 
while abs(loss-old_loss) > 0.001:
    temp = np.matmul(data_x, theda)
    dew = np.zeros([3])
    j = random.randint(0, data_y.size-1)
    dew += (data_y[j]-sigmoids(temp[j]))*data_x[j]
    z = random.randint(0, data_y.size - 1)
    while j == z:
        z = random.randint(0, data_y.size - 1)
    dew += (data_y[z] - sigmoids(temp[z])) * data_x[z]
    theda = theda+learn_rate*dew
    old_loss = loss
    loss = 0
    for i in range(data_y.size):
        if data_y[i] == 1:
            loss += math.log10(sigmoids(np.matmul(data_x[i], theda)))
        else:
            loss += math.log10(1 - sigmoids(np.matmul(data_x[i], theda)))
    print(-old_loss)
plot_y = np.zeros(65-16)
plot_x = np.arange(16, 65)
for i in range(16, 65):
    plot_y[i-16] = -(theda[2]+theda[0]*((i-mean[0])/variance[0]))/theda[1]
    plot_y[i - 16] = plot_y[i-16]*variance[1]+mean[1]
plt.plot(plot_x, plot_y)
plt.show()
