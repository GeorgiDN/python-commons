import re
information = {}

with open("split.txt", "r") as file:
    for line in file:
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        found = re.findall(pattern, line)
        for email in found:
            name = email.split("@")[0]
            if name not in information:
                information[name] = []
            information[name].append(email)

print(information)
for name_, data in information.items():
    print(f"The name is -  {name_}. His email\\s is/are: {', '.join(data)}.")

file.close()
