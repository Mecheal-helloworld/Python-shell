[TOC]

### 1、包的导入

```python
import numpy as np
```

### 2、arange生成数组

##### 2.1语法格式

```python
numpy.arange(start, stop, step, dtype = None)
```

在给定间隔内返回均匀间隔的值。值在半开区间 [开始，停止]内生成（包括开始但不包括停止的区间）,返回的是 ndarray 。

##### 2.2参数

start —— 开始位置，数字，**可选项**，默认起始值为0
stop —— 停止位置，数字
step —— 步长，数字，**可选项**， 默认步长为1，如果指定了step，则还必须给出start。
dtype —— 输出数组的类型。 如果未给出dtype，则从其他输入参数推断数据类型。

**返回：**
返回类型：numpy.ndarray，均匀间隔值的数组。
注意：对于浮点参数（参数为浮点），结果的长度为ceil（（stop - start）/ step）） 由于浮点溢出，此规则可能导致最后一个元素大于stop。因此要特别注意

##### 2.3例子

```python
import numpy as np
np.arange(1, 10, 10)
```

输出：array([1])

```python
np.arange(0,10,1)
#np.arange(10)
```

输出：array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

```python
np.arange(0,10,1,float)
#np.arange(0.0,10.0,1)
```

输出：array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])

### 3、linspace生成数组

##### 3.1语法格式

```
numpy.linspace(start,stop,num,endpoint,retstep,dtype)
```

##### 3.2参数

start——开始位置，数字

stop——序列的结束点

num——生成的样本数，默认是50。必须是非负。

endpoint——默认为False，如果是True，则一定包括stop，如果为False，一定不会有stop

retstep——默认为False，如果是True，则同时返回步长，如果为False，只返回数组。

dtype——输出数组的类型。 如果未给出dtype，则从其他输入参数推断数据类型。

##### 返回

返回类型：numpy.ndarray，均匀间隔值的数组。

##### 3.3例子

```
import numpy as np
np.linspace(1, 10, 10)
```

输出：array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])

```
np.linspace(1, 10, 10, endpoint = False)
```

输出：array([1. , 1.9, 2.8, 3.7, 4.6, 5.5, 6.4, 7.3, 8.2, 9.1])

```python
 np.linspace(1, 10, 10, endpoint = False, retstep= True)
 #np.linspace(1, 10, 10, False,True)
```

输出：(array([1. , 1.9, 2.8, 3.7, 4.6, 5.5, 6.4, 7.3, 8.2, 9.1]), 0.9)

### 4、np.random.uniform

##### 3.1语法格式

```python
numpy.random.uniform(low=0.0, high=1.0, size=None)
#从一个均匀分布[low,high)中随机采样，注意定义域是左闭右开，即包含low，不包含high.
```

##### 3.2参数

low——采样下界，float类型，默认值为0；

high——采样上界，float类型，默认值为1；

size——输出样本数目，为int或元组(tuple)类型，例如，size=(m,n,k), 则输出 m * n * k 个样本，缺省时输出1个值。

##### 返回

返回类型：numpy.ndarray，其形状和参数size中描述一致。

##### 3.3例子

```python
import numpy as np
np.random.uniform(-0.25, 0.25, 300)
#array([ 0.11774701, -0.09188408, -0.15208505,  0.04098993,  0.20436965])
```

### 5、函数

##### 5.1三角函数

提供了标准的三角函数：sin()、cos()、tan()

##### 5.2反三角函数

arcsin，arccos，和 arctan 函数返回给定角度的 sin，cos 和 tan 的反三角函数

这些函数的结果可以通过degrees() 函数将弧度转换为角度

### 6、around四舍五入

##### 6.1语法格式

```
numpy.around(a,decimals)
```

##### 6.2参数

a——输入数字或数组

decimals——四舍五入的位置，默认为0。

##### 6.3例子

```python
np.around(22222.22222)
np.around(22222.22222,0)
np.around(22222.22222,1)
np.around(22222.22222,-1)
```

输出：22222.0

​			22222.0

​			22222.2

​			22220.0

### 7、ceil和floor向上向下取整

##### 7.1格式

```
np.ceil(a)
np.floor(a)
```

##### 7.2参数

a——输入的数字或数组

##### 返回

ceil向上取整，floor向下取整

##### 7.3例子

```python
a=np.linspace(1, 10, 10, endpoint = False)#array([1. , 1.9, 2.8, 3.7, 4.6, 5.5, 6.4, 7.3, 8.2, 9.1])
np.ceil(a)
np.floor(a)
```

输出：array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])

​			array([1., 1., 2., 3., 4., 5., 6., 7., 8., 9.])