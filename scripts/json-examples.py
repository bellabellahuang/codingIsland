import json
from io import StringIO

# --------------------------------
# json.loads
# converting string to dictionary
json.loads('{"a": 1, "b": 2, "c": 3}')

with open("filename.json", "r") as cfgfile:
    cfg = json.loads(cfgfile.read())
    print(cfg)

# --------------------------------
# json.load
# converting a file-like object to dictionary
with open("filename.json", "r") as cfgfile:
    cfg = json.load(cfgfile)
    print(cfg)

io = StringIO('["streaming API"]')
print(json.load(io))

# --------------------------------
# json.dumps
# converting dictionary to string
json.dumps({"a": 1, "b": 2, "c": 3}, indent=2)

# --------------------------------
# json.dump
# converting json objects into a file-like writable object
example = {"json": "test"}
with open("filename.json", "w") as f:
    json.dump(example, f)

# --------------------------------
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
