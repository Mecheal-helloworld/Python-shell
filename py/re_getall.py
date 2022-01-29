import json
import os

find_trigger_dicts = []
remove_trigger_dicts = []
find_weapon_dicts = []
remove_weapon_dicts = []
find_time_dicts = []
remove_time_dicts = []
find_location_dicts = []
remove_location_dicts = []
find_country_dicts = []
remove_country_dicts = []

other_dicts = []
find_dicts = []

def file_name(file_dir):
    L=[] 
    for root,dirs, files in os.walk(file_dir):  
        for file in files:
            if os.path.splitext(file)[1]=='.json':
                L.append(os.path.join(file))
    return L

all_examples = []

def get_remove_triggers():
    f = open("C:/Users/ASUS/Desktop/using/remove_triggers.txt", "r", encoding="utf-8")
    triggers = f.readlines()
    f.close()
    for trigger in triggers:
        trigger = trigger.strip("\n").split("	")[0].strip()
        if trigger == "":
            continue
        if trigger not in remove_trigger_dicts:
            remove_trigger_dicts.append(trigger)


def get_remove_weapons():
    f = open("C:/Users/ASUS/Desktop/using/remove_weapons.txt", "r", encoding="utf-8")
    weapons = f.readlines()
    f.close()
    for weapon in weapons:
        weapon = weapon.strip("\n").split("	")[0].strip()
        if weapon == "":
            continue
        if weapon not in remove_weapon_dicts:
            remove_weapon_dicts.append(weapon)


def get_remove_countrys():
    f = open("C:/Users/ASUS/Desktop/using/remove_countrys.txt", "r", encoding="utf-8")
    countrys = f.readlines()
    f.close()
    for country in countrys:
        country = country.strip("\n").split("	")[0].strip()
        if country == "":
            continue
        if country not in remove_country_dicts:
            remove_country_dicts.append(country)


def get_remove_times():
    f = open("C:/Users/ASUS/Desktop/using/remove_times.txt", "r", encoding="utf-8")
    times = f.readlines()
    f.close()
    for time in times:
        time = time.strip("\n").split("	")[0].strip()
        if time == "":
            continue
        if time not in remove_time_dicts:
            remove_time_dicts.append(time)


def get_remove_locations():
    f = open("C:/Users/ASUS/Desktop/using/remove_locations.txt", "r", encoding="utf-8")
    locations = f.readlines()
    f.close()
    for location in locations:
        location = location.strip("\n").split("	")[0].strip()
        if location == "":
            continue
        if location not in remove_location_dicts:
            remove_location_dicts.append(location)


def get_others():
    f = open("C:/Users/ASUS/Desktop/using/others.txt", "r", encoding="utf-8")
    names = f.readlines()
    f.close()
    global other_dicts
    for name in names:
        name = name.strip()
        if name == "":
            continue
        if name not in other_dicts:
            find_dicts.append(name)
            other_dicts.append(name)


def using_weapon_table():
    f = open("C:/Users/ASUS/Desktop/using/weapons.txt", "r", encoding="utf-8")
    weapons = f.readlines()
    f.close()
    global find_dicts
    for weapon in weapons:
        if weapon == "":
            continue
        names = weapon.strip("\n").split(",,,")
        for name in names[1:-1]:
            name = name.strip()
            if name == "":
                continue
            one_names = name.split(";")
            for one_name in one_names:
                one_name = one_name.strip(" ")
                if (one_name not in find_dicts) and (one_name != "") and (len(one_name) <= 10):
                    find_dicts.append(one_name)
                    find_weapon_dicts.append((one_name,10))


def get_find_triggers():
    f = open("C:/Users/ASUS/Desktop/using/standard_triggers.txt", "r", encoding="utf-8")
    triggers = f.readlines()
    global find_trigger_dicts
    global find_dicts
    f.close()
    for trigger in triggers:
        line = trigger.strip().split("	")
        my_trigger = line[0].strip()
        part_of_speech = line[1].strip()
        freq = 1
        if len(line) == 3 and line[2] != "":
            freq = int(line[2])
        if my_trigger == "":
            continue
        if my_trigger not in find_dicts:
            find_dicts.append(my_trigger)
            if part_of_speech == "名词":
                find_trigger_dicts.append((my_trigger, "n",freq))
            elif part_of_speech == "动词":
                find_trigger_dicts.append((my_trigger, "v",freq))
            else:
                find_trigger_dicts.append((my_trigger, "x",freq))
    find_trigger_dicts = sorted(find_trigger_dicts, key = lambda x:(len(x[0]),x[2]), reverse=True)


