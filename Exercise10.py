'''
10. Write a Python program to create Fibonacci series upto n using Lambda.
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]
Fibonacci series upto 9:
[0, 1, 1, 2, 3, 5, 8, 13, 21]

'''

def function(n):
    list = []
    i = 0
    a = 1
    b = 1
    c = a+b
    while(i < n):
        list.append(a)
        a = b
        b = c
        c = a+b
        i += 1
    return list

print(function(10))

####################################################################################################

from functools import reduce
 
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                range(n-2), [0, 1])
 
print("Fibonacci series upto 2:")
print(fib_series(2))
print("\nFibonacci series upto 5:")
print(fib_series(5))
print("\nFibonacci series upto 6:")
print(fib_series(6))
print("\nFibonacci series upto 9:")
print(fib_series(9))
