def myFun(**kwargs):
    for key, value in kwargs.items():
        print(key + "=" + value)


"""
calling function using named arguments
myFun(a=1, b=2, c=3)

calling function by passing a dictionary object
myFun(**{"a": "1", "b": "2", "c": "3"})

** is required to unpack the dictionay
"""


def sum(*argv):
    sum = 0
    for num in argv:
        sum += num
    print("sum: " + str(sum))


"""
create a function with variable number of arguments
sum(1, 2, 3)
"""
