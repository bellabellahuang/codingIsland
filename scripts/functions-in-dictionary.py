# use this method when designing a function for
# repetitive codes with a slice of difference


def function_1(payload):
    return result_1


def function_2(payload):
    return result_2


def function_3(payload):
    return result_3


# type could be ['A', 'B', 'C']
def mainFunction(type, payload):
    functions = {'A': function_1, 'B': function_2, 'C': function_3}
    return functions[type](payload)
