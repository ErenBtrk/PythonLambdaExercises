'''
11. Write a Python program to find intersection of two given arrays using Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
[1, 2, 4, 8, 9]
Intersection of the said arrays: [1, 2, 8, 9]

'''

list1 = [1, 2, 3, 5, 7, 8, 9, 10]
list2 = [1, 2, 4, 8, 9]

check_intersection = filter(lambda x : x in list1,list2)

result1 = list(check_intersection)

print(result1)

