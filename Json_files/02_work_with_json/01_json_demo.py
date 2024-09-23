import json

file = "01_names.json"

with open(file) as json_file:
    data = json.load(json_file)
    name_data = data["names"]
    for idx in name_data:
        name = (idx["firstname"])
        age = (idx["age"])
        print(f"{name} is {age}")
