# get element index of a list
example = [1, 2, 3]
print(example.index(2))
# output: 1


# split a list into evenly sized chunks
# create a list from 0 to 99
data = [str(n) for n in range(100)]
chunks = [data[x:x + 10] for x in range(0, len(data), 10)]
print(chunks)
# '10' indicates the maximum size of each chunk
# output:
# [
#     ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
#     ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19'],
#     ['20', '21', '22', '23', '24', '25', '26', '27', '28', '29'],
#     ['30', '31', '32', '33', '34', '35', '36', '37', '38', '39'],
#     ['40', '41', '42', '43', '44', '45', '46', '47', '48', '49'],
#     ['50', '51', '52', '53', '54', '55', '56', '57', '58', '59'],
#     ['60', '61', '62', '63', '64', '65', '66', '67', '68', '69'],
#     ['70', '71', '72', '73', '74', '75', '76', '77', '78', '79'],
#     ['80', '81', '82', '83', '84', '85', '86', '87', '88', '89'],
#     ['90', '91', '92', '93', '94', '95', '96', '97', '98', '99']
# ]


# convert a list of tuples into a list with all first elements of each tuple
example = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
result = [t[0] for t in example]
print(result)
# output: [1, 3, 5, 7, 9]


# convert a list of strings into string
example = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
s = ','.join(example)
print(s)
# output: 0,1,2,3,4,5,6,7,8,9


# convert a list of numbers into string
numbers = [n for n in range(10)]
# convert it into a list of strings and then join each element into one string
print(','.join([str(x) for x in numbers]))
# output: 0,1,2,3,4,5,6,7,8,9


# replace the original list in a single line
numbers = [n for n in range(10)]
numbers = [n for n in numbers if bool(n % 2)]
print(numbers)
# output: [1, 3, 5, 7, 9]


# even numbers using filter function
numbers = [n for n in range(10)]
print(list(filter(lambda x: x % 2 == 0, numbers)))
# output: [0, 2, 4, 6, 8]
