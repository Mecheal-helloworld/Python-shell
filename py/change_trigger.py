import json
import os
import jieba
import jieba.posseg as pseg

remove_triggers = []
find_triggers = []
weapon_dicts = []
country_dicts = []
other_dicts = []
sentence_label = []

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


def get_triggers_in_seq(sentence, trigger, part_of_speech):
    trigger_length = len(trigger)
    if trigger_length==0 :
        print("error")
        return []
    if trigger not in sentence:
        print("error")
        return []
    mylist = sentence.split(trigger)
    num = len(mylist)
    rtn_triggers = []
    offset = 0
    for i in range(num-1):
        offset = offset + len(mylist[i])
        if part_of_speech == "x":
            rtn_triggers.append({"text": trigger,"offset": offset, "length": trigger_length})
        else:
            add_sign = True
            #print(trigger + " " + part_of_speech)
            for index in range(offset, offset + trigger_length):
                if (sentence_label[index] != part_of_speech) and (sentence_label[index] != "x"):
                    add_sign = False
                    break
            if add_sign:
                rtn_triggers.append({"text": trigger,"offset": offset, "length": trigger_length})
        offset += trigger_length
    return rtn_triggers


def get_remove_triggers():
    f = open("C:/Users/ASUS/Desktop/remove_triggers.txt", "r", encoding="utf-8")
    triggers = f.readlines()
    f.close()
    for trigger in triggers:
        trigger = trigger.strip("\n").split("	")[0]
        if trigger == "":
            continue
        if trigger not in remove_triggers:
            remove_triggers.append(trigger)


def get_weapons():
    f = open("C:/Users/ASUS/Desktop/weapons.txt", "r", encoding="utf-8")
    weapons = f.readlines()
    f.close()
    for weapon in weapons:
        if weapon == "":
            continue
        names = weapon.strip("\n").split(",,,")
        for name in names[1:-1]:
            name = name.strip(" ")
            if name == "":
                continue
            one_names = name.split(";")
            for one_name in one_names:
                one_name = one_name.strip(" ")
                if (one_name not in weapon_dicts) and (one_name != "") and (len(one_name) <= 10):
                    weapon_dicts.append(one_name)
        country = names[-1].strip(" ")
        if country == "":
            continue
        one_names = country.split(";")
        for one_name in one_names:
            one_name = one_name.strip(" ")
            if (one_name not in country_dicts) and (one_name != "") and (len(one_name) <= 10):
                country_dicts.append(one_name)


def get_others():
    f = open("C:/Users/ASUS/Desktop/others.txt", "r", encoding="utf-8")
    names = f.readlines()
    f.close()
    for name in names:
        name = name.strip("\n")
        if name == "":
            continue
        if name not in other_dicts:
            other_dicts.append(name)


def get_find_triggers():
    f = open("C:/Users/ASUS/Desktop/standard_triggers.txt", "r", encoding="utf-8")
    triggers = f.readlines()
    global find_triggers
    f.close()
    for trigger in triggers:
        line = trigger.strip("\n").split("	")
        my_trigger = line[0]
        part_of_speech = line[1]
        freq = 1
        if len(line) == 3 and line[2] != "":
            freq = int(line[2])
        if my_trigger == "":
            continue
        if trigger not in find_triggers:
            if part_of_speech == "名词":
                find_triggers.append((my_trigger, "n",freq))
            elif part_of_speech == "动词":
                find_triggers.append((my_trigger, "v",freq))
            else:
                find_triggers.append((my_trigger, "x",freq))
    find_triggers = sorted(find_triggers, key = lambda x:(len(x[0]),x[2]), reverse=True)
    for word,tag,freq in find_triggers:
        jieba.add_word(word, freq)


def change(fileName):
    f = open(fileName+".json", "r", encoding="utf-8")
    examples = json.load(f)
    example_index = 0
    f.close()
    f1 = open("C:/Users/ASUS/Desktop/data.txt", "w+", encoding="utf-8")
    global sentence_label
    my_examples = []
    for example in examples:
        my_example = {}
        sentence = example["sentence"]
        sentence_label = []
        print(sentence)
        f1.write(sentence + "\n")
        sentence_token = [0] * len(sentence)
        seq_words = pseg.cut(sentence)
        for seq_word in seq_words:
            #print(seq_word.word+str(seq_word.flag))
            for char_i in seq_word.word:
                #print(char_i+" "+str(seq_word.flag))
                sentence_label.append(seq_word.flag)
        my_example["sentence"] = sentence
        my_triggers = []
        my_events = []
        events = example["events"]
        empty = {"text": "","offset": 0, "length": 0}
        arguments = example["arguments"]
        for event in events:
            trigger = event["trigger"]
            text = trigger["text"]
            if text in remove_triggers:
                continue
            start_offset = trigger["offset"]
            end_offset = start_offset + trigger["length"]
            for index in range(start_offset, end_offset):
                sentence_token[index] = 1
            my_events.append(event)
        for find_trigger, part_of_speech,freq in find_triggers:
            if find_trigger in sentence:
                #print(find_trigger)
                triggers_in = get_triggers_in_seq(sentence, find_trigger, part_of_speech)
                #print(sentence_token)
                #print(triggers_in)
                for inner_trigger in triggers_in:
                    add_sign = True
                    now_trigger_start = inner_trigger["offset"]
                    now_trigger_end = now_trigger_start + inner_trigger["length"]
                    for index in range(now_trigger_start, now_trigger_end):
                        if sentence_token[index] == 1:
                            add_sign = False
                            break
                    if add_sign:
                        #print(inner_trigger)
                        start_offset = inner_trigger["offset"]
                        end_offset = start_offset + inner_trigger["length"]
                        for index in range(start_offset, end_offset):
                            sentence_token[index] = 1
                        my_events.append({"trigger": inner_trigger, "subject": empty, "object": empty})
        my_example["events"] = my_events
        my_example["arguments"] = example["arguments"]
        my_examples.append(my_example)
        example_index += 1
        for event in my_events:
            print(event["trigger"])
            f1.write(str(event["trigger"]) + "\n")
        if example_index == 669*7:
            f = open(fileName+"_train.json", "w+", encoding="utf-8")
            json.dump(my_examples,f)
            f.close()
            my_examples = []
        #print(my_events)
    print(len(my_examples))
    f = open(fileName+"_eval.json", "w+", encoding="utf-8")
    json.dump(my_examples,f)
    f.close()
    f1.close()


if __name__ == "__main__":
    get_find_triggers()
    get_remove_triggers()
    get_weapons()
    get_others()
    for weapon in weapon_dicts:
        print(weapon)
    for weapon in country_dicts:
        print(weapon)
    for other in other_dicts:
        print(other)
    '''
    f = open("C:/Users/ASUS/Desktop/standard_triggers__.txt", "w+", encoding="utf-8")
    for find_trigger in find_triggers:
        f.write(str(find_trigger[0])+"	"+str(find_trigger[1])+"	"+str(find_trigger[2]) + "\n")
    f.close()
    '''
    '''
    print(find_triggers)
    for trigger_in in find_triggers:
        if trigger_in[0] == "交付使用":
            print("yes")
    '''
    #change("E:/Rootpath/dataset/test/data")
'''
    files = file_name("/usr/local/Rootpath/data/mark/json")
    for file in files:
        print(file)
        change("/usr/local/Rootpath/data/mark/json" + file)
'''
