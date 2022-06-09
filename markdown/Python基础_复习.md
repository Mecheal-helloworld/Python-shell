## Python基础

#### 基础类型

##### Number（数字）

```python
# 逻辑值
True 非0
False 0
# int
a = 1
b = 1.0
c = "123"
a = int()
a = int(b)
a = int(c)
# float
a = 1.0
b = 1
c = "1.23"
a = float(b)
a = float(c)
```



##### String（字符串）

```python
# str '' "" ''' '''
# '\'' "\""
'''
123
'''
s1 = "0123456"
s1 = str()
# 获取字符串的子串
s2 = s1[0:2]
s2 = s1[:2]
s2 = s1[1:]
s2 = s1[:]
s2 = s1[2:-1]
s2 = s1[-3:-1]
#获取字符串的对应字符
s2 = s1[2]
#字符串去除首尾指定字符
s3 = s1.strip()
# 字符串分割成列表
s4 = s1.split("")
# 替代
s1.replace("a","b")
# 返回指定子串在字符串中的出现位置，没有找到就返回-1
s1.find(str_child)
# 返回指定子串在该字符串中第一次出现的索引，没有找到就抛出异常
s1.index(str_child)
# 返回指定子串在该字符串中出现的次数
s1.count(str_child)
```



##### List（列表）

```python
# 列表定义
a = []
a = [1,2,3]
a = list()
# 访问元素
b = a[2]
c = a[0:2]
# 添加元素
b = 1
a.append(b)
# 删除元素
a.remove(value) # 只删除第一个元素
del a[2]
# 列表大小
len(a)
# 列表排序
a.sort(key=lambda x: x[1], reverse=True)# list类型内置方法
sorted(a)# 可迭代的序列排序生成新的序列
```



##### Tuple（元组）

```python
# 元组定义
a = (1,"",3.0)
a = tuple()
b = 1
c = 2
a = (b,c)
b = ((1,2),(3,4))
list2 = [(1,2),(3,4)]
list1 = [(data,label),(data,label)]
val1,val2 = a
for data,label in list2:
    pass
# 注意：元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
a = (b,)
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
# tuple大小
len1 = len(tup3)
```



##### Set（集合）

```python
# 集合定义
a = {1,2}
a = set()
# 添加元素
b = 1
a.add(b)
# 删除元素
a.remove(b)
# 不支持按索引访问
```



##### Dictionary（字典）

```python
# 字典定义
a = {}
a = dict()
a = {"1":111,"2":"aaa"}
# 删除键 '1'
del a['1']
# 清空字典
a.clear()
# 字典转键/值列表
keys = list(a.keys())
values = list(a.values())
```



#### 基础语法

##### if条件语句

```python
if condition_1:
    pass
elif condition_2:      
    pass
elif condition_3:      
    pass
else:
    pass
if a<b:
if a>b:
if a and b:
if a or b:
if not a:
if x not in a:
```

##### for循环

```python
for i in range(1,5):
    pass
```

##### 迭代



##### while循环

```python
while condition_1:
    pass
```



##### def函数定义

```python
def func_1(s,b,c):
    print(s)
    a = 1
    d = "123"
    if s>0:
        return a+b
    else:
        return d
def func_2(m,key=1):
    print(m)
    a = 1
def func_3(m,key=1,*args): # *arg [12,3,5]  func_3(1,2,3,4)
    def func_2(args):
        pass
    func_2(1)
    a = 1
def func_4(m,key=1,*args,**keys):# **keys {"a":11}  func_3(1,key=2,a=3)
    print(m)
    print(key)
    print(args)
    print(keys)
    if "x" in list(keys.keys()):
        print(keys["x"])
if __name__ == "__main__":
    func_1(1,2,key=1) # 不能写成 func_1(1,key=1,2)
    func_2(1,2,3)
    func_2(s=1,b=2,c=3)
```

##### try错误处理

```python
try:
    pass
except:
    pass

try:
    pass
except:
    pass
else:
    pass
finally:
    pass


try:
    a = b
    a()
    print("111")
except FileNotFoundError as err:
    print("File")
except:
    print(a)
    print("222")
else:
    print(a())
    print("333")
finally:
    print("final")
    
# 抛出异常
raise Exception()


a = b
print(a())
```



##### import模块

```python
# 
import json
import os ,sys
from PyQt5 import QtWidgets #从文件夹中引入模块
from PyQt5.QtWidgets import QApplication, QWidget, QLabel# 从模块中引入子模块
from json import load  # 从模块中引入函数
# 错误import json.load

import numpy as np
json.load()
load()
# __all__ = ["load1"] # 字符串列表，存储本文件中可被导入的模块名称
# from xxx import * 时使用可以保证只导入__all__中的模块
# __all__ 的作用就是定义公开接口
'''
Python在执行import语句时，执行了如下操作：
第1步，创建一个新的，空的module对象（它可能包含多个module）；
第2步，把这个module对象插入sys.module中
第3步，装载module的代码（如果需要，首先必须编译）
第4步，执行新的module中对应的代码。
'''
```



### 类和对象

```python
class ClassName:
    # __new__(cls)  return obj空的对象就行 只需要用object里的就行，不需要复写
    # 构造方法，该方法在类实例化时会自动调用
    def __init__(self,n,data):
        self.name = n
        self.data = data
        self.__value = len(n)
    # 两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用
    def __func(self):
        print(self.__class__)
    # 类的方法有一个额外的第一个参数名称, 按照惯例它的名称是 self
    def func(self):
        print(self)
        self.__func()
    @staticmethod
    def func_1():
        
# 构造类的对象并赋值给obj变量进行使用
obj = ClassName("Li Hua",[1,2,3])
# 获取对象的属性值
obj.new_l = 1
obj.name
list1 = obj.data
# 无法使用对象访问类的私有方法
obj.__func()
# 使用对象的方法
obj.func()
```

