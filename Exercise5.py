'''
5. Write a Python program to filter a list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]

'''

check_even = lambda num : num % 2 == 0
check_odd = lambda num : num % 2 != 0

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result1 = list(filter(check_even,list1))
result2 = list(filter(check_odd,list1))

print(result1)
print(result2)




