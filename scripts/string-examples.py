# -----------------------------
# separating a string with a delimeter
example = 'a/b/c/d'
print(example.split('/'))
# output: ['a', 'b', 'c', 'd']

print('/'.join(example.split('/')[2:]))
# output: c/d


# -----------------------------
# replacing the last character of a string
print(example[:-1] + 'e')


# -----------------------------
# formatting string with variable placer
example = """
    SELECT * FROM {table}
    WHERE id = '{id}';
"""

print(example.format(table="students", id="123"))


# -----------------------------
# string formatting with dictionary
kwargs = {
    "table": "teachers",
    "id": "000"
}
print(example.format(**kwargs))


# -----------------------------
# converting http payload string to key-value dictionary
def convertParamsToDict(req_string):
    req_dict = {}
    for val in req_string.split('&'):
        k, v = val.split('=')
        req_dict[k] = v
    return req_dict


# -----------------------------
# convert string to or from binary
string_example = "hello world"
binary_result = string_example.encode('utf-8')
string_result = binary_result.decode('utf-8')

# -----------------------------
# convert string to or from base64 string
import base64
base64_result = base64.b64encode(string_example.encode('utf-8'))
string_result = base64.b64decode(base64_result).decode('utf-8')

# -----------------------------
# convert dictionary to string with '&' symbol which is commonly used in http urls
import urllib.parse
print(urllib.parse.urlencode({'one': 1, 'two': 2}))
# output: one=1&two=2
