'''
23. Write a Python program to calculate the sum of the positive and negative
 numbers of a given list of numbers using lambda function.
Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
Sum of the positive numbers: -32
Sum of the negative numbers: 48

'''

list1 = [2, 4, -6, -9, 11, -12, 14, -5, 17]

positive = lambda x : x > 0
negative = lambda x : x < 0

result1 = list(filter(positive,list1))
result2 = list(filter(negative,list1))


# positiveSum = 0
# for item in result1:
#     positiveSum += item

# negativeSum = 0
# for item in result2:
#     negativeSum += item

# print(f"Positive Sum = {positiveSum}")
# print(f"Negative Sum = {negativeSum}")


print(f"Positive Sum = {sum(result1)}")
print(f"Negative Sum = {sum(result2)}")


