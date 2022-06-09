## Python常用GUI库

​		GUI(图形用户界面)，顾名思义就是用图形的方式，来显示计算机操作的界面，更加方便且直观。与之相对应的则是CUI(命令行用户交互)，就是常见的Dos命令行操作，需要记忆一些常用的命令，对于普通人而言，操作起来学习难度还是蛮高的。一个好看又好用的GUI，可以大大提高大家的使用体验，提高效率。以下七个PythonGUI库，每一个都值得学习。

### 一、PyQt5

PyQt5由Riverbank Computing开发。基于Qt框架构建，是一个跨平台框架，可以给各种平台创建应用程序，包括：Unix、Windows、Mac OS。

PyQt将Qt和Python结合在一起。它不只是一个GUI工具包。还包括了线程，Unicode，正则表达式，SQL数据库，SVG，OpenGL，XML和功能完善的Web浏览器，以及许多丰富的GUI小部件集合。

**使用pip安装一下**

```
# 安装PyQt5
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PyQt5
```

安装成功后，来个Hello Word**简单示例**。

```
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

# 建立application对象
app = QApplication(sys.argv)
# 建立窗体对象
w = QWidget()
# 设置窗体大小
w.resize(500, 500)

# 设置样式
w.layout = QVBoxLayout()
w.label = QLabel("Hello World!")
w.label.setStyleSheet("font-size:25px;margin-left:155px;")
w.setWindowTitle("PyQt5 窗口")
w.layout.addWidget(w.label)
w.setLayout(w.layout)

# 显示窗体
w.show()
# 运行程序
sys.exit(app.exec_())
```

结果如下



