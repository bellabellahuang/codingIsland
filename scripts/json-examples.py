import json

# converting string to dictionary
json.loads('{"a": 1, "b": 2, "c": 3}')

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
