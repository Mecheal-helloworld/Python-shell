import json
import os

#dict_f = open("C:/Users/ASUS/Desktop/dict.txt", "a", encoding="utf-8-sig")


def get_files_of_path(file_dir):
    L=[] 
    for root,dirs, files in os.walk(file_dir):  
        for file in files:
            if os.path.splitext(file)[1]=='.json':
                L.append(os.path.join(file))
    return L


f2 = open("E:/Rootpath/data/mark/result.txt", "w+", encoding="utf-8")
def change(fileName):
    f = open(fileName+".json", "r", encoding="utf-8")
    examples = json.load(f)
    f.close()
    f2.write(fileName.split("/")[-1]+"、")
    trigger = []
    time = []
    location = []
    weapon = []
    country = []
    for idx, example in enumerate(examples):
        sentence = example["sentence"]
        print(sentence)
        f2.write(sentence)
        if idx == 0:
           f2.write("\n")
        events = example["events"]
        arguments = example["arguments"]
        times = arguments["time"]
        locs = arguments["loc"]
        weapons = arguments["weapon"]
        countrys = arguments["country"]
        for event in events:
            trigger.append(event["trigger"]["text"])
        for role in times:
            time.append(role["text"])
        for role in locs:
            location.append(role["text"])
        for role in weapons:
            weapon.append(role["text"])
        for role in countrys:
            country.append(role["text"])
    f2.write("\n")
    f2.write("触发词："+str(trigger) + "\n")
    f2.write("时间："+str(time) + "\n")
    f2.write("地点："+str(location) + "\n")
    f2.write("武器："+str(weapon) + "\n")
    f2.write("国家："+str(country) + "\n")
    f2.write("\n")
    f2.write("\n")


if __name__ == "__main__":
    change("E:/Rootpath/dataset/test/data")
    '''
    files = get_files_of_path("E:/Rootpath/data/mark/json")
    for file in files:
        print(file)
        change("E:/Rootpath/data/mark/json/" + file.split(".")[0])
    '''
    f2.close()
