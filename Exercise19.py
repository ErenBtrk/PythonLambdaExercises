'''
19. Write a Python program to find all anagrams of a string in a given list of strings using lambda.
Orginal list of strings:
['bcda', 'abce', 'cbda', 'cbea', 'adcb']
Anagrams of 'abcd' in the above string:
['bcda', 'cbda', 'adcb']

'''

from itertools import permutations 

list1 = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']

perm = list(permutations("abcd"))

permList = []

for item in perm:
    str = ""
    for item2 in item:
        str += item2
    permList.append(str)  

function1 = lambda x : x if (x in permList) else ''

result1 = list(filter(function1,list1))

print(result1)


#########################################################################################################


from collections import Counter  
texts = ["bcda", "abce", "cbda", "cbea", "adcb"]
str = "abcd"
print("Orginal list of strings:")
print(texts) 
result = list(filter(lambda x: (Counter(str) == Counter(x)), texts)) 
print("\nAnagrams of 'abcd' in the above string: ")
print(result)
