'''
24. Write a Python program to find numbers within a given range where every number
is divisible by every digit it contains.
Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

'''


def function(startNum,endNum):
    return [str(n) for n in range(startNum,endNum+1)]

list1 = function(1,22)

print(list1)


lambda1 = lambda x : [True if int(x) % int(item) == 0 else False for item in x] 


resultList = []




for item in list1:
    flag = True
    if('0' in item):
        continue
    list2 = lambda1(item)
    for item2 in list2:
        if(item2 == False):
            flag = False
    if(flag == True):
        resultList.append(item)

print(resultList)


################################################################################################

def divisible_by_digits(start_num, end_num):
    return [n for n in range(start_num, end_num+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
print(divisible_by_digits(1,22))

