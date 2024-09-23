import json


def write_json(data, filename="02_names.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


with open("02_names.json") as json_file:
    data = json.load(json_file)
    temp = data["names"]
    rec = {"firstname": "Mike", "age": 45}
    temp.append(rec)

write_json(data)
