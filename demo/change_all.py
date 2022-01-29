import json
import os
import jieba
import jieba.posseg as pseg
import wordseg

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
word_flag = []
words_in_sentence = []

#dict_f = open("C:/Users/ASUS/Desktop/dict.txt", "a", encoding="utf-8-sig")


def get_files_of_path(file_dir):
    L=[] 
    for root,dirs, files in os.walk(file_dir):  
        for file in files:
            if os.path.splitext(file)[1]=='.json':
                L.append(os.path.join(file))
    return L

'''
def get_roles_in_seq(sentence, role, part_of_speech="x"):
    role_length = len(role)
    if role_length==0 :
        print("error")
        return []
    if role not in sentence:
        print("error")
        return []
    rtn_roles = []
    global word_in_sentence_label
    my_cut_all_words = [sentence]
    offset = 0
    for cut_word in words_in_sentence:
        if len(cut_word) <= role_length:
            break
        if role in cut_word:
            tmp_my_cut_all_words = []
            for each_word in my_cut_all_words:
                my_cut_each_words = each_word.split(cut_word)
                tmp_my_cut_all_words.append(my_cut_each_words[0])
                for num_i in range(1,len(my_cut_each_words)):
                    tmp_my_cut_all_words.append(cut_word)
                    tmp_my_cut_all_words.append(my_cut_each_words[num_i])
            my_cut_all_words = tmp_my_cut_all_words
    tmp_my_cut_all_words = []
    for each_word in my_cut_all_words:
        my_cut_each_words = each_word.split(role)
        tmp_my_cut_all_words.append(my_cut_each_words[0])
        for num_i in range(1,len(my_cut_each_words)):
            tmp_my_cut_all_words.append(role)
            tmp_my_cut_all_words.append(my_cut_each_words[num_i])
    my_cut_all_words = tmp_my_cut_all_words
    for cut_word in my_cut_all_words:
        if cut_word == role:
            if part_of_speech == "x":
                rtn_roles.append({"text": role,"offset": offset, "length": role_length})
            else:
                if (words_flag[offset] == part_of_speech) or (words_flag[offset] == "x"):
                    rtn_roles.append({"text": role,"offset": offset, "length": role_length})
        offset = offset + len(cut_word)
    return rtn_roles
'''

def get_roles_in_seq(sentence, role, part_of_speech="x"):
    role_length = len(role)
    if role_length==0 :
        print("error")
        return []
    if role not in sentence:
        print("error")
        return []
    rtn_roles = []
    global word_in_sentence
    offset = 0
    for cut_word in words_in_sentence:
        if cut_word == role:
            if part_of_speech == "x":
                rtn_roles.append({"text": role,"offset": offset, "length": role_length})
            else:
                if (words_flag[offset] == part_of_speech) or (words_flag[offset] == "x"):
                    rtn_roles.append({"text": role,"offset": offset, "length": role_length})
        offset = offset + len(cut_word)
    return rtn_roles


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
    for word in other_dicts:
        jieba.add_word(word)


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
    for word,tag,freq in find_trigger_dicts:
        jieba.add_word(word, freq)


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
    for word, freq in find_weapon_dicts:
        jieba.add_word(word, freq)


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
    for word, freq in find_country_dicts:
        jieba.add_word(word, freq)


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
    for word, freq in find_time_dicts:
        jieba.add_word(word, freq)


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
    for word, freq in find_location_dicts:
        jieba.add_word(word, freq)


