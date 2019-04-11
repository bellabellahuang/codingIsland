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
