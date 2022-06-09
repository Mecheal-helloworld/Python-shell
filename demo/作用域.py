import my_tools
import builtins
b = 1
def func():
    b = 1
    a = b
    print(a)

def func2():
    print(b)

def func1():
    nonlocal b
    b = 1
    def func2():
        def func3():
            b = 100
            print(b)
        func3()
        print(b)
    func2()
    print(b)

'''
builtins.__dict__['a'] = func1
a = 2
print(a)
list1 = my_tools.str2list("[1,2,3]")
func1()
b = b + 1
print(b)
'''

func1()
print(b)