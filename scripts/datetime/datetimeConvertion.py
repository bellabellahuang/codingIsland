# dateutil is a third-party library
from dateutil.parser import parse
# datetime is a built-in module
from datetime import datetime

# -----------------------------
# converting string to datetime
example = '2019-10-12 13:14:15.890'

# able to convert different string format to datetime automatically
print('Converting string to datetime using dateutil.parser.parse')
print(parse(example))

# the datetime format must be known when using strptime
print('Converting string to datetime using datetime.strptime')
print(datetime.strptime(example, '%Y-%m-%d %H:%M:%S.%f'))


# -----------------------------
# converting datetime to string
example = datetime.utcnow()

print(example)
# output: 2019-04-01 22:42:06.803544

print(example.strftime('%Y/%m/%d'))
# output: 2019/04/01


# -----------------------------
# converting datetime to timestamp
example = datetime.utcnow()

print('converting datetime to timestamp using timestamp()')
print(example.timestamp())
# output: 1554180640.580296

print('converting datetime to timestamp using strftime()')
# display the int digital only
print(example.strftime('%s'))
# output: 1554180620

# display it in float format, same as timestamp()
print(example.strftime('%s.%f'))
# output: 1554180640.580296


# -----------------------------
# converting timestamp to datetime
example = 1554180640.580296

print(datetime.fromtimestamp(example))
# output: 2019-04-01 21:50:40.580296
