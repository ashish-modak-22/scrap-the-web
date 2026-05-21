import os
import json


def json_load(file_Location):
    if not os.path.exists(file_Location):
        return []
    
    try:
        with open(file_Location, "r", encoding="utf-8") as file:
            return json.load(file)
        
    except json.JSONDecodeError:
        return[]
    

def json_save(file_Location,data):
    with open(file_Location, "w", encoding="utf-8") as file:
        json.dump(data,file, indent=3, ensure_ascii=False)


def json_append(file_Location, new_data):
    data = json_load(file_Location)
    if not isinstance(data, list):
        data = []
    data.append(new_data)
    json_save(file_Location, data)


def json_update(file_Location, condition_key, condition_val, update_data):
    data = json_load(file_Location)
    for item in data:
        if item.get(condition_key) == condition_val:
            item.update(update_data)

    json_save(file_Location, data)


def json_clear(file_Location):
    json_save(file_Location, [])
