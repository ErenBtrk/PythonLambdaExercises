'''
9. Write a Python program to check whether a given string is number or not using Lambda.
Sample Output:
True
True
False
True
False
True
Print checking numbers:
True
True

'''

check_string = lambda x : True if(x.isdigit()) else False

print(check_string("213123"))
print(check_string("12s3asf"))
print(check_string("100"))