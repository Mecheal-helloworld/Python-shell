import urllib.request
import sys   #引用sys模块进来，并不是进行sys的第一次加载
import os
import time
import gzip
from io import StringIO  #StringIO模块就是在内存中读写str
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
headers = {
    'User-Agent': user_agent
}


def GetDesktopPath():
  return os.path.join(os.path.expanduser("~"),'Desktop')  

g=sys.getdefaultencoding()  ##调用setdefaultencoding函数
def weapon_scraper():
  str='http://weapon.huanqiu.com/weaponlist/aircraft/list_1'
  request = urllib.request.Request(str,headers=headers)
  request.add_header('Accept-encoding', 'gzip') #添加头信息
  response = urllib.request.urlopen(request)
  if(response.info().get('Content-Encoding')=='gzip'):
    data = gzip.decompress(response.read())
    html=data.decode('utf-8')
  bs=BeautifulSoup(html,"html.parser")
  titles=[]
  values=[]
  num='1'
  for item in bs.find_all("div"): 
    try:
      if(item['class']==['select']):
        itess=item.find_all("ul")[0]
        ites=itess.find_all("li")[1]
        for ite in ites.find_all("a"):
          if(ite.get_text()=='不限'):
            continue
          link=[]
          link.append(ite.get_text())
          link.append(ite.get('href').split('?')[0])
          values.append(link)
      if(item['class']==['sideNav']):
        for it in item.find_all("a"):
          link=[]
          link.append(it.get_text())
          link.append(it.get('href').split('?')[0])
          titles.append(link)
      if(item['class']==['pages']):
        sign=0
        for its in item.find_all("a"):
          if(its.get_text()=='下一页'):
            break
          if(its.get_text()!='上一页'):
            num=its.get_text()
    except:
      continue
  print(num)
  print(values)
  print(titles)
weapon_scraper()