#### 继承

```python
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def people_func(self):
        pass
 
#单继承示例
class student(people):
    
    grade = ''
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    def __init__(self,n,a,w,g):
        #调用父类的构造函数
        people.__init__(self,n,a,w)# super(student,self).__init__(n,a,w)
        self.grade = g
        self.__weight
    def people_func(self):
        super(student,self).people_func()
        pass
    def student_func(self):
        pass
a = student()
super(student,a).people_func()
```



##### 方法重写

```python
class Parent:        # 定义父类
   def myMethod(self):
      print('调用父类方法')
 
class Child(Parent): # 定义子类
   def myMethod(self):
      print('调用子类方法')

class Children(Parent): # 定义子类
   def myMethod(self):
      super().myMethod()# 调用父类方法
      print('调用子类方法')
 
c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法 super(type, obj)
c = Children()          # 子类实例
c.myMethod()         # 子类调用重写方法
```

#### Python内置类属性

- **_ _ dict _ _** : 类的属性（包含一个字典，由类的数据属性组成）

- **_ _ name _ _**: 类名

- **_ _ module _ _**: 类定义所在的模块（类的全名是'_ _ main_ _ .className'，如果类位于一个导入模块mymod中，那么className._ _ module_ _  等于 mymod）  ***具体是干啥用的

  

- 一个类就相当于系统中类定义的类的一个对象

#### Python内置类的专有方法：

- **_ _ init _ _ :** 构造函数，在生成对象时调用 class()
- **_ _ del _ _ :** 析构函数，释放对象时使用  del
- **_ _ repr _ _ :** 打印，转换 print
- **_ _ setitem _ _:** 按照索引赋值 []=
- **_ _ getitem _ _:** 按照索引获取值 []
- **_ _ len _ _:** 获得长度 len()
- **_ _ cmp _ _:** 比较运算  sorted()      ***是sorted还是.sort
- **_ _ call _ _:** 函数调用 object()
- **_ _ add _ _:** 加运算 +
- **_ _ sub _ _:** 减运算 -
- **_ _ mul _ _:** 乘运算 *
- **_ _ truediv _ _:** 除运算 /
- **_ _floordiv _ _:** 整除运算 //
- **_ _ mod _ _:** 求余运算 %
- **_ _ pow _ _:** 乘方 **



#### 命名空间

**局部的命名空间 -> 全局命名空间 -> 内置命名空间**

##### 局部命名空间

函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

##### 全局命名空间

```python
# var1 是全局变量
var1 = 5
def some_func():
    # var2 是局部变量
    var2 = 6
    def some_inner_func():
        # var3 是内嵌的局部变量
        a = var3
        var3 = 7
if True:
    a = 1#a 为全局变量
```



##### 内置命名空间

Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等



#### 作用域

##### 四种作用域：

- **L（Local）**：最内层，包含局部变量，比如一个函数/方法内部。
- **E（Enclosing）**：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的变量来说 A 中的作用域就为nonlocal。
- **G（Global）**：最外层，比如当前模块的全局变量。
- **B（Built-in）**： 包含了内建的变量/关键字等，最后被搜索。

Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块不会引入新的作用域，也就是说条件/循环等语句内定义的变量，外部也可以访问。

##### 局部作用域

定义在函数内部的变量拥有一个局部作用域。

##### 全局作用域

定义在函数外的拥有全局作用域。

##### 嵌套作用域

定义在嵌套函数内部的变量拥有嵌套作用域。

##### 内置作用域

内置作用域是通过一个名为 builtin 的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能够使用它。

##### global关键字

将一个变量声明为全局变量

相当于把一个变量从局部命名空间放到全局命名空间

##### nonlocal关键字

寻找上层的局部变量，并将其声明为拥有嵌套作用域的变量

把一个局部命名空间的变量提升到上一层



### 拷贝

**浅拷贝和深拷贝**在处理本质上是嵌套结构的复合对象时才有用

#### 赋值

把一个对象赋值给一个变量时，变量 a 和 b 对同一个对象都有相同的引用。这意味着，如果这两个变量中的任何一个用于执行就地修改，其他变量也将受到影响。

对象a

class Student:

​    def __init__():

​            self.cla = Classmate()

a   =  Student()

b   =    a

b.func()

#### 浅拷贝

b = copy(a)    #copy出一个新的对象,a和b就是不同的对象了

b.func()

浅拷贝就是self.cla是指向同一个对象

a 和 b 是不同的对象，但内部对象(即两个内部列表)与原始对象引用的对象相同。不必处理复合对象时，浅拷贝才适用。

#### 深拷贝

深层拷贝将获取原始对象的副本，然后递归地获取找到的内部对象的副本(如果有的话)。当我们必须处理复合对象并希望确保任何内部对象的更改都不会影响引用相同对象的其他变量时，深拷贝更为合适。

深拷贝就是self.cla是指向不同的对象







a = [...]

b = {...}

c = ()

d=[a,b,c]

f=d

a2 = []

b2 = []

c2 = ()

d2 = [a2,b2,c2]

f=deepcopy(d)



a={}

b={}

a["value"] = ""

b["xxx"] = a

b["aaa"] = "111"

d1 = deepcopy(b)

d1做操作

d2 = deepcopy(b)

d2做操作
