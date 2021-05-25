'''
13. Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
Number of even numbers in the above array: 3
Number of odd numbers in the above array: 5

'''

list1 = [1, 2, 3, 5, 7, 8, 9, 10]

count_even = lambda x : x % 2 == 0
count_odd = lambda x : x % 2 != 0

result1 = len(list(filter(count_even,list1)))
result2 = len(list(filter(count_odd,list1)))

print(f"Number of even numbers in the above list : {result1} ")
print(f"Number of odd numbers in the above list : {result2} ")