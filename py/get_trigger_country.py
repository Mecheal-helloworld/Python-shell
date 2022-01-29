import json
import os

def file_name(file_dir):
    L=[] 
    for root,dirs, files in os.walk(file_dir):  
        for file in files:
            if os.path.splitext(file)[1]=='.json':
                L.append(os.path.join(file))
    return L


def getOffset(sentence,item):
    if len(item["text"])==0 :
        return 0
    if item["text"] not in sentence:
        return -1
    mylist = sentence.split(item["text"])
    num = len(mylist)
    offset = 0
    for i in range(num-1):
        offset = offset + len(mylist[i])
    offset = offset + (num - 2) * len(item["text"])
    return offset


def write_labels(labels,name):
    f = open("E:/Rootpath/dataset/"+name+".txt", "w+", encoding="utf-8")
    for label in labels:
        f.write(label[0]+"     "+str(label[1]) + "\n")
    f.close()


def read_labels(fileName):
    f = open(fileName, "r", encoding="utf-8")
    examples = json.load(f)
    f.close()
    my_triggers = []
    my_times = []
    my_locs = []
    my_countrys = []
    my_weapons = []
    my_triggers_num = []
    my_times_num = []
    my_locs_num = []
    my_countrys_num = []
    my_weapons_num = []
    for example in examples:
        events = example["events"]
        for event in events:
            trigger = event["trigger"]
            text = trigger["text"]
            print(text+" ")
            sign = True
            for index, inner_trigger in enumerate(my_triggers):
                if text == inner_trigger:
                    my_triggers_num[index] += 1
                    sign = False
                    break
            if sign:
                my_triggers.append(text)
                my_triggers_num.append(1)
        arguments = example["arguments"]
        locs = arguments["loc"]
        times = arguments["time"]
        countrys = arguments["country"]
        weapons = arguments["weapon"]
        for role in locs:
            text = role["text"]
            sign = True
            for index, inner_loc in enumerate(my_locs):
                if text == inner_loc:
                    my_locs_num[index] += 1
                    sign = False
                    break
            if sign:
                my_locs.append(text)
                my_locs_num.append(1)
        for role in times:
            text = role["text"]
            sign = True
            for index, inner_time in enumerate(my_times):
                if text == inner_time:
                    my_times_num[index] += 1
                    sign = False
                    break
            if sign:
                my_times.append(text)
                my_times_num.append(1)
        for role in countrys:
            text = role["text"]
            sign = True
            for index, inner_country in enumerate(my_countrys):
                if text == inner_country:
                    my_countrys_num[index] += 1
                    sign = False
                    break
            if sign:
                my_countrys.append(text)
                my_countrys_num.append(1)
        for role in weapons:
            text = role["text"]
            sign = True
            for index, inner_weapon in enumerate(my_weapons):
                if text == inner_weapon:
                    my_weapons_num[index] += 1
                    sign = False
                    break
            if sign:
                my_weapons.append(text)
                my_weapons_num.append(1)
    print(my_triggers)
    print(my_times)
    print(my_locs)
    print(my_countrys)
    print(my_weapons)
    labels = []
    for index, label in enumerate(my_triggers):
        labels.append((label, my_triggers_num[index]))
    labels = sorted(labels, key=lambda x:x[0])
    labels = sorted(labels, key=lambda x:x[1], reverse=True)
    write_labels(labels, "all_triggers")
    labels = []
    for index, label in enumerate(my_locs):
        labels.append((label, my_locs_num[index]))
    labels = sorted(labels, key=lambda x:x[0])
    labels = sorted(labels, key=lambda x:x[1], reverse=True)
    write_labels(labels, "all_locs")
    labels = []
    for index, label in enumerate(my_times):
        labels.append((label, my_times_num[index]))
    labels = sorted(labels, key=lambda x:x[0])
    labels = sorted(labels, key=lambda x:x[1], reverse=True)
    write_labels(labels, "all_times")
    labels = []
    for index, label in enumerate(my_weapons):
        labels.append((label, my_weapons_num[index]))
    labels = sorted(labels, key=lambda x:x[0])
    labels = sorted(labels, key=lambda x:x[1], reverse=True)
    write_labels(labels, "all_weapons")
    labels = []
    for index, label in enumerate(my_countrys):
        labels.append((label, my_countrys_num[index]))
    labels = sorted(labels, key=lambda x:x[0])
    labels = sorted(labels, key=lambda x:x[1], reverse=True)
    write_labels(labels, "all_countrys")


if __name__ == "__main__":
    read_labels("E:/Rootpath/dataset/data.json")