![图片](https://mmbiz.qpic.cn/mmbiz_png/y0SBuxfLhakK1ZcBmkgK0AlfzU2rOFCefibXnhrHpn4ic9NibuqlIFyJjJ5F5XEbbIgeVmIlSo3gjPJ1QMRBg9cug/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



文档地址：

*https://riverbankcomputing.com/software/pyqt/intro*

教程链接：

*https://www.guru99.com/pyqt-tutorial.html*



### 二、Tkinter

Tkinter是Python中最受欢迎的GUI库之一。由于它简单易学的语法，成为GUI开发初学者的首选之一。

Tkinter提供了各种小部件，例如标签，按钮，文本字段，复选框和滚动按钮等。

支持Grid(网格)布局，由于我们的程序大多数都是矩形显示，这样即使是复杂的设计，开发起来也变得简单些。 

```python
# 安装tkinter
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tkinter
```

下面使用Tkinter设计一个BMI计算器。

以重量和高度作为输入，并在弹出框中返回BMI系数作为输出。

```
from tkinter import *
from tkinter import messagebox

def get_height():
    # 获取身高数据(cm)
    height = float(ENTRY2.get())
    return height

def get_weight():
    # 获取体重数据(kg)
    weight = float(ENTRY1.get())
    return weight

def calculate_bmi():
    # 计算BMI系数
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        messagebox.showinfo("提示", "请输入有效的身高数据!!")
    except ValueError:
        messagebox.showinfo("提示", "请输入有效的数据!")
    else:
        messagebox.showinfo("你的BMI系数是: ", bmi)

if __name__ == '__main__':
    # 实例化object，建立窗口TOP
    TOP = Tk()
    TOP.bind("<Return>", calculate_bmi)
    # 设定窗口的大小(长 * 宽)
    TOP.geometry("400x400")
    # 窗口背景颜色
    TOP.configure(background="#8c52ff")
    # 窗口标题
    TOP.title("BMI 计算器")
    TOP.resizable(width=False, height=False)
    LABLE = Label(TOP, bg="#8c52ff", fg="#ffffff", text="欢迎使用 BMI 计算器", font=("Helvetica", 15, "bold"), pady=10)
    LABLE.place(x=55, y=0)
    LABLE1 = Label(TOP, bg="#ffffff", text="输入体重(单位：kg):", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE1.place(x=55, y=60)
    ENTRY1 = Entry(TOP, bd=8, width=10, font="Roboto 11")
    ENTRY1.place(x=240, y=60)
    LABLE2 = Label(TOP, bg="#ffffff", text="输入身高(单位：cm):", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE2.place(x=55, y=121)
    ENTRY2 = Entry(TOP, bd=8, width=10, font="Roboto 11")
    ENTRY2.place(x=240, y=121)
    BUTTON = Button(bg="#000000", fg='#ffffff', bd=12, text="BMI", padx=33, pady=10, command=calculate_bmi,
                    font=("Helvetica", 20, "bold"))
    BUTTON.grid(row=5, column=0, sticky=W)
    BUTTON.place(x=115, y=250)
    TOP.mainloop()
```

界面如下。

![图片](https://mmbiz.qpic.cn/mmbiz_png/y0SBuxfLhakzVWMoE185VacLWxibkbKL0h5B228DxkruHtLHx1RSMHRQTD0kEkAbxEKNVr69zzTW98Sybm9jSMQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

当没有数据时，点击BMI按钮，会有与之对应的提示。

下面我们使用正确的数据，来看看结果。

![图片](https://mmbiz.qpic.cn/mmbiz_png/y0SBuxfLhakzVWMoE185VacLWxibkbKL0c1qhqCGg91w8miayYQZE9mhWyXxEqZnZCLquHibyY07jC16ibvPtBwtGg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

使用起来感觉还是不错的。



### 三、Kivy

Kivy是另一个开源的Python库，最大的优点就是可以快速地编写**移动应用程序**(手机)。

Kivy可以在不同的平台上运行，包括Windows、Mac OS、Linux、Android、iOS和树莓派。

此外也是免费使用的，获得了MIT许可。

```
# 安装kivy
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple kivy
```

一个基于Kivy的Hello World窗口。

```
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text=" Hello Kivy World ")

TestApp().run()
```

结果如下。

![图片](https://mmbiz.qpic.cn/mmbiz_png/y0SBuxfLhakK1ZcBmkgK0AlfzU2rOFCe4rhWG0MpaKkVhoUBGNGIGgOVKwO6f0S3WGCVfRyLWpKLG8XicDpCjaQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



### 四、wxPython

wxPython是一个跨平台GUI的Python库，可轻松创建功能强大稳定的GUI，毕竟是用C++编写的～

目前，支持Windows，Mac OS X，macOS和Linux。

使用wxPython创建的应用程序(GUI)在所有平台上都具有原生外观。

```
# 安装wxPython
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple wxPython
```

下面使用wxPython创建一个基本的GUI示例。

```
import wx

myapp = wx.App()
init_frame = wx.Frame(parent=None, title='WxPython 窗口')

init_frame.Show()
myapp.MainLoop()
```

结果如下。

![图片](https://mmbiz.qpic.cn/mmbiz_png/y0SBuxfLhakzVWMoE185VacLWxibkbKL0jn2iczicibd8vlNliakzkWyufJRxvUzgFqvSrFNIoCrrSnoM161d5fg89A/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



文档链接：*https://www.wxpython.org/*



### 五、PySimpleGUI

PySimpleGUI也是基于Python的GUI框架。可以轻松制作自定义的GUI。

采用了四种最流行的GUI框架QT、Tkinter、WxPython和Remi，能够实现大多数样例代码，**降低了学习难度**。

Remi将应用程序的界面转换为HTML，以便在Web浏览器中呈现。

```
# 安装PySimpleGUI
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PySimpleGUI
```

下面是一个简单的案例。

```
import PySimpleGUI as sg

layout = [[sg.Text("测试 PySimpleGUI")], [sg.Button("OK")]]
window = sg.Window("样例", layout)
while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break
window.close()
```

结果如下。

![图片](https://mmbiz.qpic.cn/mmbiz_png/y0SBuxfLhakzVWMoE185VacLWxibkbKL0iaI3GR7cMoOYSOiaL7ebnaiaFsVaHbIYVpBibrpiaycPMSB90ljGnMPeKfQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

点击OK按钮，窗口消失。



### 六、PyGUI

PyGUI是一个以简单API而闻名的GUI框架，减少Python应用与平台底层GUI之间的代码量。

轻量级的API，可以让你的应用程序运行起来更流畅，更快速。

同时还开源代码，跨平台项目。目前可在基于Unix的系统，Windows和Mac OS上运行。

Python2和Python3，都是可以支持的。

文档地址：

*https://www.cosc.canterbury.ac.nz/greg.ewing/python_gui/*

教程链接：

*https://realpython.com/pysimplegui-python/*



### 七、 Pyforms

Pyforms是用于开发GUI应用程序的一个跨平台框架。

![图片](https://mmbiz.qpic.cn/mmbiz_png/y0SBuxfLhakzVWMoE185VacLWxibkbKL04Z5FZMd6G3Bp2XpPwUemvzwGSQx2O9jcxakibXqy7uYpbDpaiaB4U2lQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

Pyforms是一个Python2.7/3.x跨环境图形应用开发框架，模块化和代码复用可以节省大量工作。

允许应用程序在桌面，Web和终端上运行，无需修改代码。

```
# 安装PyFroms
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PyFroms
```

文档地址：*https://pyforms.readthedocs.io/en/v4/*