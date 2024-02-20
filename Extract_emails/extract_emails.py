import re
persons_data = {}

with open("split.txt", "r") as file:
    for line in file:
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        found = re.findall(pattern, line)
        for email in found:
            name = email.split("@")[0]
            if name not in persons_data:
                persons_data[name] = []
            persons_data[name].append(email)

print(persons_data)
for name_, data in persons_data.items():
    print(f"The name is -  {name_}. His email\\s is/are: {', '.join(data)}.")

file.close()