def change(fileName):
    f = open(fileName+".json", "r", encoding="utf-8")
    examples = json.load(f)
    f.close()
    f1 = open("E:/Rootpath/data/mark/data/" + fileName.split("/")[-1]+".txt", "w+", encoding="utf-8")
    global sentence_label
    global words_in_sentence
    global words_flag
    my_examples = []
    for example in examples:
        my_example = {}
        sentence = example["sentence"]
        print(sentence)
        f1.write(sentence + "\n")
        sentence_token = [0] * len(sentence)
        cut_words_ = pseg.cut(sentence)
        words_in_sentence = wordseg.BMM(sentence)#jieba.lcut(sentence,cut_all=True,HMM=True)
        words_flag = []
        for cut_res in cut_words_:
            for word_i in cut_res.word:
                words_flag.append(cut_res.flag)
        my_triggers = []
        my_events = []
        events = example["events"]
        empty = {"text": "","offset": 0, "length": 0}
        arguments = example["arguments"]
        times = arguments["time"]
        locs = arguments["loc"]
        weapons = arguments["weapon"]
        countrys = arguments["country"]
        my_times = []
        my_locs = []
        my_weapons = []
        my_countrys = []
        for event in events:
            try:
                trigger = event["trigger"]
            except:
                continue
            text = trigger["text"]
            if text in remove_trigger_dicts:
                continue
            start_offset = trigger["offset"]
            end_offset = start_offset + trigger["length"]
            for index in range(start_offset, end_offset):
                sentence_token[index] = 1
            my_events.append(event)
        for role in times:
            text = role["text"]
            if text in remove_time_dicts:
                continue
            start_offset = role["offset"]
            end_offset = start_offset + role["length"]
            for index in range(start_offset, end_offset):
                sentence_token[index] = 1
            my_times.append(role)
        for role in locs:
            text = role["text"]
            if text in remove_location_dicts:
                continue
            start_offset = role["offset"]
            end_offset = start_offset + role["length"]
            for index in range(start_offset, end_offset):
                sentence_token[index] = 1
            my_locs.append(role)
        for role in weapons:
            text = role["text"]
            if text in remove_weapon_dicts:
                continue
            start_offset = role["offset"]
            end_offset = start_offset + role["length"]
            for index in range(start_offset, end_offset):
                sentence_token[index] = 1
            my_weapons.append(role)
        for role in countrys:
            text = role["text"]
            if text in remove_country_dicts:
                continue
            start_offset = role["offset"]
            end_offset = start_offset + role["length"]
            for index in range(start_offset, end_offset):
                sentence_token[index] = 1
            my_countrys.append(role)
        for find_role, part_of_speech,freq in find_trigger_dicts:
            if find_role in sentence:
                roles_in = get_roles_in_seq(sentence, find_role, part_of_speech)
                for inner_role in roles_in:
                    add_sign = True
                    now_role_start = inner_role["offset"]
                    now_role_end = now_role_start + inner_role["length"]
                    for index in range(now_role_start, now_role_end):
                        if sentence_token[index] == 1:
                            add_sign = False
                            break
                    if add_sign:
                        start_offset = inner_role["offset"]
                        end_offset = start_offset + inner_role["length"]
                        for index in range(start_offset, end_offset):
                            sentence_token[index] = 1
                        my_events.append({"trigger": inner_role, "subject": empty, "object": empty})
        for find_role, freq in find_time_dicts:
            if find_role in sentence:
                roles_in = get_roles_in_seq(sentence, find_role)
                for inner_role in roles_in:
                    add_sign = True
                    now_role_start = inner_role["offset"]
                    now_role_end = now_role_start + inner_role["length"]
                    for index in range(now_role_start, now_role_end):
                        if sentence_token[index] == 1:
                            add_sign = False
                            break
                    if add_sign:
                        start_offset = inner_role["offset"]
                        end_offset = start_offset + inner_role["length"]
                        for index in range(start_offset, end_offset):
                            sentence_token[index] = 1
                        my_times.append(inner_role)
        for find_role,freq in find_location_dicts:
            if find_role in sentence:
                roles_in = get_roles_in_seq(sentence, find_role)
                for inner_role in roles_in:
                    add_sign = True
                    now_role_start = inner_role["offset"]
                    now_role_end = now_role_start + inner_role["length"]
                    for index in range(now_role_start, now_role_end):
                        if sentence_token[index] == 1:
                            add_sign = False
                            break
                    if add_sign:
                        start_offset = inner_role["offset"]
                        end_offset = start_offset + inner_role["length"]
                        for index in range(start_offset, end_offset):
                            sentence_token[index] = 1
                        my_locs.append(inner_role)
        for find_role,freq in find_weapon_dicts:
            if find_role in sentence:
                roles_in = get_roles_in_seq(sentence, find_role)
                for inner_role in roles_in:
                    add_sign = True
                    now_role_start = inner_role["offset"]
                    now_role_end = now_role_start + inner_role["length"]
                    for index in range(now_role_start, now_role_end):
                        if sentence_token[index] == 1:
                            add_sign = False
                            break
                    if add_sign:
                        start_offset = inner_role["offset"]
                        end_offset = start_offset + inner_role["length"]
                        for index in range(start_offset, end_offset):
                            sentence_token[index] = 1
                        my_weapons.append(inner_role)
        for find_role,freq in find_country_dicts:
            if find_role in sentence:
                roles_in = get_roles_in_seq(sentence, find_role)
                for inner_role in roles_in:
                    add_sign = True
                    now_role_start = inner_role["offset"]
                    now_role_end = now_role_start + inner_role["length"]
                    for index in range(now_role_start, now_role_end):
                        if sentence_token[index] == 1:
                            add_sign = False
                            break
                    if add_sign:
                        start_offset = inner_role["offset"]
                        end_offset = start_offset + inner_role["length"]
                        for index in range(start_offset, end_offset):
                            sentence_token[index] = 1
                        my_countrys.append(inner_role)
        my_arguments = {"time": my_times, "loc": my_locs, "weapon": my_weapons, "country": my_countrys}
        my_examples.append({"sentence": sentence, "events": my_events, "arguments": my_arguments})
        f1.write("【识别的触发词】：\n")
        for event in my_events:
            print(event["trigger"])
            f1.write(str(event["trigger"]) + "\n")
        f1.write("【识别的时间】：\n")
        for role in my_times:
            print(role)
            f1.write(str(role) + "\n")
        f1.write("【识别的地点】：\n")
        for role in my_locs:
            print(role)
            f1.write(str(role) + "\n")
        f1.write("【识别的武器】：\n")
        for role in my_weapons:
            print(role)
            f1.write(str(role) + "\n")
        f1.write("【识别的国家】：\n")
        for role in my_countrys:
            print(role)
            f1.write(str(role) + "\n")
        f1.write("\n")
    print(len(my_examples))
    f = open(fileName+".json", "w+", encoding="utf-8")
    json.dump(my_examples,f)
    f.close()
    f1.close()


