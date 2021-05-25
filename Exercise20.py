'''
20. Write a Python program to find the numbers of a given string and store them in a list,
display the numbers which are bigger than the length of the list in sorted form.
Use lambda function to solve the problem.
Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
Numbers in sorted form:
20 23 56

'''
str = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5".split()


function1 = lambda x : x if x.isdigit() else ''
function2 = lambda x : int(x) > len(result1) 

result1 = list(filter(function1,str))
result2 = list(filter(function2,result1))
result2.sort()

print(result2)

###############################################################################

str1 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
print("Original string: ",str1)
str_num=[i for i in str1.split(' ')]
lenght=len(str_num)
numbers=sorted([int(x) for x in str_num if x.isdigit()])
print('Numbers in sorted form:')
for i in ((filter(lambda x:x>lenght,numbers))):
    print(i,end=' ')