import os
import sys
import re
import json
try:
  from xlrd import open_workbook
except:
  os.system(r"pip install xlrd")
try:
  from xlutils.copy import copy
except:
  os.system(r"pip install xlutils")
try:
  import xlwt
except:
  os.system(r"pip install xlwt")
def GetDesktopPath():
  return os.path.join(os.path.expanduser("~"), 'Desktop')
def Get_twitter_name(got):
  if got=="yes":
    return ["chenweijian2011"]
  if got=="no":
    names=input('请输入文件名(xx,xx):')
    name=names.split(",")
    return name
def sort(i,path,file_name):
  with open(path+"\\"+file_name+'.json','r',encoding='utf-8') as f:
    load_f=json.load(f)
    rb = open_workbook(path+"\\"+'twitter.xls')
    rs = rb.sheet_by_index(0)
    wb = copy(rb)
    ws = wb.get_sheet(0)
    for loadf in load_f:
      timestamp=loadf["timestamp"]
      if timestamp<='2019-07-23T15:59:59':
        continue
      i+=1
      ws.write(i,0,i)
      ws.write(i,4,timestamp)
      hashtags=loadf["hashtags"]
      #ws.write(i,8,hashtags)
      is_replied=loadf["is_replied"]
      #ws.write(i,15,is_replied)
      is_reply_to=loadf["is_reply_to"]
      #ws.write(i,16,is_reply_to)

      likes=loadf["likes"]
      ws.write(i,7,likes)

      links=loadf["links"]
      #ws.write(i,14,links)

      parent_tweet_id=loadf["parent_tweet_id"]

      replies=loadf["replies"]
      ws.write(i,8,replies)

      reply_to_users=loadf["reply_to_users"]
      #a=""
      #for user in reply_to_users:
        #a+=user['screen_name']+","
      #a=a.strip(',')
      #ws.write(i,10,a)
      #print(type(reply_to_users))
      #try:
        #ws.write(i,17,reply_to_users)
      #except:
        #wb.write(i,17,"can't write!")
      retweets=loadf["retweets"]
      ws.write(i,9,retweets)

      screen_name=loadf["screen_name"]
      ws.write(i,2,screen_name)

      text=loadf["text"]
      ws.write(i,5,text)

      tweet_id=loadf["tweet_id"]
      tweet_url=loadf["tweet_url"]
      user_id=loadf["user_id"]
      username=loadf["username"]
      ws.write(i,3,username)
      
      print("已得到第"+str(i)+"次发言")
  wb.save(path+"\\"+'twitter.xls')
  f.close()
  return i
def scraper(path,names):
  for name in names:
    print(name)
    os.system(r"cd "+path)
    print(path)
    try:
      #twitterscraper @wenyunchao --user  -bd 2020-06-26 -ed 2020-06-29 -o @wenyunchao.json
      os.system(r"twitterscraper "+name+" --user  -bd 2020-03-01 -ed 2020-05-25 -o "+name+".json")
    except:
      os.system(r"pip install twitterscraper")
      os.system(r"twitterscraper "+name+" --user  -bd 2020-03-01 -ed 2020-05-25 -o "+path+"\\"+name+".json")
def cin(check):
  if check=="yes":
    path=GetDesktopPath()
    return path
  if check=="no":
    path=input("请输入您希望的路径:")
    return path
def main():
  check=input("Use default path?[yes/no]:")
  path=cin(check)
  print(path)
  judge=input("Is information obtained?[yes/no]:")
  got=input("Use default names?[yes/no]:")
  twitter_names=Get_twitter_name(got)
  #twitter_names="test","test2"
  i=0
  if judge=="no":
    scraper(path,twitter_names)
  workbook=xlwt.Workbook(path+"\\"+'twitter.xls')
  workbook.add_sheet("sheet1")
  workbook.add_sheet("sheet2")
  workbook.add_sheet("sheet3")
  workbook.save(path+"\\"+'twitter.xls')
  rb = open_workbook(path+"\\"+'twitter.xls')
  rs = rb.sheet_by_index(0)
  wb = copy(rb)
  ws = wb.get_sheet(0)
  ws.write(0, 0, '信息编号')
  ws.write(0, 1, '姓名编号')
  ws.write(0, 2, '用户名')
  ws.write(0, 3, '账号')
  ws.write(0, 4, '发言时间')
  ws.write(0, 5, '发言信息原始文本')
  ws.write(0, 6, '对应的中文')
  #ws.write(0, 7, '发帖图片')
  ws.write(0, 8, '评论数')
  ws.write(0, 7, '点赞数')
  ws.write(0, 10, '转推账号')
  ws.write(0, 11, '情感态度')
  ws.write(0, 9, '被转发数')
  ws.write(0,12,'关联话题编号')
  wb.save(path+"\\"+'twitter.xls')
  for name in twitter_names:
    i=sort(i,path,name)
  rb = open_workbook(path+"\\"+'twitter.xls')
  rs = rb.sheet_by_index(0)
  nrows=rs.nrows
  ncols=rs.ncols
  print(nrows)
  wb=copy(rb)
  ws=wb.get_sheet(1)
  for i in range(nrows):
    for j in range(ncols):
      if i==0 or j==0:
        ws.write(i,j,rs.cell_value(i,j))
      else:
        ws.write(i,j,rs.cell_value(nrows-i,j))
  wb.save(path+"\\"+'twitter.xls')
main()