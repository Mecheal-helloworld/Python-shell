import json
import os
import jieba
import jieba.posseg as pseg
import wordseg

def check_in(sentence,role):
    start_ = role["offset"]
    end_ = start_ + role["length"]
    if role["text"] == sentence[start_:end_]:
        return True
    else:
        return False


def get_files_of_path(file_dir):
    L=[] 
    for root,dirs, files in os.walk(file_dir):  
        for file in files:
            if os.path.splitext(file)[1]=='.json':
                L.append(os.path.join(file))
    return L


def change(fileName):
    f = open(fileName+".json", "r", encoding="utf-8")
    examples = json.load(f)
    f.close()
    example_index = 0
    my_examples = []
    for example in examples:
        sentence = example["sentence"]
        print(sentence)
        events = example["events"]
        my_events = []
        for event in events:
            if check_in(sentence,event["trigger"]):
                my_events.append(event)
        arguments = example["arguments"]
        times = arguments["time"]
        my_times = []
        for role in times:
            if check_in(sentence,role):
                my_times.append(role)
        locs = arguments["loc"]
        my_locs = []
        for role in locs:
            if check_in(sentence,role):
                my_locs.append(role)
        weapons = arguments["weapon"]
        my_weapons = []
        for role in weapons:
            if check_in(sentence,role):
                my_weapons.append(role)
        countrys = arguments["country"]
        my_countrys = []
        for role in countrys:
            if check_in(sentence,role):
                my_countrys.append(role)
        example_index += 1
        my_arguments = {"time":my_times,"loc":my_locs,"weapon":my_weapons,"country":my_countrys}
        my_examples.append({"sentence": sentence, "events": my_events, "arguments": my_arguments})
        if example_index == 2638 * 7:
                f = open(fileName+"_train.json", "w+", encoding="utf-8")
                json.dump(my_examples,f)
                f.close()
                my_examples = []
    print(len(my_examples))
    f = open(fileName+"_eval.json", "w+", encoding="utf-8")
    json.dump(my_examples,f)
    f.close()


if __name__ == "__main__":
    change("E:/Rootpath/dataset/test/data")
'''
    files = file_name("E:/Rootpath/data/mark/json")
    for file in files:
        print(file)
        change("E:/Rootpath/data/mark/json" + file.split(".")[0])
'''
