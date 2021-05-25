'''
1. Write a Python program to create a lambda function that adds 15 to a given number
 passed in as an argument, also create a lambda function that multiplies argument x
  with argument y and print the result.
Sample Output:
25
48

'''

function1 = lambda num : num +15
function2 = lambda num1,num2 : num1*num2

print(function1(5))
print(function2(10,20))