'''
26. Write a Python program to find the list with maximum and minimum length using lambda. Go to the editor
Original list:
[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])

'''

def maxLengthList(list):
    maxLength = max(len(item) for item in list)
    maxList = max(list,key = lambda i : len(i))
    return(maxLength,maxList)

def minLengthList(list):
    minLength = min(len(item) for item in list)
    minList = min(list,key = lambda i : len(i))
    return(minLength,minList)

list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

print(f"max lenght list : {maxLengthList(list1)}")
print(f"min lenght list : {minLengthList(list1)}")

