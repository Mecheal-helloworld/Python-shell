#导入需要使用到的数据模块
import pandas as pd
import pymysql
"""
#读入数据
#filepath = 'E:\_DataSet\catering_sale.xls'
#data = pd.read_excel(filepath)

#建立数据库连接
db = pymysql.connect('localhost','news_event','news_event','military_events')
#获取游标对象
cursor = db.cursor()
#创建数据表，如果数据表已经存在，注意主键不要重复，否则出错
try:
    cursor.execute('create table news(newsID int primary key,newsTime datetime, url VARCHAR(50))')
    cursor.execute('create table weaponSentence(SentenceID int primary key,newsID int,weaponName VARCHAR(20),SentenceContent Varchar(500))')
    cursor.execute('create table conflictEvent(conflictEventID int primary key,conflictEventTime datetime,conflictEventLocation VARCHAR(20),activeSubject VARCHAR(20),sufferSubject VARCHAR(20),damageSubject VARCHAR(20),SentenceID int)')
    cursor.execute('create table practiceEvent(practiceEventID int primary key,practiceEventTime datetime,practiceEventLocation VARCHAR(20),practiceWeapon VARCHAR(20),practiceSubject VARCHAR(20),SentenceID int)')
    cursor.execute('create table conflictEvent(soleConflictEventID int primary key,conflictEventTime datetime,conflictEventLocation VARCHAR(20),activeSubject VARCHAR(20),sufferSubject VARCHAR(20) ,damageSubject VARCHAR(20),conflictEventID int)')
    cursor.execute('create table practiceEvent(solePracticeEventID int primary key,practiceEventTime datetime,practiceEventLocation VARCHAR(20),practiceWeapon VARCHAR(20),practiceSubject VARCHAR(20),SentenceID int)')
    cursor.execute('create table weapon(weaponID int primary key,weaponName VARCHAR(20),weaponClass VARCHAR(20),weaponSClass VARCHAR(20))')
except:
    print('数据库已存在！')

#插入数据语句
"""
"""
#query = '''insert into catering_sale (num, date, sale) values (%s,%s,%s)'''

#迭代读取每行数据
#values中元素有个类型的强制转换，否则会出错的
#应该会有其他更合适的方式，可以进一步了解
for r in range(0, len(data)):
    num = data.ix[r,0]
    date = data.ix[r,1]
    sale = data.ix[r,2]
    values = (int(num), str(date), float(sale))
    cursor.execute(query, values)

#关闭游标，提交，关闭数据库连接
#如果没有这些关闭操作，执行后在数据库中查看不到数据
cursor.close()
db.commit()
db.close()
#重新建立数据库连接
db = pymysql.connect('localhost','root','1234','python_anylysis')
cursor = db.cursor()
#查询数据库并打印内容
cursor.execute('''select * from news''')
results = cursor.fetchall()
for row in results:
    print(row)
#关闭
"""
"""
cursor.close()
db.commit()
db.close()
"""
  #建立数据库连接
db = pymysql.connect('localhost','news_event','news_event','military_events')
  #获取游标对象
cursor = db.cursor()
def sqlin(weaClass,weaSClass,weaName,weaCountry):
  query = '''insert into weapon(weaponID,weaponName,weaponClass,weaponSClass,weaponCountry) values (null,%s,%s,%s,%s)'''
  values = (str(weaName),str(weaClass), str(weaSClass),str(weaCountry))
  cursor.execute(query, values)
  #关闭
sqlin("舰船舰艇","航空母舰","Q5J—强击教练机","中国")
#sqlin("舰船舰艇","航空母舰","Q5J强击教练机","中国")
cursor.close()
db.commit()
db.close()