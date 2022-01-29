import os
import time
try:
  from bs4 import BeautifulSoup
except:
  os.system(r"pip install bs4")
  from bs4 import BeautifulSoup
desktop=os.path.join(os.path.expanduser("~"), 'Desktop')
import sys
sys.path.append(desktop)
import MyTools
#################定义播放函数################
def auto_study(url,pos,acc,pw):
  #启动IE浏览器
  browser = MyTools.creat_browser('ie')
  time.sleep(1)
  browser.get(url)
  browser.maximize_window()
  time.sleep(1)
  now_url=browser.current_url
  print(now_url)
  if(now_url!=url):
    #执行js
    time.sleep(1)
    js="document.getElementById('phone').value='"+acc+"';"
    browser.execute_script(js)
    time.sleep(1)
    js="document.getElementById('pwd').value='"+pw+"';"
    browser.execute_script(js)
    time.sleep(1)
    js = "loginByPhoneAndPwd();"
    browser.execute_script(js)
    time.sleep(1)
  if(pos=='studentcourse'):
    ahref=browser.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[3]/div[3]/div[3]/h3/a').get_attribute("href")
    print(ahref)
    browser.get(ahref)
    #browser.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[3]/div[1]/div/h3/span[3]/a').click()
    time.sleep(1)
  page=browser.page_source
  page=BeautifulSoup(page,"html.parser")
  jslist=[]
  for item in page.find_all("div"): 
    try:
      if(item['class']==['ncells']):
        signlist=item.select_one('span.roundpointStudent.orange01.a002.jobCount')
        print(signlist)
        if not signlist is None :
          for its in item.find_all("a"):
            jslist.append(its.get("href"))
    except:
      continue
  sourceUrl="https://mooc1-2.chaoxing.com"
  print(jslist)
  for ajs in jslist:
    browser.execute_script(ajs)
    nowpage=browser.page_source
    nowpage=BeautifulSoup(nowpage,"html.parser")
    anotherBrowser = MyTools.creat_browser('ie')
    for item in nowpage.find_all("iframe"):
      iframeUrl=sourceUrl+item.get("src")
      anotherBrowser.get(iframeUrl)
      anotherBrowser.maximize_window()
      nowurl=anotherBrowser.current_url
      if(nowurl!=iframeUrl):
      #执行js
        time.sleep(1)
        js="document.getElementById('phone').value='"+acc+"';"
        anotherBrowser.execute_script(js)
        time.sleep(1)
        js="document.getElementById('pwd').value='"+pw+"';"
        anotherBrowser.execute_script(js)
        time.sleep(1)
        js = "loginByPhoneAndPwd();"
        anotherBrowser.execute_script(js)
        time.sleep(1)
      iframes=[]
      newpage=anotherBrowser.page_source
      newpage=BeautifulSoup(newpage,"html.parser")
      for items in newpage.find_all('p'):
        iframeSign1=items.select_one('div.ans-attach-ct.ans-job-finished')
        iframeSign2=items.select_one('div.ans-attach-ct')
        iframeSign3=items.select_one('div.ans-job-icon')
        if not iframeSign1 is None :
          iframes.append(0)
        elif not iframeSign2 is None :
          if not iframeSign3 is None :
            iframes.append(1)
          else:
            iframes.append(0)
      print(iframes)
      for i in range(len(iframes)):
        iiframe=anotherBrowser.find_elements_by_tag_name("iframe")[i]
        anotherBrowser.switch_to.frame(iiframe)
        anotherBrowser.find_element_by_xpath('//*[@id="video"]/button').click()
        time.sleep(1)
        if(iframes[i]==1):
          timeLength=anotherBrowser.find_element_by_xpath('//*[@id="video"]/div[5]/div[4]/span[2]').text
          time1=0
          times=timeLength.split(':')
          print("这个视频需要用时：","")
          for t in times:
            time1=time1*60+int(t)
          print(time1+2,"")
          print("秒")
          time.sleep(time1+2)
        anotherBrowser.switch_to.default_content()
    MyTools.quit_browser(anotherBrowser)
  print("hhh")
  time.sleep(1)
  #关闭Chrome浏览器
  MyTools.quit_browser(browser)
#################获取网址################
print("请输入课程网址：")
print("例如：https://mooc1-2.chaoxing.com/mycourse/studentcourse?courseId=216095483&clazzid=35693304&enc=45fceb40a17f2cd7fae1f9b0be0be66b&cpi=75292093&vc=1")
for i in range(3):
  ustr=input("url: ")
  urls=ustr.split('/')
  postion=urls[4]
  postions=postion.split('?')
  print(len(postions))
  if(urls[3]!='mycourse' or len(postions)==1):
    print("输入的链接格式不正确，请输入完整url，包括'?'后的后缀！")
    lasttimes=str(2-i)
    print("剩余是输入次数"+lasttimes+"次")
    continue
  if(postions[0]=='studentcourse' or postions[0]=='studentstudy'):
    acc="19852858105"#input("请输入手机号：")
    pw="96242436946lo."#input("请输入密码：")
    #try:
    auto_study(ustr,postions[0],acc,pw)
    #except:
    print("发生了一些意料之外的错误")
    try:
      auto_study(ustr,postions[0],acc,pw)
    except:
      print("发生了一些意料之外的错误")
    break
  else:
    print("输入的链接格式不正确，请输入完整url，包括'?'后的后缀！")
    lasttimes=str(2-i)
    print("剩余是输入次数"+lasttimes+"次")
    continue
###############结束程序####################
print("恭喜您，已经看完了所有的课程，改程序将在10s后关闭！")
time.sleep(10)