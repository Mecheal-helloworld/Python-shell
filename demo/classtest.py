import Tools
class people:
    #定义基本属性
    name = ''
    age = ''
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = '123456'
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = "father:"+ n
        self.age = "father:"+ a
        self._people__weight = "father:"+ w
    def people_func(self):
        print(self.name)
        print(self.age)
        print(self._people__weight)

class newPeople:
    #定义基本属性
    name = ''
    age = ''
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = '123456'
    #定义构造方法
    def __init__(self):
        pass
    def people_func(self):
        print(self.name)
        print(self.age)
        print(self._people__weight)
        b = 1
        def func():
            b = 1
 
#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        # 调用父类的构造函数
        people.__init__(self,n,a,w)# super(student,self).__init__(n,a,w)
        self.grade = g
    def student_func(self):
        print(self.name)
        print(self.age)
        print(self.grade)
        print(self.__weight)
    def __call__(self):
        print("callable")
    def __add__(self,a):
        print("add")
    def __pow__(self,a):
        print(a)
    def __setitem__(self,a,b):
        print(a)
        print(b)
    def __getitem__(self,a):
        return "111"
    def __repr__(self):
        return "object"
    def __len__(self):
        return 2
    def __truediv__(self,a):
        return self
    def __floordiv__(self,a):
        return self
    def __rfloordiv__(self,a):
        return self
b = 1
def func1():
    global b
    b = 1
    def func2():
        nonlocal b
        b = 1
        def func3():
            nonlocal b
            b = 1




p = people("w","12","123")
p._people__weight
q1 = student("w","12","123","12345")
q2 = student("w","12","123","12345")
p.people_func()
q1.people_func()
q1.student_func()

a:定义为内置命名空间变量
q1()
q3 = q1**2
q1[1] = 2
print(q1)
len(q1)
print(q1[1])
q3 = 0 // q1