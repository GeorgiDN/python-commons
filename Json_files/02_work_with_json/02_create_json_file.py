import json

file = "01_names.json"


def write_json(data, filename="01_new_json_data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


with open(file, "r") as json_file:
    data = json.load(json_file)
    write_json(data)

