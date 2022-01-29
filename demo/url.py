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
  if(postions[0]=='studentcourse'):
    break
  elif(postions[0]=='studentstudy'):
    import stydy_scrapper
    break
  else:
    print("输入的链接格式不正确，请输入完整url，包括'?'后的后缀！")
    lasttimes=str(2-i)
    print("剩余是输入次数"+lasttimes+"次")
    continue
str=input()