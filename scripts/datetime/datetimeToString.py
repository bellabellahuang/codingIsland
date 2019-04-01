from datetime import datetime

example = datetime.utcnow()

print(example)
# output: 2019-04-01 22:42:06.803544

print(example.strftime('%Y/%m/%d'))
# output: 2019/04/01
