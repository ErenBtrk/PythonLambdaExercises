'''
27. Write a Python program to sort each sublist of strings in a given list of lists using lambda. 
Original list:
[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
After sorting each sublist of the said list of lists:
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

'''
def sortSublist(list):
    return [sorted(x,key = lambda x : x[0]) for x in list]

list1 = [['green', 'orange'] , ['black', 'white'] , ['white', 'black', 'orange']]

print(sortSublist(list1))