import urllib.request
import sys   #引用sys模块进来，并不是进行sys的第一次加载  
g=sys.getdefaultencoding()  ##调用setdefaultencoding函数
print(g)
str='https://www.w3cschool.cn/python/python-socket.html'
response = urllib.request.urlopen(str)
html = response.read() # html就是我们所请求的网页的源码
if g!='utf-8':
  code_of_html = html.decode('utf-8')
  print(code_of_html)
  html=code_of_html
f=open("南海事件.txt",mode='rb+')
f.write(html)
f.close()
