import json
import os
def file_name(file_dir):
    L=[] 
    for root,dirs, files in os.walk(file_dir):  
        for file in files:
            if os.path.splitext(file)[1]=='.json':
                L.append(os.path.join(file))
    return L

trigger_f = open("C:/Users/ASUS/Desktop/all_triggers.txt", "w+", encoding="utf-8")
def change(fileName):
    f = open(fileName, "r", encoding="utf-8")
    examples = json.load(f)
    f.close()
    trigger_texts = set()
    for example in examples:
        events = example["events"]
        for event in events:
            try:
                trigger = event["trigger"]
            except:
                continue
            text = trigger["text"]
            trigger_texts.add(text)
    triggers_texts = ""
    for trigger_text in trigger_texts:
        triggers_texts = triggers_texts + trigger_text + " "
    trigger_f.write(triggers_texts+"\n")


if __name__ == "__main__":
    files = file_name("C:/Users/ASUS/Desktop/json")
    for file in files:
        change("C:/Users/ASUS/Desktop/json/" + file)
    trigger_f.close()