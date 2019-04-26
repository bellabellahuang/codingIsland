import re

# a pattern object to validate strings start with 'h'
# 's' is optional
validator = re.compile('^https?://')
validator.match('https://abc.com')  # true
validator.match('http://abc.com')  # true
validator.match('abc.com')  # true
