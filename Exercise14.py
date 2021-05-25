'''
14. Write a Python program to find the values of length six in a given list using Lambda.
Sample Output:
Monday
Friday
Sunday

'''

list1 = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

function1 = lambda x : len(x) == 6

result1 = list(filter(function1,list1))

print(result1)
