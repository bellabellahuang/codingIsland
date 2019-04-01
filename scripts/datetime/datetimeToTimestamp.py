from datetime import datetime

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
