[参考文章]: https://www.cnblogs.com/fengmk2/archive/2008/04/21/1163766.html

##### 例子

```python
def function(*args, **kwargs):
    print 'args = ', args
    print 'kwargs = ', kwargs
    print '---------------------------------------'

if __name__ == '__main__':
    function(1,2,3,4)
    function(a=1,b=2,c=3)
    function(1,2,3,4, a=1,b=2,c=3)
    function('a', 1, None, a=1, b='2', c=3)
```

##### 输出结果：

```
args =  (1, 2, 3, 4)
kwargs =  {}
---------------------------------------
args =  ()
kwargs =  {'a': 1, 'c': 3, 'b': 2}
---------------------------------------
args =  (1, 2, 3, 4)
kwargs =  {'a': 1, 'c': 3, 'b': 2}
---------------------------------------
args =  ('a', 1, None)
kwargs =  {'a': 1, 'c': 3, 'b': '2'}
---------------------------------------
```

args表示任何多个**无名参数**，它是一个**tuple**；kwargs表示**关键字参数**，它是一个**dict**。并且同时使用args和kwargs时，**必须args参数列要在kwargs前**，像function(a=1, b='2', c=3, a', 1, None, )这样调用的话，会提示语法错误“SyntaxError: non-keyword arg after keyword arg”。

##### 补充：kwargs不影响参数位置

```python
def test(a,*args,**kwargs):
  print a
  #print b
  #print c
  print args
  print kwargs
test(1,2,3,d='4',e=5)
#1还是参数a的值，args表示剩余的值，kwargs在args之后表示成对键值对。
```

输出结果：

```
1
(2, 3)
{'e': 5, 'd': '4'}
```

