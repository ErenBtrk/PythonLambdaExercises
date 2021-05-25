'''
2. Write a Python program to create a function that takes one argument,
 and that argument will be multiplied with an unknown given number.
Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75

'''

def function(x):
    return lambda y : y * x

result = function(2)
print("Double the number of 15 = ",result(15)) 

result = function(3)
print("Double the number of 15 = ",result(15)) 

result = function(4)
print("Double the number of 15 = ",result(15)) 

result = function(5)
print("Double the number of 15 = ",result(15)) 


