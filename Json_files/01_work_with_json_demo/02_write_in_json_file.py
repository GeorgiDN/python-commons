import json

with open('states.json') as f:
    data = json.load(f)

for state in data["states"]:
    print(state["name"])


for state in data["states"]:
    print(state["name"], state["abbreviation"])


for state in data["states"]:
    del state["area_codes"]

# with open("new_states.json", "w") as f:
#     json.dump(data, f)

with open("new_states.json", "w") as f:
    json.dump(data, f, indent=2)  # serialize a Python object and write it directly to a file in JSON format
