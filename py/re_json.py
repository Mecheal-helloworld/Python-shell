import json
result = []
with open("E:/Model/nature_model_win/data/final/raw_data/stack.json", "r", encoding="utf-8") as f:
    examples = json.load(f)
    for example in examples:
        data = {}
        data['sentence'] = example['sentence']
        my_events = example['events'][0]
        events = []
        event = {}
        labels = {}
        labels['tense'] = my_events['tense']
        labels['polarity'] = my_events['polarity']
        times = []
        locs = []
        subjects = []
        objects = []
        weapons = []
        countrys = []
        for role in my_events['arguments']:
            argument = {}
            argument['text'] = role['text']
            argument['offset'] = role['offset']
            argument['length'] = role['length']
            if role['role'] == "object":
                objects.append(argument)
            if role['role'] == "subject":
                subjects.append(argument)
            if role['role'] == "time":
                times.append(argument)
            if role['role'] == "loc":
                locs.append(argument)
        arguments = {}
        arguments['time'] = times
        arguments['loc'] = locs
        arguments['weapon'] = weapons
        arguments['country'] = countrys
        event['subject'] = subjects
        event['object'] = objects
        event['trigger'] = [my_events['trigger']]
        event['labels'] = labels
        events.append(event)
        data['arguments'] = arguments
        data['events'] = events
        result.append(data)
        f.close()
with open("E:/Rootpath/dataset/train/train_1.json", "w+", encoding="gbk") as f:
    print(result[0])
    json.dump(result,f)
    f.close()