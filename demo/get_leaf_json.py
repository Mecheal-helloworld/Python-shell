import json
import copy

fd = open("C:\\Users\\ASUS\\Desktop\\1.txt","r",encoding="utf-8")
strs = fd.readlines()
for x in strs:
  print(x)
print(strs)
fd.close()