.#bilibili弹幕抓取
import requests
import re
from bs4 import BeautifulSoup
import operator#排序
 
def getHTMLText(url):
    try:
        print("获取url中...")
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print("获取url完成")
        return r.text
    except:
        print("获取Url失败")
 
def parsePage(text):
    try:
        print("解析文本...")
        keyStr = re.findall(r'"cid":[\d]*',text)#B站有两种寻址方式，第二种多一些
        if not keyStr:#若列表为空，则等于“False”
            keyStr = re.findall(r'cid=[\d]*', text)
            key = eval(keyStr[0].split('=')[1])
        else:
            key = eval(keyStr[0].split(':')[1])
        commentUrl = 'https://comment.bilibili.com/' + str(key) + '.xml'  # 弹幕存储地址
        print(commentUrl)
        print("再一次")
        commentText=getHTMLText(commentUrl)
        soup = BeautifulSoup(commentText, "html.parser")
        soup2=BeautifulSoup(text,"html.parser")
        commentList={}
        title=soup2.find('h1').get_text().strip()#find()方法，获取文本，去掉空格
        for comment in soup.find_all('d'):
            time=float(comment.attrs['p'].split(',')[0])#tag.attrs（标签属性，字典类型）
            commentList[time]=comment.string
        newDict=sorted(commentList.items(),key=operator.itemgetter(0))#字典排序
        commentList=dict(newDict)
        print("解析文本完成")
        return commentList,title
    except:
        print("解析失败")
 
def float2time(f):
    timePlus=int(f)
    m=timePlus//60
    s=timePlus-m*60
    return str(m)+':'+str(s).zfill(2)
 
def ioFunc(commentList,title,root):
    print("写入文本中...")
    path = root + "/" + title + '.txt'
    print(path)
    f = open(path, 'w',encoding='utf-8')#windows默认gbk编码输出，与网络编码“utf-8”不符
    begin = "{}\n共有{}条弹幕\n".format(title, len(commentList))
    f.write(begin)
    ws = "{:7}\t{}\n".format('time', 'comment')
    f.write(ws)
    lastTime=0
    for time,string in commentList.items():#记得items()
        lastTime = float2time(time)
        ws = "{:7}\t{}\n".format(lastTime,string)
        f.write(ws)  # 手动换行
    f.close()
 
def main():
    av =input('Put in av number: ')  # 视频地址
    url=r"https://www.bilibili.com/video/av"+str(av)
    root = r"C:/Users/ASUS/Desktop"
    text=getHTMLText(url)
    commentList,title=parsePage(text)
    ioFunc(commentList, title, root)
    print("Finish.")
 
main()
