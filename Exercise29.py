'''
29. Write a Python program to find the maximum value in a given heterogeneous list using lambda.
Original list:
['Python', 3, 2, 4, 5, 'version']
Maximum values in the said list using lambda:
5

'''

def findMax(list):
    return max(list,key = lambda i : (isinstance(i,int),i))

list1 = ['Python', 3, 2, 4, 5, 'version']

print(findMax(list1))