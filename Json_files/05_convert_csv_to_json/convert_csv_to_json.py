import json
import csv

with open("05_names.csv", "r") as f:
    reader = csv.reader(f)
    next(reader, None)
    data = {"names": []}
    for row in reader:
        data["names"].append({"firstname": row[0], "age": row[1]})

with open("05_names.json", "w") as f:
    json.dump(data, f, indent=4)