def get_find_weapons(using_weapons=True):
    if using_weapons:
        using_weapon_table()
    f = open("C:/Users/ASUS/Desktop/using/standard_weapons.txt", "r", encoding="utf-8")
    weapons = f.readlines()
    global find_weapon_dicts
    global find_dicts
    f.close()
    for weapon in weapons:
        line = weapon.strip().split("	")
        my_weapon = line[0].strip()
        freq = 1
        if len(line) == 2 and line[1] != "":
            freq = int(line[1])
        if my_weapon == "":
            continue
        if my_weapon not in find_dicts:
            find_dicts.append(my_weapon)
            find_weapon_dicts.append((my_weapon, freq))
    find_weapon_dicts = sorted(find_weapon_dicts, key = lambda x:(len(x[0]),x[1]), reverse=True)


def get_find_countrys():
    f = open("C:/Users/ASUS/Desktop/using/standard_countrys.txt", "r", encoding="utf-8")
    countrys = f.readlines()
    global find_country_dicts
    global find_dicts
    f.close()
    for country in countrys:
        line = country.strip().split("	")
        my_country = line[0].strip()
        freq = 1
        if len(line) == 2 and line[1] != "":
            freq = int(line[1])
        if my_country == "":
            continue
        if my_country not in find_dicts:
            find_dicts.append(my_country)
            find_country_dicts.append((my_country, freq))
    find_country_dicts = sorted(find_country_dicts, key = lambda x:(len(x[0]),x[1]), reverse=True)


def get_find_times():
    f = open("C:/Users/ASUS/Desktop/using/standard_times.txt", "r", encoding="utf-8")
    times = f.readlines()
    global find_time_dicts
    global find_dicts
    f.close()
    for time in times:
        line = time.strip().split("	")
        my_time = line[0].strip()
        freq = 1
        if len(line) == 2 and line[1] != "":
            freq = int(line[1])
        if my_time == "":
            continue
        if my_time not in find_dicts:
            find_dicts.append(my_time)
            find_time_dicts.append((my_time, freq))
    find_time_dicts = sorted(find_time_dicts, key = lambda x:(len(x[0]),x[1]), reverse=True)


def get_find_locations():
    f = open("C:/Users/ASUS/Desktop/using/standard_locations.txt", "r", encoding="utf-8")
    locations = f.readlines()
    global find_location_dicts
    global find_dicts
    f.close()
    for location in locations:
        line = location.strip().split("	")
        my_location = line[0].strip()
        freq = 1
        if len(line) == 2 and line[1] != "":
            freq = int(line[1])
        if my_location == "":
            continue
        if my_location not in find_dicts:
            find_dicts.append(my_location)
            find_location_dicts.append((my_location, freq))
    find_location_dicts = sorted(find_location_dicts, key = lambda x:(len(x[0]),x[1]), reverse=True)


item_num = 0


def change(fileName):
    f = open(fileName, "r", encoding="utf-8")
    examples = json.load(f)
    f.close()
    global all_examples, item_num
    f1 = open("C:/Users/ASUS/Desktop/data_output.txt", "w+", encoding="utf-8")
    for example in examples:
        my_example = {}
        sentence = example["sentence"]
        print(sentence)
        f1.write(sentence + "\n")
        my_events = []
        events = example["events"]
        add_sign = False
        for event in events:
            try:
                trigger = event["trigger"]
            except:
                continue
            text = trigger["text"]
            if text not in find_dicts:
                continue
            item_num += 1
            add_sign = True
            my_events.append(event)
        if not add_sign:
            continue
        all_examples.append({"sentence": sentence, "events": my_events, "arguments": example["arguments"]})
        f1.write("【识别的触发词】：\n")
        for event in my_events:
            print(event["trigger"])
            f1.write(str(event) + "\n")
    f1.close()


if __name__ == "__main__":
    get_find_triggers()
    get_remove_triggers()
    get_others()
    file_num_list = list(range(1,28)) + list(range(239,1700))
    print(file_num_list)
    #change("E:/Rootpath/dataset/data.json")
    files = file_name("C:/Users/ASUS/Desktop/mark/json")
    for file in files:
        file_num = int(file.split(".")[0])
        if file_num in file_num_list:
            change("C:/Users/ASUS/Desktop/mark/json/" + file)
    f = open("C:/Users/ASUS/Desktop/data.json", "w+", encoding="utf-8")
    print(len(all_examples))
    print(item_num)
    json.dump(all_examples,f)
    f.close()