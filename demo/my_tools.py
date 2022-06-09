import builtins
def str2list(format_str=""):
    print(a)
    rtn_str = format_str.strip("[]")
    rtn_strs = rtn_str.split(",")
    rtn_list = []
    for each_str in rtn_strs:
        #rtn_list.append(each_str.strip().strip("'\""))
        rtn_list.append(int(each_str.strip()))
    return rtn_list

# 第一种思路：转换成字符串，然后字符串处理： 12321 123321
def isCircle1(num):
    # 转换成字符串
    num_str = str(num)
    str1 = ""
    str_len = len(num_str)//2
    for i in range(str_len):
        str1 = str1 + num_str[str_len-1-i]
    print(str1)
    if str1 == num_str[len(num_str)-len(str1):]:
        return True
    else:
        return False


# 第二种思路：把每一位依次存到列表中，判断第i个数和第n-i个数是否相同12321
# 12321 = 1*10^4 + 2*10^3 + 3*10^2 + 2*10^1 + 1*10^0
# 0O765 = 7*8^2 + 6*8^1 + 5*8^0
# 对一个数对10取余就是最低位的数，整除就把最低位去掉
def isCircle2(num):
    # 转换成列表
    num_list = []
    while num:
        num_list.append(num%10)
        num = num // 10
    list_len = len(num_list)
    for i in range(list_len//2):
        if num_list[i] != num_list[list_len-1-i]:
            return False
    return True


def febo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return febo(n-1)+febo(n-2)


def simple(n):
    print("call:"+str(n))
    if n == 1:
        return 1
    sum = n + simple(n-1)
    print("return:"+str(n))
    return sum

a = 1
if __name__ == "__main__":
    a = 1
    print(simple(int(input())))
