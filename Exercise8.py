'''

8. Write a Python program to extract year, month, date and time using Lambda.
Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178

'''

import re


def function(date):
    return lambda : re.split('-| ',date)

result = function("2020-01-15 09:03:32.744178")

list = result()

for item in list:
    print(item)

