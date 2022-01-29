
trigger_file = open("E:/Rootpath/resource/tmp.txt", "r", encoding="utf-8")
lines = trigger_file.readlines()
trigger_file.close()
trigger_class = {}
tmp_class = []
all_class = set()
for line in lines:
    trigger_ = line.strip().split("	")
    trigger = trigger_[0]
    tri_class = trigger_[2]
    tmp_class.append((tri_class,trigger))
    all_class.add(tri_class)
tmp_class.sort(key=lambda x:(x[1],x[0]))
for tmp_cls, tmp_tri in tmp_class:
    trigger_class[tmp_tri] = tmp_cls
for cls in all_class:
    cls_file = open("E:/Rootpath/resource/format/trigger/classes/"+cls+".txt", "w+", encoding="utf-8")
    cls_file.close()
trigger_file = open("E:/Rootpath/resource/format/trigger/Triggers.txt", "r", encoding="utf-8")
lines = trigger_file.readlines()
trigger_file.close()
cls_file = open("E:/Rootpath/resource/format/trigger/classes/unknown.txt", "w+", encoding="utf-8")
cls_file.close()
for line in lines:
    trigger = line.strip().split(" ")[0]
    cls = ""
    try: 
        cls = trigger_class[trigger]
    except:
        cls = "unknown"
        print(trigger)
    cls_file = open("E:/Rootpath/resource/format/trigger/classes/"+cls+".txt", "a", encoding="utf-8")
    cls_file.write(line)
    cls_file.close()

