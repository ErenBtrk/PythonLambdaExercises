'''
22. Write a Python program that sum the length of the names of a given list
of names after removing the names that starts with an lowercase letter.
Use lambda function.
Result:
16

'''
import re


string1 = "Hello.my Name is Yarasa reis".replace('.',' ').split(' ')


print(string1)

function1 = lambda x : x if (x[0].isupper()) else ''

result1 = list(filter(function1,string1))

numOfLetters = 0

for item in result1:
    numOfLetters += len(item)

print(numOfLetters)
