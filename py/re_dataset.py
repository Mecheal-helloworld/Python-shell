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


def change(fileName):
    f = open(fileName, "r", encoding="utf-8")
    examples = json.load(f)
    f.close()
    my_examples = []
    for example in examples:
        my_example = {}
        sentence = example["sentence"]
        my_example["sentence"] = sentence
        my_events = []
        events = example["events"]
        for event in events:
            sign = True
            my_event = {}
            my_trigger = {}
            my_subject = {}
            my_object = {}
            trigger = event["trigger"]
            subject = event["subject"]
            object = event["object"]
            my_trigger["text"] = trigger["text"]
            my_trigger["offset"] = getOffset(sentence,trigger)
            my_trigger["length"] = 0 if trigger["length"] == "" else trigger["length"]
            my_subject["text"] = subject["text"]
            my_subject["offset"] = getOffset(sentence,subject)
            my_subject["length"] = 0 if subject["length"] == "" else subject["length"]
            my_object["text"] = object["text"]
            my_object["offset"] = getOffset(sentence,object)
            my_object["length"] = 0 if object["length"] == "" else object["length"]
            my_event["trigger"] = my_trigger
            my_event["subject"] = my_subject
            my_event["object"] = my_object
            my_events.append(my_event)
        my_example["events"] = my_events
        my_locs = []
        my_times = []
        my_countrys = []
        my_weapons = []
        my_arguments = {}
        arguments = example["arguments"]
        locs = arguments["loc"]
        times = arguments["time"]
        countrys = arguments["country"]
        weapons = arguments["weapon"]
        for role in locs:
            sign = True
            my_role = {}
            my_role["text"] = role["text"]
            my_role["offset"] = getOffset(sentence,role)
            my_role["length"] = 0 if role["length"] == "" else role["length"]
            my_locs.append(my_role)
        for role in times:
            sign = True
            my_role = {}
            my_role["text"] = role["text"]
            my_role["offset"] = getOffset(sentence,role)
            my_role["length"] = 0 if role["length"] == "" else role["length"]
            my_times.append(my_role)
        for role in countrys:
            sign = True
            my_role = {}
            my_role["text"] = role["text"]
            my_role["offset"] = getOffset(sentence,role)
            my_role["length"] = 0 if role["length"] == "" else role["length"]
            my_countrys.append(my_role)
        for role in weapons:
            sign = True
            my_role = {}
            my_role["text"] = role["text"]
            my_role["offset"] = getOffset(sentence,role)
            my_role["length"] = 0 if role["length"] == "" else role["length"]
            my_weapons.append(my_role)
        my_arguments["loc"] = my_locs
        my_arguments["time"] = my_times
        my_arguments["country"] = my_countrys
        my_arguments["weapon"] = my_weapons
        my_example["arguments"] = my_arguments
        #print(example)
        if sign:
            my_examples.append(my_example)
            #print(my_example)
    f = open(fileName, "w+", encoding="utf-8")
    json.dump(my_examples,f)
    f.close()


if __name__ == "__main__":
    change("E:/Rootpath/dataset/data.json")
