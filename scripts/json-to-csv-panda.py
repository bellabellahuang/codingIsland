from pandas.io.json import json_normalize

json_example = {"Name": "Jackson", "Age": 22, "Grade": 86}
table_result = json_normalize(json_example)
csv_result = table_result.to_csv(sep=',', header=False, index=False)
print(csv_result)
# output: '22,86,Jackson\n'
