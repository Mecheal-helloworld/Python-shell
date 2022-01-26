from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from lxml import etree
import os
import requests
import csv
desktop=os.path.join(os.path.expanduser("~"), 'Desktop')
import sys
sys.path.append(desktop)
import MyTools

#启动IE浏览器
browser = MyTools.creat_browser()



# 使用谷歌无头浏览器来加载动态js
def start_get(url,news_type):
        browser.get(url)
        time.sleep(1)
        for one in range(30):
            # 翻到页底
            js = "window.scrollTo(0,document.body.scrollHeight);"
            browser.execute_script(js)#('window.scrollTo(0,document.body.scrollHeight);')
            time.sleep(1)
         # 拿到页面源代码
        source = browser.page_source
        print(source)
        #parse_page(url,source,news_type)
 
# 对新闻列表页面进行解析
def parse_page(url,html,news_type):
    # 创建etree对象
    tree = etree.HTML(html)
    new_lst = tree.xpath('//ul[@id="recommend"]//a')
    for one_new in new_lst:
        title = one_new.xpath('.//h4/text()')[0]
        link = url + one_new.xpath('./@href')[0]
        try:
            write_in(title, link,news_type)
        except Exception as e:
            print(e)
   
# 将其写入到文件
def write_in(title, link,news_type):
    alist = []
    print('开始写入新闻:{}'.format(title))
    # response = requests.get(url=link)
    browser.get(link)
    sleep(1)
    # 再次翻页到底
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    # 拿到页面源代码
    source = browser.page_source
    #print(source)
    tree = etree.HTML(source)

    alist.append(news_type)
    # title = title.replace('?', '')
    alist.append(title)

    con_link = link
    alist.append(con_link)

    content_lst = tree.xpath('//section[@data-type="rtext"]/p')
    con = ''
    if content_lst:
        for one_content in content_lst:
            if one_content.text:
                con = con + '\n' + one_content.text.strip()
        alist.append(con)

        # post_time_source = tree.xpath('//div[@class="left-t"]')[0].text

        post_time = tree.xpath('//div[@class="metadata-info"]//p[@class="time"]')[0].text
        alist.append(post_time)

        post_source = tree.xpath('//div[@class="metadata-info"]//span[@class="source"]//a')
        if post_source:
            post_source=post_source[0].text
        else:
            post_source = tree.xpath('//div[@class="metadata-info"]//span[@class="source"]//span')[0].text
        alist.append(post_source)
         # 1. 创建文件对象
        f = open('C:/Users/ASUS/Desktop/环球网n.csv', 'a+', encoding='utf-8',newline='')
        # 2. 基于文件对象构建 csv写入对象
        csv_writer = csv.writer(f)
        #print(alist)
        csv_writer.writerow(alist)
        f.close()
if __name__ == '__main__':
    url = 'https://mil.huanqiu.com/world'#'https://mil.huanqiu.com/'
    news_type = "军事"
    #headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}
    start_get(url, news_type)
browser.quit()

