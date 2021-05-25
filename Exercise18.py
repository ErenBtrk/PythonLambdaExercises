'''
8. Write a Python program to find palindromes in a given list of strings using Lambda.
Orginal list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']

'''

list1 = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

function1 = lambda x : x == x[::-1]

result1 = list(filter(function1,list1))

print(result1)