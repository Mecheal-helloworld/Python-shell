import json
import os
import copy

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

trigger_dicts = {}
trigger_list = []

trigger_file = open("C:/Users/ASUS/Desktop/Trigger.txt", "r", encoding="utf-8")
read_trigger = trigger_file.readlines()
trigger_file.close()
for line in read_trigger:
    trigger_items = line.strip().split(" ")
    for trigger_item in trigger_items:
        if trigger_item not in trigger_list:
            trigger_list.append(trigger_item)
            trigger_dicts[trigger_item] = trigger_items
print(trigger_dicts)

def expend_events(sentence, event):
    rtn_expends = []
    event_trigger = event["trigger"]
    event_subject = event["subject"]
    event_object = event["object"]
    offset = event_trigger["offset"]
    length = event_trigger["length"]
    triggers = trigger_dicts[event_trigger["text"]]
    rtn_obj = {}
    rtn_sub = {}
    for expend_trigger in triggers:
        addLength = len(expend_trigger)
        addTrigger = {"text":expend_trigger,"offset":offset,"length":addLength}
        rtn_sentence = sentence[:offset] + expend_trigger + sentence[offset+length:]
        print(rtn_sentence)
        if length == addLength:
            rtn_expends.append((rtn_sentence,{"trigger":addTrigger,"subject":event_subject,"object":event_object}))
            continue
        rtn_obj = copy.deepcopy(event_object)
        rtn_sub = copy.deepcopy(event_subject)
        if event_subject["offset"] > addLength:
            rtn_sub["offset"] = event_subject["offset"] + addLength - length
        if event_object["offset"] > addLength:
            rtn_obj["offset"] = event_object["offset"] + addLength - length
        rtn_expends.append((rtn_sentence,{"trigger":addTrigger,"subject":rtn_sub,"object":rtn_obj}))
    return rtn_expends

def change(fileName):
    f = open(fileName+".json", "r", encoding="utf-8")
    examples = json.load(f)
    f.close()
    example_index = 0
    my_examples = []
    for example in examples:
        sentence = example["sentence"]
        events = example["events"]
        add_sign = False
        for event in events:
            subject_text = event["subject"]["text"]
            object_text = event["object"]["text"]
            if (subject_text == "") or (subject_text == ""):
                continue
            if check_in(sentence,event["trigger"]):
                add_sign = True
                my_expends = expend_events(sentence, event)
                example_index += len(my_expends) - 1
                for expend_sentence, expend_event in my_expends:
                    my_examples.append({"sentence": expend_sentence, "events": [expend_event], "arguments": example["arguments"]})
        if add_sign:
            example_index += 1
    '''
        if example_index == 669 * 7:
            f = open(fileName+"_train.json", "w+", encoding="utf-8")
            json.dump(my_examples,f)
            f.close()
            my_examples = []
    '''
    print(len(my_examples))
    f = open(fileName+"_train.json", "w+", encoding="utf-8")
    json.dump(my_examples,f)
    f.close()


if __name__ == "__main__":
    print("hhh")
    change("C:/Users/ASUS/Desktop/data_subobj_eval")