import json
import copy

find_dicts = []

def get_find_triggers():
    f = open("C:/Users/ASUS/Desktop/using/standard_triggers.txt", "r", encoding="utf-8")
    triggers = f.readlines()
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
        if (my_trigger not in find_dicts) and len(my_trigger) == 2:
            find_dicts.append(my_trigger)


if __name__ == "__main__":
    f = open("C:/Users/ASUS/Desktop/data_small_eval.json", "r", encoding="utf-8")
    examples = json.load(f)
    f.close()
    example_index = 0
    my_examples = []
    
    for example in examples:
        my_example = {}
        sentence = example["sentence"]
        my_example["sentence"] = sentence
        events = example["events"]
        my_events = []
        my_triggers = []
        my_distance = []
        for event in events:
            my_trigger = event["trigger"]["text"]
            if len(my_trigger) != 2:
                continue
            my_event = {"trigger" : event["trigger"]}
            my_arguments = []
            my_subject = copy.deepcopy(event["subject"])
            my_subject["role"] = "subject"
            if my_subject["text"] != "":
                my_arguments.append(my_subject)
            my_object = copy.deepcopy(event["object"])
            my_object["role"] = "object"
            if my_object["text"] != "":
                my_arguments.append(my_object)
            my_event = {"trigger" : event["trigger"], "arguments": my_arguments}
            my_events.append(my_event)
            my_triggers.append(my_trigger)
        for find_trigger in find_dicts:
            if find_trigger in sentence:
                my_distance.append(find_trigger)
        my_example["distant_triggers"] = my_distance
        my_example["events"] = my_events
        my_examples.append(my_example)
    print(len(my_examples))
    f = open("C:/Users/ASUS/Desktop/data_dev.json", "w+", encoding="utf-8")
    json.dump(my_examples,f)
    f.close()