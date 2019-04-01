import datetime

today = datetime.date.today()
print('Today is %s.' % today)

tomorrow = today + datetime.timedelta(days=1)
print('Tomorrow is %s.' % tomorrow)

yesterday = today - datetime.timedelta(hours=24)
print('Yesterday was %s.' % yesterday)

# output:
# Today is 2019-04-01.
# Tomorrow is 2019-04-02.
# Yesterday was 2019-03-31.
