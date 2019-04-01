# dateutil is a third-party library
from dateutil.parser import parse
# datetime is a built-in module
from datetime import datetime

example = '2019-10-12 13:14:15.890'

# able to convert different string format to datetime automatically
print('Converting string to datetime using dateutil.parser.parse')
print(parse(example))

# the datetime format must be known when using strptime
print('Converting string to datetime using datetime.strptime')
print(datetime.strptime(example, '%Y-%m-%d %H:%M:%S.%f'))
