import json

file_path = "./config.json"

def loadConfig():
    with open(file_path, 'r') as file:
        return json.load(file)

def modifyConfig(key_to_modify, new_value):
    # Step 1: Read the JSON file
    json_data = loadConfig(file_path)

    # Step 2: Modify the data in memory
    if key_to_modify in json_data:
        json_data[key_to_modify] = new_value
    else:
        print(f"Key {key_to_modify} not found.")