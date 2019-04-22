# get element index of a list
example = [1, 2, 3]
print(example.index(2))


# split a list into evenly sized chunks
# create a list from 0 to 99
data = [str(n) for n in range(100)]
chunks = [data[x:x + 10] for x in range(0, len(data), 10)]
print(chunks)
# '10' indicates the maximum size of each chunk


# convert a list of tuples into a list with all first elements of each tuple
example = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
result = [t[0] for t in example]
print(result)


# convert a list of strings into string
example = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
s = ','.join(example)
print(s)


# convert a list of numbers into string
numbers = [n for n in range(10)]
# convert it into a list of strings and then join each element into one string
print(','.join([str(x) for x in numbers]))
