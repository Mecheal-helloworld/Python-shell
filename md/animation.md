[TOC]

### 一、包的导入

```python
import matplotlib.animation as animation
```

### 二、FuncAnimation

##### 语法格式：

```python
animation.FuncAnimation(fig, func, frames=None, init_func=None, fargs=None,save_count=None, *, cache_frame_data=True, **kwargs)
```

##### 参数详解：

fig——绘图对象

func——动态更新图像的函数

