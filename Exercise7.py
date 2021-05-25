'''
7. Write a Python program to find if a given string starts with a given character using Lambda.
Sample Output:
True
False

'''

def function1(string):
    return lambda char : char == string[0]

result = function1("Yarasa Reis")
print(result('Y'))

####################################################################################################

starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Python'))
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Java'))