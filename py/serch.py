#coding:utf-8

import json
import redis
import time
import requests
session = requests.session()
import logging.handlers
import pickle
import sys
import re
import datetime
from bs4 import BeautifulSoup
from imp import reload


import sys
reload(sys)

import datetime
# 生成一年的日期
def dateRange(start, end, step=1, format="%Y-%m-%d"):
    strptime, strftime = datetime.datetime.strptime, datetime.datetime.strftime
    days = (strptime(end, format) - strptime(start, format)).days
    return [strftime(strptime(start, format) + datetime.timedelta(i), format) for i in range(0, days, step)]




def spider():

    date_list = dateRange("2017-01-01", "2018-01-06")[::-1]
    print(date_list)
    for date in date_list:
        for page in range(1,5):
            #组合url
            url = "http://roll.mil.news.sina.com.cn/col/zgjq/" + str(date)+"_"+ str(page) +".shtml"
            # 伪装请求头
            headers = {

                "Host":"roll.mil.news.sina.com.cn",
              
                "Cache-Control":"max-age=0",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
              
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language":"zh-CN,zh;q=0.8",
                "If-Modified-Since":"Sat, 06 Jan 2018 09:57:24 GMT",

            }

            result = session.get(url=url,headers=headers).content
            #编码格式是 gb2312，使用BeautifulSoup解决编码格式
            soup = BeautifulSoup(result,'html.parser')
            #找到新闻列表
            result_div = soup.find_all('div',attrs={"class":"fixList"})[0]
            #去下换行
            result_replace = str(result_div).replace('\n','').replace('\r','').replace('\t','')
            #正则匹配信息
            result_list = re.findall('<li>(.*?)</li>',result_replace)

            for i in result_list:
                #匹配出来新闻 url， name，time

                news_url = re.findall('<a href="(.*?)" target=',i)[0]
                news_name = re.findall('target="_blank">(.*?)</a>',i)[0]
                news_time = re.findall('<span class="time">\((.*?)\)</span>',i)[0]
                news = re.findall('<div class="article" id="article">(.*?)</div>',i)
                print(news_url)
                print(news_name)
                print(news_time)
                print(news)
spider()