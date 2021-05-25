'''
12. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
Original arrays:
[-1, 2, -3, 5, 7, 8, 9, -10]
Rearrange positive and negative numbers of the said array:
[2, 5, 7, 8, 9, -10, -3, -1]

'''

list1 = [-1, 2, -3, 5, 7, 8, 9, -10]

list1.sort(key = lambda x: 0 if x == 0 else -1 / x)

print(list1)



