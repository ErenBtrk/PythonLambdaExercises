'''
21. Write a Python program that multiply each number of given list with a given
 number using lambda function. Print the result.
Original list: [2, 4, 6, 9, 11]
Given number: 2
Result:
4 8 12 18 22

'''

list1 = [2, 4, 6, 9, 11]

function1 = lambda x : x*2

result1 = list(map(function1,list1))

print(result1)