import json
import csv

with open("04_names.json", "r") as f:
    data = json.load(f)
    names = data["names"]

    with open("04_names.csv", "w") as output_file:
        fieldnames = names[0].keys()
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        for name in names:
            writer.writerow(name)
