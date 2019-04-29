import json
from io import StringIO

# converting string to dictionary
json.loads('{"a": 1, "b": 2, "c": 3}')

with open("filename.json", "r") as cfgfile:
    cfg = json.loads(cfgfile.read())
    print(cfg)

# converting a file-like object to dictionary
with open("filename.json", "r") as cfgfile:
    cfg = json.load(cfgfile)
    print(cfg)

io = StringIO('["streaming API"]')
print(json.load(io))

# converting dictionary to string
json.dumps({"a": 1, "b": 2, "c": 3}, indent=2)

# converting json to csv
json_obj = {
    "student": "Jason",
    "gpa": "3.1"
}

csv_obj = ','.join([
    json_obj['student'],
    json_obj['gpa'] +
    '\n'
])
