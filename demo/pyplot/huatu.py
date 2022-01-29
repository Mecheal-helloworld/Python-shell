import numpy as np
import matplotlib.pyplot as plt

# 从-3到中取50个数
x = np.linspace(-3, 3, 50)
print(x)
y1 = 2*x+1
y2 = x**2
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=10.0, linestyle='--')   # linewidth 设置线的宽度， linesyyle设置线的形状
# savefig  保存图片
plt.show()