if __name__ == "__main__":
    get_find_triggers()
    get_remove_triggers()
    get_find_countrys()
    get_remove_countrys()
    get_find_weapons()
    get_remove_weapons()
    get_find_times()
    get_remove_times()
    get_find_locations()
    get_remove_locations()
    get_others()
    '''
    f = open("E:/Rootpath/resource/Trigger.txt", "w+", encoding="utf-8")
    for trigger in find_trigger_dicts:
        f.write(trigger[0]+"\n")
    f.close()
    f = open("E:/Rootpath/resource/Weapon.txt", "w+", encoding="utf-8")
    for role in find_weapon_dicts:
        f.write(role[0]+"\n")
    f.close()
    f = open("E:/Rootpath/resource/TimeLoc.txt", "w+", encoding="utf-8")
    for role in find_time_dicts:
        f.write(role[0]+"\n")
    for role in find_location_dicts:
        f.write(role[0]+"\n")
    f.close()
    f = open("E:/Rootpath/resource/Country.txt", "w+", encoding="utf-8")
    for role in find_country_dicts:
        f.write(role[0]+"\n")
    f.close()
    '''
    change("C:/Users/ASUS/Desktop/data")#E:/Rootpath/dataset/test/data")
    '''
    files = get_files_of_path("E:/Rootpath/data/mark/json")
    for file in files:
        print(file)
        change("E:/Rootpath/data/mark/json/" + file.split(".")[0])
    '''