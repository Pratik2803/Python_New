import json
import csv

# Sample JSON data with multiple rows
data = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
    {"name": "Charlie", "age": 28, "city": "Chicago"}
]

# write json to sample file

with open(file="json.txt", mode='w') as file:
    json.dump(data, file, indent=1)


# read json file
with open("json.txt", 'r') as file: 
    content = json.load(file)
    for item in content:
        for key in item.keys():
            if key == 'name':
                print(f"{key} : {item[key]}")

