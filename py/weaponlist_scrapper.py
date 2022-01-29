import urllib.request
import sys   #引用sys模块进来，并不是进行sys的第一次加载
import os
import time
import gzip
from io import StringIO  #StringIO模块就是在内存中读写str
from bs4 import BeautifulSoup
import pymysql

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
headers = {
    'User-Agent': user_agent
}

def GetDesktopPath():
  return os.path.join(os.path.expanduser("~"),'Desktop')  
def pfile(str):
  path=GetDesktopPath()
  f=open(path+"/weaponlist.txt", 'a+',encoding='utf-8')
  t=f.write(str)
  f.close()
g=sys.getdefaultencoding()  ##调用setdefaultencoding函数
def url_scraper():
  str='http://weapon.huanqiu.com/weaponlist'
  request = urllib.request.Request(str)
  request.add_header('Accept-encoding', 'gzip') #添加头信息
  response = urllib.request.urlopen(request)
  if(response.info().get('Content-Encoding')=='gzip'):
    data = gzip.decompress(response.read())
    html=data.decode('utf-8')
  bs=BeautifulSoup(html,"html.parser")
  titles=[]
  for item in bs.find_all("div"): 
    try:
      if(item['class']==['sideNav']):
        for it in item.find_all("a"):
          link=[]
          link.append(it.get_text())
          link.append(it.get('href').split('?')[0])
          titles.append(link)
    except:
      continue
  return titles
def value_scraper(stru):
  str='http://weapon.huanqiu.com'+stru
  print(str)
  request = urllib.request.Request(str)
  request.add_header('Accept-encoding', 'gzip') #添加头信息
  response = urllib.request.urlopen(request)
  if(response.info().get('Content-Encoding')=='gzip'):
    data = gzip.decompress(response.read())
    html=data.decode('utf-8')
  bs=BeautifulSoup(html,"html.parser")
  values=[]
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
    except:
      continue
  return values
def num_scraper(strv):
  str='http://weapon.huanqiu.com'+strv
  print(str)
  request = urllib.request.Request(str)
  request.add_header('Accept-encoding', 'gzip') #添加头信息
  response = urllib.request.urlopen(request)
  if(response.info().get('Content-Encoding')=='gzip'):
    data = gzip.decompress(response.read())
    html=data.decode('utf-8')
  bs=BeautifulSoup(html,"html.parser")
  num='1'
  for item in bs.find_all("div"): 
    try:
      if(item['class']==['pages']):
        sign=0
        for its in item.find_all("a"):
          if(its.get_text()=='下一页'):
            break
          if(its.get_text()!='上一页'):
            num=its.get_text()
    except:
      continue
  return num
def weapon_scraper(strn):
  str='http://weapon.huanqiu.com'+strn
  print(str)
  request = urllib.request.Request(str,headers=headers)
  request.add_header('Accept-encoding', 'gzip') #添加头信息
  response = urllib.request.urlopen(request)
  if(response.info().get('Content-Encoding')=='gzip'):
    data = gzip.decompress(response.read())
    html=data.decode('utf-8')
  bs=BeautifulSoup(html,"html.parser")
  weaponNames=[]
  weaponCountrys=[]
  for item in bs.find_all("div"): 
    try:
      if(item['class']==['picList']):
          for its in item.find_all("li"): 
            for sit in its.find_all("span"):
              try:
                if(sit['class']==['name']):
                  pfile(sit.get_text()+"\n")
                  weaponNames.append(sit.get_text())
              except:
                continue
            for dit in its.find_all("div"):
              try:
                if(dit['class']==['country']):
                  pfile(dit.get_text()+"\n")
                  weaponCountrys.append(dit.get_text())
              except:
                continue
    except:
      continue
  return weaponNames,weaponCountrys
lists=url_scraper()
time.sleep(1)
print(lists)
#建立数据库连接
db = pymysql.connect('localhost','news_event','news_event','military_events')
#获取游标对象
cursor = db.cursor()
def sqlin(weaClass,weaSClass,weaName,weaCountry):
  query = '''insert into weapon(weaponID,weaponName,weaponClass,weaponSClass,weaponCountry) values (null,%s,%s,%s,%s)'''
  values = ( weaName, weaClass, weaSClass, weaCountry)
  cursor.execute(query, values)
for list in lists:
  pfile("@"+list[0]+"\n")
  vars=value_scraper(list[1])
  time.sleep(1)
  print(vars)
  for var in vars:
    pfile("["+var[0]+"]\n")
    number=int(num_scraper(var[1]))
    time.sleep(1)
    for i in range(number):
      weaponNames,weaponCountrys=weapon_scraper(var[1]+'_0_0_'+str(i+1))
      print(len(weaponNames),len(weaponCountrys))
      for weai in range(len(weaponNames)):
        print(weaponNames[weai],weaponCountrys[weai])
        sqlin(list[0],var[0],weaponNames[weai],weaponCountrys[weai])
      time.sleep(1)
#关闭
cursor.close()
db.commit()
db.close()
str=input()