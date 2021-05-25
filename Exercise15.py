'''
15. Write a Python program to add two given lists using map and lambda.
Original list:
[1, 2, 3]
[4, 5, 6]
Result: after adding two list
[5, 7, 9]

'''

list1 = [1, 2, 3]
list2 = [4, 5, 6]

function1 = lambda x,y: x+y

result1 = list(map(function1,list1,list2))

print(result1)

